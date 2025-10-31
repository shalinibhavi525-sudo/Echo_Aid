import speech_recognition as sr

def capture_voice(audio_bytes):
    if audio_bytes is None:
        return None
    
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio_bytes, 32000, 2)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
