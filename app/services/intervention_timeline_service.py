def generate_intervention_timeline(risk, weak_subjects):
    timeline = []

    if risk == "High":
        timeline = [
            "Week 1: Parent & student counseling",
            "Week 2: Faculty mentoring",
            "Week 3: Weekly assessments",
            "Week 4: Progress review meeting"
        ]

    elif risk == "Medium":
        timeline = [
            "Week 1: Faculty mentoring",
            "Week 2: Extra assignments",
            "Week 3: Improvement review"
        ]

    else:
        timeline = ["No intervention required"]

    if weak_subjects:
        timeline.append(f"Focus subjects: {', '.join(weak_subjects)}")

    return timeline
