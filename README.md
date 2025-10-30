# Echo_Aid
Real-Time Emotion-Aware Speech Companion
> *"An AI that listens between the lines."*
EchoAid is a local prototype that listens to your voice and detects emotional tone — calm, anxious, happy, tired — to help you understand your own patterns of speech and stress.
It offers gentle feedback like *“You sound a bit tense, maybe take a small break?”* or *“Your tone feels calmer today.”*
Built as an **emotion-aware companion**, EchoAid promotes emotional wellness and mindful communication using lightweight local AI tools.
---
## ■ Features
- ■■ Listens to your voice in real time (via microphone)
- ■ Detects tone and sentiment
- ■ Provides gentle textual feedback and encouragement
- ■ Tracks daily emotion patterns and trends
- ■ Works fully offline and respects privacy
---
## ■ Architecture
```
User Voice → Voice Listener → Emotion Analyzer → Mood Tracker → UI Feedback
```
**Modules**
- `voice_listener.py`: captures and transcribes speech
- `emotion_analyzer.py`: detects tone, emotion, and sentiment
- `mood_tracker.py`: logs and visualizes emotional trends over time
---
## ■■ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
---
## ■ Future Expansion
- Integrate facial sentiment recognition
- Add personalized affirmations
- Sync with wearables for biofeedback
