import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
RULES_PATH = os.path.join(BASE_DIR, "config", "rules.json")

def load_rules():
    with open(RULES_PATH) as f:
        return json.load(f)

def apply_rules(attendance_percent):
    rules = load_rules()

    thresholds = rules["attendance_thresholds"]
    paths = rules["learning_paths"]

    if attendance_percent >= thresholds["low"]:
        return "Low", paths["low"]
    elif attendance_percent >= thresholds["medium"]:
        return "Medium", paths["medium"]
    else:
        return "High", paths["high"]
