from loaders.web_loader import load_urls
from processing.text_splitter import split_documents
from vectorstore.chroma_store import create_vector_store


urls = [
    "https://python.langchain.com/docs/integrations/text_embedding/",
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/concepts/rag/"
]

print("Loading URLs...")
documents = load_urls(urls)

print("Splitting...")
chunks = split_documents(documents)

print("Creating Vector Store...")
vector_store = create_vector_store(chunks)

print("Knowledge Base Ready!")