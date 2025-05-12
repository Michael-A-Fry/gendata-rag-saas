import streamlit as st

st.set_page_config(page_title="GenData RAG Assistant")
st.title("AI Document Assistant")

query = st.text_input("Ask a question about your documents:")
if query:
    st.write(f"Response: (simulate Vectara reply to: '{query}')")
