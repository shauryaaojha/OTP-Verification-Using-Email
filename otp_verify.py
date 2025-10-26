from otp_send import send_otp

def verify_otp():
    """Handle OTP sending and verification."""
    email = input("Enter your email: ")
    sent_otp = send_otp(email)

    if not sent_otp:
        print("❌ Could not send OTP. Please try again later.")
        return

    entered_otp = input("Enter the OTP you received: ")

    if entered_otp == sent_otp:
        print("✅ OTP verified successfully!")
    else:
        print("❌ Incorrect OTP.")

if __name__ == "__main__":
    verify_otp()
