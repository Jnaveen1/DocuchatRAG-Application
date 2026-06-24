from langchain_chroma import Chroma
from embeddings.embedder import get_embeddings


def create_vector_store(chunks):
    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="web_rag",
        persist_directory="./chroma_db"
    )

    return vector_store


def load_vector_store():
    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name="web_rag",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store