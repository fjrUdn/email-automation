import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from dotenv import load_dotenv

# Load file .env
load_dotenv()

# Ambil data dari .env
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("EMAIL_PASSWORD")


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Setup SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    # Write the email's body
    body = f"""Hi {name},
    
I hope you are well.
    
I just wanted to drop you a quick note to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}.
    
I would be really grateful if you could confirm that everything is on track for payment.
    
Best regards
Fajar Kamaludin A
"""
    message = MIMEMultipart()
    message['From'] = formataddr(("Coding Is Fun Corp.", f"{sender_email}"))
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server.send_message(message)
    # print(f"Email terkirim ke {name} ({receiver_email})")
if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="John Doe",
        receiver_email="fajarimansyah45@gmail.com",
        due_date="11, Aug 2022",
        invoice_no="INV-21-12-009",
        amount="5",
    )
