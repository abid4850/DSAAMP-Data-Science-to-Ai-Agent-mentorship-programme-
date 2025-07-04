import os
import pandas as pd
from langchain_community.document_loaders import TextLoader, CSVLoader, PyPDFLoader, UnstructuredWordDocumentLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.base import VectorStoreRetriever
from typing import List

SUPPORTED_FORMATS = ['.txt', '.csv', '.pdf', '.docx']

def load_document(file_path: str):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == '.txt':
        loader = TextLoader(file_path)
    elif ext == '.csv':
        loader = CSVLoader(file_path)
    elif ext == '.pdf':
        loader = PyPDFLoader(file_path)
    elif ext == '.docx':
        loader = UnstructuredWordDocumentLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    return loader.load()

def create_vector_store(docs, persist_dir="chroma_rag_db"):
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    split_docs = text_splitter.split_documents(docs)
    vector_store = Chroma.from_documents(split_docs, embeddings, persist_directory=persist_dir)
    return vector_store

def get_retriever(vector_store, k=5) -> VectorStoreRetriever:
    return vector_store.as_retriever(search_kwargs={"k": k})
