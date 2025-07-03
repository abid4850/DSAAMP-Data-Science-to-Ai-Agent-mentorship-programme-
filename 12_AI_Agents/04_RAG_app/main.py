import streamlit as st
import os
from langchain_ollama import OllamaLLM
from rag_utils import load_document, create_vector_store, get_retriever
from datetime import datetime

# --- Custom CSS for beautiful color scheme ---
st.markdown('''
    <style>
    body { background: linear-gradient(135deg, #f0f4ff 0%, #e0f7fa 100%) !important; }
    .stApp { background: linear-gradient(135deg, #f0f4ff 0%, #e0f7fa 100%) !important; }
    .main-header { color: #0a2540; font-size: 2.6rem; font-weight: 800; letter-spacing: 1px; }
    .stButton>button { background: linear-gradient(90deg, #6366f1, #06b6d4); color: white; font-weight: 600; border-radius: 8px; }
    .stFileUploader { background: #e0f2fe; border-radius: 10px; }
    .stTextInput>div>input { background: #f0f9ff; border-radius: 8px; }
    .stMarkdown h2 { color: #0ea5e9; }
    .stMarkdown h3 { color: #6366f1; }
    .stMarkdown h4 { color: #16a34a; }
    .stSidebar { background: #e0e7ff; }
    .stAlert { background: #fef9c3; }
    .stSuccess { background: #dcfce7; }
    .stSpinner { color: #6366f1; }
    </style>
''', unsafe_allow_html=True)

st.set_page_config(page_title="Universal RAG Q&A App", layout="wide")
st.sidebar.image("https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg", use_column_width=True)
st.sidebar.title("Universal RAG Q&A")
st.sidebar.markdown("<span style='color:#6366f1;font-weight:600;'>Ask questions from your own documents using local LLMs!</span>", unsafe_allow_html=True)
st.sidebar.info("Supports: CSV, PDF, Word, Text")
st.sidebar.markdown("---")

st.markdown('<div class="main-header">Universal RAG Q&A App</div>', unsafe_allow_html=True)
st.write("<span style='font-size:1.2rem;'>Upload a document (CSV, PDF, Word, or Text) and ask questions using Retrieval-Augmented Generation (RAG) with local LLMs!</span>", unsafe_allow_html=True)

# File upload
uploaded_file = st.file_uploader("Upload your document", type=["csv", "pdf", "docx", "txt"])

if uploaded_file:
    file_path = os.path.join("temp_uploads", uploaded_file.name)
    os.makedirs("temp_uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name}")

    # Load and embed document
    with st.spinner("Loading and embedding document..."):
        docs = load_document(file_path)
        vector_store = create_vector_store(docs)
        retriever = get_retriever(vector_store)
    st.success("Document indexed and ready for Q&A!")

    # Question input
    st.markdown("---")
    st.markdown("### Ask a question about your document:")
    question = st.text_input("Type your question here", key="question_input")
    if question:
        with st.spinner("Generating answer with local LLM..."):
            llm = OllamaLLM(model="llama3.2")
            context_docs = retriever.get_relevant_documents(question)
            context = "\n\n".join([d.page_content for d in context_docs])
            prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
            answer = llm.invoke(prompt)
        st.markdown(f"<div style='background:#e0f2fe;padding:18px 16px;border-radius:10px;'><b style='color:#0ea5e9;'>Answer:</b> {answer}</div>", unsafe_allow_html=True)
        with st.expander("Show retrieved context", expanded=False):
            for i, doc in enumerate(context_docs, 1):
                st.markdown(f"<b style='color:#6366f1;'>Chunk {i}:</b> <span style='color:#334155'>{doc.page_content}</span>", unsafe_allow_html=True)
        st.markdown("---")
        st.info(f"Answered at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.info("Please upload a document to get started.")

st.markdown("<hr style='margin-top:2em;margin-bottom:1em;border:1px solid #e0e7ff;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#64748b;font-size:1.1em;'>Made with ❤️ for local, private, and beautiful RAG Q&A. Powered by Ollama, ChromaDB, and Streamlit.</div>", unsafe_allow_html=True)
