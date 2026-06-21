from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_core.documents import Document


def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_text(text)


def create_vector_store(documents):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings
    )

    return vector_db

def create_documents(pages):

    docs = []

    for page in pages:

        docs.append(
            Document(
                page_content=page["text"],
                metadata={
                    "page": page["page"]
                }
            )
        )

    return docs