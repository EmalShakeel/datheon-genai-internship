import streamlit as st

st.set_page_config(page_title="Task 2 — Document Q&A Assistant", page_icon="📄")

st.title("📄 Document Question-Answering Assistant (RAG)")
st.write("Upload a `.txt` file or paste document text below, then ask a question based on its content.")

with st.sidebar:
    st.header("⚙️ RAG Settings")
    chunk_size = st.slider("Chunk Size (characters)", min_value=100, max_value=1000, value=300, step=50)
    top_k = st.slider("Top Matching Chunks", min_value=1, max_value=5, value=2)
    st.caption("Task 2 — Context-Grounded Document Q&A")

uploaded_file = st.file_uploader("Upload a text document (.txt)", type=["txt"])
doc_text = ""

if uploaded_file is not None:
    doc_text = uploaded_file.read().decode("utf-8", errors="ignore")

pasted_text = st.text_area(
    "Or paste document context here:",
    value=doc_text,
    height=150,
    placeholder="Paste notes, article, or project text here..."
)

question = st.text_input("Ask a question about the document:")

if st.button("Search & Answer"):
    context = pasted_text.strip()
    query = question.strip()

    if not context:
        st.warning("Please upload a `.txt` file or paste document text first.")
    elif not query:
        st.warning("Please enter a question to search in the document.")
    else:
        # Split text into chunks
        chunks = [context[i:i + chunk_size] for i in range(0, len(context), chunk_size)]
        query_words = [w.lower().strip(".,!?") for w in query.split() if len(w) > 2]

        # Score chunks by matching keywords
        scored = []
        for idx, ch in enumerate(chunks, start=1):
            ch_lower = ch.lower()
            score = sum(1 for qw in query_words if qw in ch_lower)
            scored.append((score, idx, ch))

        scored.sort(key=lambda x: x[0], reverse=True)
        matched = scored[:top_k]

        st.success("Retrieved relevant context chunks for your question.")
        st.markdown("### 💡 Answer / Relevant Context")

        best_score, best_idx, best_chunk = matched[0]
        if best_score > 0:
            st.write(f"**Best Match (Chunk #{best_idx}):** {best_chunk}")
        else:
            st.info("No exact keyword match found; showing top chunk from the document.")
            st.write(f"**Chunk #{best_idx}:** {best_chunk}")

        with st.expander("🔍 View Retrieved Chunks"):
            for sc, c_idx, c_val in matched:
                st.markdown(f"**Chunk #{c_idx}** *(Keyword Matches: {sc})*")
                st.write(c_val)