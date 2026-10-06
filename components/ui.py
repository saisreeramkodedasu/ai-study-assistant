import streamlit as st


def show_header():

    st.title("📚 AI Study Assistant")

    st.write(
        "Upload your study material PDF, generate summaries, "
        "ask questions, and interact using your voice."
    )


def show_footer():

    st.divider()

    st.caption(
        "AI Study Assistant | "
        "PDF Processing + LLM + Summarization + "
        "Question Answering + STT + TTS + Streamlit"
    )