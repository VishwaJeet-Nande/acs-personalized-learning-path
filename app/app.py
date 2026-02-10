from flask import Flask, render_template, request
import pandas as pd

from services.learning_path_service import generate_learning_path
from services.subject_analysis_service import analyze_subjects
from utils.validation import validate_file, validate_dataframe

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return render_template("error.html", message="No file uploaded.")

    file_error = validate_file(file.filename)
    if file_error:
        return render_template("error.html", message=file_error)

    try:
        file.stream.seek(0)  # 🔥 CRITICAL FIX

        if file.filename.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")

    except Exception as e:
        print("READ ERROR:", e)
        return render_template("error.html", message="Unable to read uploaded file.")
    df.columns = df.columns.str.strip().str.lower()
    
    data_error = validate_dataframe(df)
    if data_error:
        return render_template("error.html", message=data_error)

    student_data = analyze_subjects(df)
    students = []

    for name, subject_data in student_data.items():
        risk, path = generate_learning_path(subject_data)
        students.append({
            "name": name,
            "risk": risk,
            "path": path
        })

    return render_template("result.html", students=students)

import json
from pathlib import Path

RULES_FILE = Path("config/rules.json")

@app.route("/admin/rules", methods=["GET"])
def view_rules():
    with open(RULES_FILE) as f:
        rules = json.load(f)
    return render_template("admin_rules.html", rules=rules)

@app.route("/admin/rules", methods=["POST"])
def update_rules():
    low = int(request.form["low_risk"])
    medium = int(request.form["medium_risk"])

    rules = {
        "attendance_thresholds": {
            "low_risk": low,
            "medium_risk": medium
        },
        "learning_paths": {
            "low": request.form["low_path"],
            "medium": request.form["medium_path"],
            "high": request.form["high_path"]
        }
    }

    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=2)

    return render_template("admin_success.html")

if __name__ == "__main__":
    app.run(debug=True)
