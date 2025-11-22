import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import google.generativeai as genai  


API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

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

def generate_summary(text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Summarize the following text in key points:\n\n{text}")
    return response.text.strip()

def generate_quiz(text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Create 5 multiple-choice questions (with answers) from this lecture text:\n\n{text}")
    return response.text.strip()
