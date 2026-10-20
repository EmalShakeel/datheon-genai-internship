import streamlit as st

# Page Configuration
st.set_page_config(page_title="Datheon AI Assistant", page_icon="🤖")

st.title("🤖 Datheon GenAI & LangChain Internship")
st.write("Welcome to my AI-powered web application built using Python and Streamlit!")

# User Input Section
user_query = st.text_input("Ask something or type a prompt:")

if st.button("Generate Response"):
    if user_query:
        st.success(f"Processing your query: '{user_query}'")
        st.write("This is a functional prototype built for the Datheon internship program.")
    else:
        st.warning("Please enter a query first.")
