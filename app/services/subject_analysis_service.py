def analyze_subjects(df):
    student_data = {}

    for _, row in df.iterrows():
        name = row["name"]
        subject = row["subject"]
        week = int(row["week"])
        attendance = int(row["attendance"])

        if name not in student_data:
            student_data[name] = {}

        if subject not in student_data[name]:
            student_data[name][subject] = []

        student_data[name][subject].append((week, attendance))

    return student_data
