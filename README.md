# 📚 DocuMind AI – Intelligent Document Q&A System

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that allows users to upload one or more PDF documents and interact with them using natural language.

Built using modern GenAI technologies including LangChain, ChromaDB, HuggingFace Embeddings, Groq LLMs, and Streamlit.

---

## Screenshots

<img width="722" height="302" alt="image" src="https://github.com/user-attachments/assets/52b96dc8-661a-428d-a7ff-331e4105911c" />
<img width="550" height="349" alt="image" src="https://github.com/user-attachments/assets/c42b8993-43ed-4e1d-b618-fc35149c59e0" />

---

## 🔗 Live Demo: https://rag-pdf-chatbot-1-7lry23yvb65fb895gn3hdk.streamlit.app/

---

## 🚀 Features

### 📄 Multi-PDF Knowledge Base
Upload multiple PDF documents and query information across all of them simultaneously.

### 🔍 Semantic Search
Uses vector embeddings and similarity search to retrieve the most relevant document sections.

### 🤖 Conversational AI
Chat naturally with your documents using a Large Language Model (LLM).

### 🧠 Conversational Memory
Maintains chat history to support context-aware follow-up questions.

### 📚 Source Citations
Displays the retrieved source chunks used to generate answers.

### 📄 Page-Level References
Shows the page numbers from which information was retrieved.

### 📝 Document Summarization
Generate a concise summary of uploaded documents including:
- Executive Summary
- Key Topics
- Important Insights
- Key Takeaways

### 💡 Suggested Questions
Automatically generates relevant questions users can ask about the uploaded documents.

### ⚡ Fast Inference
Powered by Groq's ultra-fast LLM inference engine for responsive interactions.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │   PDF Uploads    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Text Extraction  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Document Parsing │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Page Metadata    │
                    │ Generation       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Embedding Model  │
                    │ HuggingFace      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ ChromaDB Vector  │
                    │ Database         │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Semantic Search  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Retrieved Context│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Groq Llama 3.3   │
                    │ Answer Generator │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Final Response   │
                    │ + Citations      │
                    └──────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### LLM
- Groq
- Llama 3.3 70B Versatile

### Retrieval Layer
- LangChain

### Vector Database
- ChromaDB

### Embeddings
- HuggingFace Embeddings
- all-MiniLM-L6-v2

### PDF Processing
- PyPDF

---

## 📂 Project Structure

```text
RAG-PDF-Chatbot/
│
├── app.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── vector_store.py
│   └── chatbot.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/shubhbeniwal/rag-pdf-chatbot-1.git

cd rag-pdf-chatbot-1
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create Environment File

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 6. Run Application

```bash
streamlit run app.py
```

---

## 💻 Example Use Cases

### Resume Analysis
Upload resumes and ask:

- What skills are mentioned?
- What certifications does the candidate have?
- Summarize the profile.

### Research Papers
Upload academic papers and ask:

- What are the key findings?
- What methodology was used?
- Summarize the conclusions.

### Business Documents
Upload reports and ask:

- What are the major insights?
- Summarize the executive section.
- What recommendations are provided?

---

## 🎯 Key Learnings Demonstrated

This project showcases practical AI Engineering concepts including:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embedding Models
- Large Language Model Integration
- Context-Aware Conversations
- Prompt Engineering
- Source Attribution
- AI Application Deployment
- End-to-End GenAI Product Development

---

## 📈 Future Improvements

- Hybrid Search (Keyword + Vector Search)
- OCR Support for Scanned PDFs
- PDF Highlighting
- User Authentication
- Chat Export
- Multi-Session Conversations
- Cloud Vector Database
- Agentic Document Analysis
- PDF Comparison Mode

---

## 🌐 Live Demo

https://rag-pdf-chatbot-1-7lry23yvb65fb895gn3hdk.streamlit.app/

---

## 👨‍💻 Author

### Shubh Beniwal

AI & Robotics Engineer

B.Tech Computer Science Engineering (AI & Robotics)

VIT Chennai

🔗 LinkedIn: https://www.linkedin.com/in/shubh-beniwal/

🔗 GitHub: https://github.com/shubhbeniwal

---

## ⭐ If you found this project useful, consider giving it a star!
