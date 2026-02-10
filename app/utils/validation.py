REQUIRED_COLUMNS = {"name", "subject", "week", "attendance"}

def validate_file(filename):
    if filename.endswith(".csv") or filename.endswith(".xlsx"):
        return None
    return "Only CSV or Excel (.xlsx) files are allowed."

def validate_dataframe(df):
    if df.empty:
        return "Uploaded file is empty."

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        return f"Missing required columns: {', '.join(missing)}"

    if (df["attendance"] < 0).any() or (df["attendance"] > 100).any():
        return "Attendance values must be between 0 and 100."

    return None
