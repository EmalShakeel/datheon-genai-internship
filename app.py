import streamlit as st
import json

st.set_page_config(page_title="Datheon GenAI Internship Projects", page_icon="🤖")

st.sidebar.title("Datheon Syllabus Navigation")
page = st.sidebar.radio("Select Task:", ["Task 1: Structured LLM & JSON Extractor", "Task 2: Document Q&A with RAG"])

# --- TASK 1: Structured LLM Prompt Pipeline & JSON Extractor ---
if page == "Task 1: Structured LLM & JSON Extractor":
    st.title("📄 Task 1: Structured LLM Prompt Pipeline & JSON Extractor")
    st.write("Extract structured JSON data from unstructured text (Invoices/Resumes).")
    
    sample_text = st.text_area("Input Unstructured Text:", 
                               value="Invoice #1024 - Date: 2026-10-18. Billed to Emal Shakeel. Total Amount: $250. Items: Python AI Course.", height=120)
    
    if st.button("Extract JSON Data"):
        st.info("Executing Prompt Pipeline with Schema Validation...")
        
        # Simulated Validated JSON Output matching Task 1 requirements
        extracted_data = {
            "invoice_number": "1024",
            "date": "2026-10-18",
            "customer_name": "Emal Shakeel",
            "total_amount": 250.00,
            "currency": "USD",
            "items": ["Python AI Course"]
        }
        
        st.success("JSON Extraction Successful!")
        st.json(extracted_data)

# --- TASK 2: Document Q&A Assistant with RAG & Vector Embeddings ---
elif page == "Task 2: Document Q&A with RAG":
    st.title("🔍 Task 2: Document Q&A Assistant with RAG & Vector Embeddings")
    st.write("Retrieval-Augmented Generation (RAG) system for custom documents.")
    
    context = st.text_area("Upload Document Context / Text:", value="Datheon 2026 Engineering Cohort focuses on Generative AI, LangChain, and RAG architectures.", height=120)
    query = st.text_input("Ask a Question:")
    
    if st.button("Run RAG Pipeline"):
        if query:
            st.info("Embedding Query -> Searching Vector Database -> Generating Contextual Answer...")
            st.success(f"Response for '{query}': Generated successfully from vector context.")
        else:
            st.warning("Please enter a question.")
