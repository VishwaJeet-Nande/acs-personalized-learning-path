import smtplib
from email.message import EmailMessage
import os

def send_email(to_email, subject, body):
    sender = os.getenv("ACS_EMAIL")
    password = os.getenv("ACS_EMAIL_PASSWORD")

    # DEMO SAFETY CHECK
    if not sender or not password:
        print("[EMAIL DISABLED] Missing credentials")
        print(body)
        return False

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print(f"[EMAIL SENT] → {to_email}")
        return True

    except Exception as e:
        print("EMAIL FAILED — FALLBACK MODE")
        print(e)
        print(body)
        return False
