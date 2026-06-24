import streamlit as st

from vectorstore.chroma_store import load_vector_store
from rag.rag_chain import ask_question

st.set_page_config(
    page_title="DocuChat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 DocuChat")
st.write("Ask questions about the indexed websites")

@st.cache_resource
def get_vector_store():
    return load_vector_store()

vector_store = get_vector_store()

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            result = ask_question(
                question,
                vector_store
            )

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Sources")

        sources = set()

        for doc in result["source_documents"]:
            source = doc.metadata.get("source")

            if source not in sources:
                st.write(source)
                sources.add(source)