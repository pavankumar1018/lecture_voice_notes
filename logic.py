import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import google.generativeai as genai  # ✅ Correct import

# 1️⃣ Load API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure Gemini client
genai.configure(api_key=API_KEY)

# 2️⃣ Speech-to-Text
def transcribe_audio(file):
    recognizer = sr.Recognizer()
    
    if file.type == "audio/mpeg":
        sound = AudioSegment.from_file(file)
        sound.export("temp.wav", format="wav")
        audio_file = sr.AudioFile("temp.wav")
    else:
        audio_file = sr.AudioFile(file)
    
    with audio_file as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Recognition error: {e}"

# 3️⃣ Generate Summary
def generate_summary(text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Summarize the following text in key points:\n\n{text}")
    return response.text.strip()

# 4️⃣ Generate Quiz
def generate_quiz(text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Create 5 multiple-choice questions (with answers) from this lecture text:\n\n{text}")
    return response.text.strip()
