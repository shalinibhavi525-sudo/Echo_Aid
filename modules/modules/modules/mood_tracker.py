import json
from pathlib import Path
from datetime import datetime
DATA_FILE = Path("data/mood_log.json")
def log_mood(mood):
 data = load_mood_log()
 data.append({
 "mood": mood,
 "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 })
 DATA_FILE.parent.mkdir(exist_ok=True)
 with open(DATA_FILE, "w") as f:
 json.dump(data, f, indent=2)
def load_mood_log():
 if DATA_FILE.exists():
 with open(DATA_FILE, "r") as f:
 return json.load(f)
 return []
