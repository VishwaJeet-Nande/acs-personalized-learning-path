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

if __name__ == "__main__":
    app.run(debug=True)
