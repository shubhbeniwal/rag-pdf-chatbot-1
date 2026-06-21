import streamlit as st

from utils.pdf_loader import load_pdf
from utils.vector_store import create_chunks
from utils.vector_store import (
    create_chunks,
    create_vector_store
)
from utils.chatbot import (
    retrieve_context,
    generate_answer
)
if "messages" not in st.session_state:
    st.session_state.messages = []
    
st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="📚"
)

st.title("📚 RAG PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    text = load_pdf(uploaded_file)
    chunks = create_chunks(text)
    vector_db = create_vector_store(chunks)

    st.success("PDF Loaded Successfully!")

    st.subheader("Chunk Information")

    st.write(f"Total Chunks Created: {len(chunks)}")
    st.success("Vector Database Created Successfully!")
    st.subheader("Ask Questions About Your PDF")

question = st.chat_input(
    "Ask a question about your PDF..."
)

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Searching document..."):

        context, docs = retrieve_context(
            vector_db,
            question
        )

        answer = generate_answer(
            context,
            question
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    with st.expander("View Retrieved Context"):
        st.markdown("### 📚 Sources Used")

    for i, doc in enumerate(docs, start=1):

        st.info(
            f"Source Chunk {i}"
        )

        st.write(
            doc.page_content[:300] + "..."
        )
        st.text_area(
            "Context",
            context,
            height=300
        )

    if len(chunks) > 0:
        st.text_area(
            "First Chunk Preview",
            chunks[0],
            height=300
        )