from services.trend_analysis_service import analyze_trend
from services.rule_engine_service import apply_rules

def generate_learning_path(subject_data):
    all_attendance = []
    weak_subjects = []
    improving_subjects = []

    for subject, records in subject_data.items():
        records.sort(key=lambda x: x[0])
        attendance_list = [a for _, a in records]
        all_attendance.extend(attendance_list)

        trend = analyze_trend(attendance_list)

        if min(attendance_list) < 65:
            weak_subjects.append(subject)

        if trend == "Improving":
            improving_subjects.append(subject)

    avg_attendance = sum(all_attendance) // len(all_attendance)

    risk, base_path = apply_rules(avg_attendance)

    if weak_subjects:
        base_path += f". Focus on weak subjects: {', '.join(weak_subjects)}"

    if improving_subjects:
        base_path += f". Good improvement in: {', '.join(improving_subjects)}"

    return risk, base_path
