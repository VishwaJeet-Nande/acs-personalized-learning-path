from collections import defaultdict

def analyze_subjects(df):
    students = defaultdict(lambda: defaultdict(lambda: {
        "attendance": [],
        "weeks": []
    }))

    for _, row in df.iterrows():
        name = row["name"]
        subject = row["subject"]

        students[name][subject]["attendance"].append(int(row["attendance"]))
        students[name][subject]["weeks"].append(int(row["week"]))

    return students
