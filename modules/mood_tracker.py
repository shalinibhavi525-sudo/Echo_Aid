import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/mood_log.json")

def log_mood(mood):
    """Logs the user's mood with a timestamp."""
    data = load_mood_log()
    data.append({
        "mood": mood,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_mood_log(data)

def load_mood_log():
    """Loads the mood log from the JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_mood_log(data):
    """Saves the mood log to the JSON file."""
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
