from textblob import TextBlob
import random
def analyze_emotion(text):
 blob = TextBlob(text)
 polarity = blob.sentiment.polarity
 if polarity > 0.2:
 mood = "positive"
 feedback = random.choice(["You sound happy today ■", "That’s a cheerful tone! Keep it up!"])
 elif polarity < -0.2:
 mood = "negative"
  feedback = random.choice(["You sound a bit tense ■", "Feeling low? Remember to breathe."])
 else:
 mood = "neutral"
 feedback = random.choice(["You sound calm and steady ■", "Balanced tone — peaceful energy."])
 return mood, feedback
