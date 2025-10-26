import smtplib
import random
from email.message import EmailMessage

def generate_otp():
    """Generate a 6-digit random OTP."""
    return str(random.randint(100000, 999999))

def send_otp(receiver_email):
    """Send an OTP to the receiver's email."""
    otp = generate_otp()

    sender_email = "your_email@gmail.com"        # Replace with your Gmail
    app_password = "your_app_password"           # Replace with your App Password

    # Compose the email
    msg = EmailMessage()
    msg["Subject"] = "Your OTP Verification Code"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"Your OTP code is: {otp}\nThis code is valid for 5 minutes.\n\nThank you!")

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print(f"✅ OTP sent successfully to {receiver_email}")
    except Exception as e:
        print(f"❌ Failed to send OTP. Error: {e}")
        otp = None

    return otp
