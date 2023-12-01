# SAIRA: Student Affairs AI Response Assistant

<h3 align="center">
<a href="https://huggingface.co/spaces/sairaproject/SAIRA"> 🔥 Streamlit Demo </a>|
<a href="https://youtu.be/KZKuOo5xT24"> 🖥️ Video Demo </a>|
<a href="./report/SAIRA Slides.pdf"> 📊 Slides </a>|
<a href="./report/report.pdf"> 📋 Report </a>
</h3>

<p align="center">
<img src="report/saira.png" alt="Saira" width="200"/>
</p>

## ✊ Team
- 🧑‍💻 **Vladimir Makharev** (Team Lead)
- 🧑‍💻 **Evgenii Evlampev** (ML Engineer)
- 🧑‍💻 **Danil Andreev** (Python Developer)
- 🧑‍💻 **Artem Batalov** (Dev&ML Ops)

## 🚀 Getting Started

1. **Install requirements**

   Clone the repository:
   ```bash
   git clone https://github.com/kilimanj4r0/SAIRA.git
   cd SAIRA
   ```

   Install requirements via pip:
   ```bash
   pip install -r requirements.txt
   CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
   ```

2. **Install Ollama** (to reproduce results from [2.0-solution-rag-ollama.ipynb](notebooks/2.0-solution-rag-ollama.ipynb))

   [Download ollama](https://ollama.ai/download), then run ollama server:
   ```bash
   ollama serve
   ```

   Download models:

   ```bash
   ollama pull llama2:13b
   ollama pull mistral
   ollama pull orca2:13b
   ollama pull vicuna:13b-16k
   ```

3. **Run demo**
   ```bash
   cd demo-streamlit
   streamlit run demo.py
   ```

## 📌 Introduction

SAIRA is an intelligent chatbot designed for the Student Affairs Office of our University. Powered by a Large Language Model (LLM), it aims to promptly address students' queries about various aspects of student life. Our initiative not only seeks to enhance the student experience but also ensures swift, efficient, and accurate dissemination of crucial information.

## 🔍 Features

- **Custom Knowledge Base Integration**: Leverage technologies like LlamaIndex, LangChain, or fine-tuning to Question Answering for institutional-specific data.
  
- **Intelligent Redirection Mechanism**: For complex or unsuitable queries, the bot redirects students to relevant specialists within the Student Affairs Office.
  
- **Feedback Mechanism**: Empowers students to rate the bot's performance, ensuring continuous improvement.

## 📘 Topics Covered

Students can inquire about:
- Dormitory rules
- Extracurricular activities
- Counselling services
- ... and much more!

## ⚙️ How It Works

1. **User Interaction**: The student interacts with the chatbot interface, inputting their query.
   
2. **Processing & Response Generation**: The system consults both the LLM and the custom knowledge base to generate a suitable response.

3. **Redirection (if necessary)**: In case the bot deems a question too complex or unsuitable, it triggers the redirection mechanism.

4. **Feedback Collection**: After receiving an answer, students have an option to provide feedback on the bot's response.
