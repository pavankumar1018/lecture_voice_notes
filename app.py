# app.py
import streamlit as st
from logic import transcribe_audio, generate_summary, generate_quiz

st.set_page_config(page_title="Voice Notes & Quiz", layout="wide")
st.title("Voice Lecture Notes & Quiz Generator")

st.write("Upload a lecture audio file (.wav or .mp3) to generate transcript, summary, and quiz.")

# Upload audio file
uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

if uploaded_file:
    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(uploaded_file)

    
    st.subheader("Transcript")
    st.write(transcript)
    
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(transcript)
            print(summary)
        st.subheader("Summary")
        st.write(summary)
        
    if st.button("Generate Quiz"):
        with st.spinner("Creating quiz..."):
            quiz = generate_quiz(transcript)
        st.subheader("Quiz")
        st.write(quiz)
