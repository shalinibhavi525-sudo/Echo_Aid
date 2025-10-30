import speech_recognition as sr
def capture_voice():
 recognizer = sr.Recognizer()
 with sr.Microphone() as source:
 print("Listening...")
 audio = recognizer.listen(source, phrase_time_limit=5)
 try:
 text = recognizer.recognize_google(audio)
 return text
 except sr.UnknownValueError:
 return None
 except sr.RequestError:
 return None
