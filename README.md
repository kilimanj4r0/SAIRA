# SAIRA: Student Affairs AI Response Assistant

![gm52qm91gjycxi4htfrnmgq26vb1px4v](https://github.com/bart02/SAIRA/assets/19249148/b87beaa4-e256-43de-938f-709384f439bf)

### ✊ Team
- **Vladimir Makharev** (Team Lead)
- **Evgenii Evlampev** (ML Engineer)
- **Danil Andreev** (Python Developer)
- **Artem Batalov** (Dev&ML Ops)

## 🖥️ Demo video
https://youtu.be/KZKuOo5xT24

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

## 🚀 Getting Started

1. **Installation**:
   ```bash
   git clone https://github.com/bart02/SAIRA.git
   cd SAIRA
   pip install -r requirements.txt
   CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
   ```

2. **Run demo**:
   ```bash
   streamlit run demo.py
   ```
