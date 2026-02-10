def analyze_trend(attendance_list):
    if len(attendance_list) < 2:
        return "Stable"

    if attendance_list[-1] > attendance_list[0]:
        return "Improving"
    elif attendance_list[-1] < attendance_list[0]:
        return "Declining"
    else:
        return "Stable"
