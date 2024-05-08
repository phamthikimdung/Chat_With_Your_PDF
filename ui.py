import streamlit as st

def show_upload_ui():
    st.title("Chat With Your File PDF Tool 📈")
    st.sidebar.title("Chat With Your File PDF")
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    return pdf

def show_query_input():
    return st.text_input("Ask a question about your PDF File")