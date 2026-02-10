import json

def load_rules():
    with open("config/rules.json") as f:
        return json.load(f)

def apply_rules(avg_attendance):
    rules = load_rules()
    thresholds = rules["attendance_thresholds"]
    paths = rules["learning_paths"]

    if avg_attendance >= thresholds["low_risk"]:
        return "Low", paths["low"]
    elif avg_attendance >= thresholds["medium_risk"]:
        return "Medium", paths["medium"]
    else:
        return "High", paths["high"]
