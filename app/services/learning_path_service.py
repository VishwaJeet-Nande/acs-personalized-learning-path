from services.trend_analysis_service import analyze_trend
from services.rule_engine_service import apply_rules

def generate_learning_path(subject_data):
    all_attendance = []
    weak_subjects = []
    improving_subjects = []

    for subject, records in subject_data.items():

        # 🔒 SAFETY CHECK
        if not records:
            continue

        # ✅ If single number → convert to list
        if isinstance(records, (int, float)):
            attendance_list = [records]

        # ✅ If list of numbers
        elif isinstance(records, list) and isinstance(records[0], (int, float)):
            attendance_list = records

        # ✅ If list of tuples → (date, attendance)
        elif isinstance(records, list) and isinstance(records[0], tuple):
            records.sort(key=lambda x: x[0])
            attendance_list = [a for _, a in records]

        else:
            continue

        # 🧠 Collect data
        all_attendance.extend(attendance_list)

        # 📉 Weak subject
        if min(attendance_list) < 65:
            weak_subjects.append(subject)

        # 📈 Trend
        trend = analyze_trend(attendance_list)
        if trend == "Improving":
            improving_subjects.append(subject)

    # 🚨 NO DATA CASE
    if not all_attendance:
        return "Low", "No attendance data available."

    avg_attendance = sum(all_attendance) // len(all_attendance)
    risk, base_path = apply_rules(avg_attendance)

    if weak_subjects:
        base_path += f". Focus on weak subjects: {', '.join(weak_subjects)}"

    if improving_subjects:
        base_path += f". Good improvement in: {', '.join(improving_subjects)}"

    return risk, base_path
