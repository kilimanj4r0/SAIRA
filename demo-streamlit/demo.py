import streamlit as st
import random
import time
from index import build_index, build_service_context
from loader import load_documents 

st.title("Simple chat")

@st.cache_data
def load_docs_and_build_index(context):
    docs = load_documents()
    return build_index(docs, context)

@st.cache_resource
def load_context():
    return build_service_context()

context = load_context()
index = load_docs_and_build_index(context)
query_engine = index.as_query_engine(streaming=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        resp = query_engine.query(prompt)
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        # Simulate stream of response with milliseconds delay
        for text in resp.response_gen:
            full_response += text
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})