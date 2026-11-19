import streamlit as st

# Page Configuration
st.set_page_config(page_title="Datheon AI Assistant", page_icon="🤖")

st.title("🤖 Datheon GenAI & LangChain Internship")
st.write("Welcome to my AI-powered web application built using Python and Streamlit!")

# Sidebar Controls
with st.sidebar:
    st.header("⚙️ Settings")
    response_mode = st.selectbox(
        "Select Output Format:",
        ["Structured Summary", "Bullet Points", "Text Stats & Clean"]
    )
    st.caption("Task 1 — Interactive Web Interface")

# User Input Section
user_query = st.text_area("Ask something or type a prompt:", height=110)

col1, col2 = st.columns([1, 1])
with col1:
    generate_clicked = st.button("Generate Response")
with col2:
    clear_clicked = st.button("Clear")

if clear_clicked:
    st.rerun()

if generate_clicked:
    if user_query.strip():
        clean_text = " ".join(user_query.strip().split())
        st.success(f"Processed query: '{clean_text}'")

        if response_mode == "Structured Summary":
            st.markdown("### 📌 Structured Output")
            st.markdown(f"**Input Received:** {clean_text}")
            st.markdown(
                "**Draft Response:** Yeh ek sample structured response format hai jo "
                "prompt input ko clear headings aur sections mein organize karta hai."
            )

        elif response_mode == "Bullet Points":
            st.markdown("### 🔹 Key Points View")
            words = clean_text.split()
            st.write(f"- **Query Length:** {len(words)} words")
            st.write(f"- **Selected Mode:** {response_mode}")
            st.write("- **Status:** Ready for LangChain / LLM pipeline integration")

        elif response_mode == "Text Stats & Clean":
            st.markdown("### 🧹 Cleaned Text & Statistics")
            words = clean_text.split()
            st.write(f"**Word Count:** {len(words)} | **Character Count:** {len(clean_text)}")
            st.code(clean_text, language="text")
    else:
        st.warning("Please enter a prompt or text first.")

st.caption("This is a functional prototype built for the Datheon internship program.")