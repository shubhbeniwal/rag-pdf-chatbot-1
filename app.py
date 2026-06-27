import streamlit as st

from utils.pdf_loader import load_pdf

from utils.vector_store import (
    create_vector_store,
    create_documents
)

from utils.chatbot import (
    retrieve_context,
    generate_answer,
    summarize_document,
    generate_suggested_questions
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="RAG PDF Chatbot | Shubh Beniwal",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📚 DocuMind AI – Intelligent Document Q&A System")

st.markdown("""
### AI-Powered Multi-Document Question Answering System

Upload one or more PDF documents and interact with them using Retrieval-Augmented Generation (RAG), semantic search, and Large Language Models.

#### Features

- Multi-PDF Knowledge Base
- Semantic Search
- Conversational AI
- Document Summarization
- Source Citations
- Suggested Questions

👨‍💻 Built by **Shubh Beniwal**
""")

st.divider()

st.sidebar.title("🚀 About the Creator")

st.sidebar.markdown("""
### Shubh Beniwal

## AI Engineer | Software Developer

VIT Chennai Graduate | Passionate about AI, LLMs, NLP, and Software Engineering


---

### Project

RAG PDF Chatbot

Upload PDFs and chat with them using Retrieval-Augmented Generation (RAG).

---

### Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq LLM

---
""")

st.sidebar.markdown(
    "[GitHub](https://github.com/shubhbeniwal)"
)

st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/in/shubh-beniwal/)"
)
# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

# -----------------------------
# PROCESS PDFs
# -----------------------------
if uploaded_files:

    all_pages = []

    for pdf in uploaded_files:

        pages = load_pdf(pdf)

        all_pages.extend(pages)

    documents = create_documents(all_pages)

    vector_db = create_vector_store(documents)

    st.success("✅ PDF Loaded Successfully")

    st.info(
        f"{len(uploaded_files)} document(s) loaded"
    )

    st.success("✅ Vector Database Created Successfully")
    st.markdown("---")

    st.subheader("📄 Document Summary")

    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):

            full_context = "\n\n".join(
                [
                    doc.page_content
                    for doc in documents
                ]
            )

            summary = summarize_document(
                full_context[:12000]
            )

        st.markdown(summary)

    st.markdown("---")
    
    st.subheader("💡 Suggested Questions")

    if st.button("Generate Suggested Questions"):

        with st.spinner("Generating questions..."):

            full_context = "\n\n".join(
                [
                    doc.page_content
                    for doc in documents
                ]
            )

            suggestions = generate_suggested_questions(
                full_context[:12000]
            )

        st.markdown(suggestions)

    st.markdown("---")
    # -----------------------------
    # DISPLAY CHAT HISTORY
    # -----------------------------
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # -----------------------------
    # CHAT INPUT
    # -----------------------------
    question = st.chat_input(
        "Ask a question about your documents..."
    )

    if question:

        # User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Searching documents..."):

            context, docs = retrieve_context(
                vector_db,
                question
            )

            chat_history = "\n".join(
                [
                    f"{msg['role']}: {msg['content']}"
                    for msg in st.session_state.messages
                ]
            )

            answer = generate_answer(
                context,
                question,
                chat_history
            )

        # Assistant Message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        # -----------------------------
        # SOURCES
        # -----------------------------
        with st.expander("📚 View Sources"):

            for doc in docs:

                page_number = doc.metadata.get(
                    "page",
                    "Unknown"
                )

                st.info(
                    f"📄 Page {page_number}"
                )

                st.write(
                    doc.page_content[:300] + "..."
                )

        # -----------------------------
        # RETRIEVED CONTEXT
        # -----------------------------
        with st.expander("🔍 View Retrieved Context"):

            st.text_area(
                "Context",
                context,
                height=300
            )
