def generate_student_message(name, risk, path):
    return f"""
Hi {name},

Based on recent attendance trends, your academic status is classified as {risk} risk.

Recommended action:
{path}

Please follow this guidance to improve performance.
"""

def generate_parent_message(name, risk, path):
    return f"""
Dear Parent,

This is an academic update regarding your ward {name}.

Attendance analysis indicates a {risk} academic risk level.

Suggested intervention:
{path}

Early guidance can help improve academic outcomes.
"""
