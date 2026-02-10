def analyze_subjects(df):
    students = {}

    for _, row in df.iterrows():
        name = row["name"]
        subject = row["subject"]
        week = int(row["week"])
        attendance = int(row["attendance"])

        if name not in students:
            students[name] = {
                "subjects": {},
                "student_email": row.get("student_email"),
                "parent_email": row.get("parent_email")
            }

        if subject not in students[name]["subjects"]:
            students[name]["subjects"][subject] = []

        students[name]["subjects"][subject].append((week, attendance))

    return students
