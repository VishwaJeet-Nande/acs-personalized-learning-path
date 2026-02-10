def generate_intervention_timeline(risk, weak_subjects):
    timeline = []

    if risk == "High":
        timeline = [
            "Week 1: Immediate faculty mentoring session",
            f"Week 2: Remedial classes for {', '.join(weak_subjects)}",
            "Week 3: Parent–teacher meeting",
            "Week 4: Attendance and performance re-evaluation"
        ]

    elif risk == "Medium":
        timeline = [
            f"Week 1: Focused mentoring in {', '.join(weak_subjects)}",
            "Week 2: Weekly attendance monitoring",
            "Week 3: Academic progress review"
        ]

    else:  # Low risk
        timeline = [
            "Continue current learning strategy",
            "Monthly attendance review"
        ]

    return timeline
