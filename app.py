import streamlit as st

from services.pdf_service import extract_text_from_pdf
from services.llm_service import ask_llm

from services.speech_service import transcribe_audio
from services.tts_service import text_to_speech

from prompts.prompts import (
    create_summary_prompt,
    create_question_prompt,
    create_voice_question_prompt
)

from components.ui import (
    show_header,
    show_footer
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

show_header()


# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

st.header("📄 Upload Study Material")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    # Extract PDF text
    extracted_text = extract_text_from_pdf(uploaded_file)

    if not extracted_text.strip():

        st.warning(
            "No readable text was found in this PDF."
        )

        st.stop()


    st.info(
        f"PDF text extracted successfully "
        f"({len(extracted_text)} characters)."
    )


    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------

    st.header("📝 Study Summary")

    if st.button("Generate Summary"):

        with st.spinner("Generating summary..."):

            summary_prompt = create_summary_prompt(
                extracted_text
            )

            summary = ask_llm(summary_prompt)

        st.markdown(summary)


    # --------------------------------------------------
    # TEXT QUESTION ANSWERING
    # --------------------------------------------------

    st.header("❓ Ask a Question")

    question = st.text_input(
        "Enter your question about the uploaded PDF:"
    )


    if st.button("Ask Question"):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner("Finding the answer..."):

                question_prompt = create_question_prompt(
                    extracted_text,
                    question
                )

                answer = ask_llm(question_prompt)


            st.subheader("Answer")

            st.write(answer)


            # Text-to-Speech
            try:

                audio_file = text_to_speech(answer)

                st.audio(
                    audio_file,
                    format="audio/mp3"
                )

            except Exception as error:

                st.warning(
                    f"Could not generate audio: {error}"
                )


    # --------------------------------------------------
    # VOICE QUESTION
    # --------------------------------------------------

    st.header("🎤 Voice Question")

    st.write(
        "Record your question and the AI will answer "
        "using the uploaded PDF."
    )


    audio_input = st.audio_input(
        "Record your question"
    )


    if audio_input is not None:

        if st.button("Process Voice Question"):

            with st.spinner(
                "Converting your voice to text..."
            ):

                voice_question = transcribe_audio(
                    audio_input
                )


            if voice_question:

                st.subheader("Recognized Question")

                st.write(voice_question)


                with st.spinner(
                    "Generating answer..."
                ):

                    voice_prompt = (
                        create_voice_question_prompt(
                            extracted_text,
                            voice_question
                        )
                    )

                    voice_answer = ask_llm(
                        voice_prompt
                    )


                st.subheader("Answer")

                st.write(voice_answer)


                # Convert answer to speech
                try:

                    voice_audio = text_to_speech(
                        voice_answer
                    )

                    st.audio(
                        voice_audio,
                        format="audio/mp3"
                    )

                except Exception as error:

                    st.warning(
                        f"Could not generate audio: {error}"
                    )

            else:

                st.warning(
                    "Could not understand the recorded audio."
                )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

show_footer()