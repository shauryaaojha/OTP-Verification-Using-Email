# 🔐 Email OTP Verification using Python

This project implements a simple **OTP (One-Time Password) verification system** using **Python** and **email (SMTP)**.
It generates a random 6-digit OTP, sends it to the user’s email address, and verifies the OTP entered by the user.

---

## 🚀 Features

* Generates a random 6-digit OTP
* Sends OTP to user’s email using **SMTP (Gmail SMTP server)**
* Verifies OTP entered by the user
* Includes error handling for wrong OTP and email issues
* Simple and beginner-friendly Python implementation

---

## 🧠 Prerequisites

Make sure you have the following installed:

* Python 3.x
* An active Gmail account (for sending OTPs)

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/shauryaaojha/OTP-Verification-Using-Email.git
   cd OTP-Verification-Using-Email
   ```

2. Install required Python libraries:

   ```bash
   pip install smtplib email
   ```

*(Note: `smtplib` and `email` are included with Python by default, so you might not need to install them separately.)*

---

## ⚙️ Configuration

Before running the script, you need to allow your Gmail account to send emails using **App Passwords**:

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security).
2. Enable **2-Step Verification**.
3. Create an **App Password** for “Mail”.
4. Copy the 16-character app password.

Then, replace your credentials in the script:

```python
sender_email = "your_email@gmail.com"
app_password = "your_app_password"
```

---

## ▶️ Usage

Run the script:

```bash
python otp_verification.py
```

Enter the recipient’s email and check for the OTP in the inbox.
Then enter the OTP in the terminal to verify.

---

## 🧩 Example Output

```
Enter your email: testuser@example.com
OTP sent successfully to testuser@example.com
Enter the OTP you received: 429318
OTP verified successfully! ✅
```

If the user enters a wrong OTP:

```
Enter the OTP you received: 123456
Incorrect OTP ❌
```

---

## ⚠️ Notes

* OTP is valid for one-time use only.
* Never hardcode your actual Gmail password — use **App Passwords**.
* This project is for **educational purposes** only and should not be used in production without proper security practices (e.g., encryption, rate limiting, etc.).

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use and modify it for your own learning.


