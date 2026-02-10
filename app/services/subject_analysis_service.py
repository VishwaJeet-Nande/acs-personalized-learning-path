def analyze_subjects(df):
    data = {}

    for _, row in df.iterrows():
        name = row["name"]

        if name not in data:
            data[name] = {
                "subjects": {},
                "student_email": row.get("student_email"),
                "parent_email": row.get("parent_email")
            }

        subject = row["subject"]
        attendance = row["attendance"]

        data[name]["subjects"][subject] = attendance

    return data
