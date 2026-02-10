from services.trend_analysis_service import analyze_trend
from services.rule_engine_service import apply_rules

def generate_learning_path(subject_data):
    all_attendance = []
    weak_subjects = []

    for subject, data in subject_data.items():
        attendance_list = data["attendance"]

        if not attendance_list:
            continue

        all_attendance.extend(attendance_list)

        if min(attendance_list) < 65:
            weak_subjects.append(subject)

    if not all_attendance:
        return "Low", "No attendance data available.", []

    avg_attendance = sum(all_attendance) // len(all_attendance)

    risk, base_path = apply_rules(avg_attendance)

    if weak_subjects:
        base_path += f". Focus on weak subjects: {', '.join(weak_subjects)}"

    return risk, base_path, weak_subjects
