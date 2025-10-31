import streamlit as st
from modules.voice_listener import capture_voice
from modules.emotion_analyzer import analyze_emotion
from modules.mood_tracker import log_mood, load_mood_log
st.set_page_config(page_title="EchoAid | Emotion-Aware Companion", page_icon="■", layout="wide")
st.title("■ EchoAid")
st.subheader("Real-Time Emotion-Aware Speech Companion")
st.markdown("Speak to EchoAid — it listens and gently reflects your tone back to you.")
if st.button("■■ Start Listening"):
 st.info("Listening... please speak clearly.")
 text = capture_voice()
 if text:
  st.markdown(f"**You said:** {text}")
 mood, feedback = analyze_emotion(text)
 st.success(feedback)
 log_mood(mood)
 else:
  st.warning("Could not detect any speech. Try again.")
if st.button("■ Show Mood Log"):
 moods = load_mood_log()
 if moods:
 st.markdown("### ■ Mood Log")
 for entry in moods:
 st.write(f"- {entry['mood']} — {entry['timestamp']}")
 else:
 st.info("No mood data yet. Speak to EchoAid first!")
