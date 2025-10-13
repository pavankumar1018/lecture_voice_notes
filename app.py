
# app.py
import streamlit as st
from logic import transcribe_audio, generate_summary, generate_quiz

# Page config
st.set_page_config(
    page_title="Voice Notes & Quiz",
    layout="wide",
    page_icon="🎤"
)

# Header Section
st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#4B8BBE;">🎤 Voice Lecture Notes & Quiz Generator</h1>
        <p style="font-size:16px;color:#555;">Upload a lecture audio file (.wav or .mp3) to generate transcript, summary, and quiz interactively.</p>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

# File upload
uploaded_file = st.file_uploader(
    "📂 Upload Audio File", type=["wav", "mp3"], 
    help="Choose a lecture audio file to transcribe."
)

# Only show rest if file is uploaded
if uploaded_file:
    st.info("🎬 Transcribing audio, please wait...")

    transcript = transcribe_audio(uploaded_file)

    # Using expander for transcript
    with st.expander("📝 Transcript", expanded=True):
        st.write(transcript)

    # Buttons in columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧠 Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = generate_summary(transcript)
            # Display summary in a card-style box
            st.success("✅ Summary Generated!")
            st.markdown(
                f'<div style="padding:10px; border-radius:10px; background-color:#f0f4f8;">{summary}</div>',
                unsafe_allow_html=True
            )

    with col2:
        if st.button("❓ Generate Quiz"):
            with st.spinner("Creating quiz..."):
                quiz = generate_quiz(transcript)
            st.success("✅ Quiz Generated!")
            st.markdown(
                f'<div style="padding:10px; border-radius:10px; background-color:#fff4e6;">{quiz}</div>',
                unsafe_allow_html=True
            )

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#888;">Made with ❤️ using Streamlit & Gemini AI</p>',
    unsafe_allow_html=True
)
