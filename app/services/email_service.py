import smtplib
import os
from email.message import EmailMessage

def send_email(to_email, subject, body):
    sender = os.getenv("ACS_EMAIL")
    password = os.getenv("ACS_EMAIL_PASSWORD")

    # Fallback if credentials missing
    if not sender or not password:
        print(f"[SIMULATED EMAIL] To: {to_email}")
        print(subject)
        print(body)
        return "SIMULATED"

    try:
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

        return "SENT"

    except Exception as e:
        print("EMAIL FAILED — FALLBACK MODE")
        print(e)
        print(f"[SIMULATED EMAIL] To: {to_email}")
        print(subject)
        print(body)
