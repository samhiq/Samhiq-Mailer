# 📧 **Samhiq-Mailer** 🚀
# Basic Version
---
**Sending Emails Made Simple and Stylish!**

**Welcome to Samhiq-Mailer**, a Python tool designed for effortless email sending via SMTP and Gmail. It combines a user-friendly Tkinter-based interface with robust features to make your email experience smooth and efficient.

## 🌟 Features

- **User-Friendly Interface:** Enjoy the simplicity of a Tkinter-based graphical interface.
- **Gmail and SMTP Integration:** Seamlessly connect to Gmail and SMTP for efficient email dispatch.
- **Lightweight and Efficient:** A quick and efficient tool tailored for smooth email sending.

## 📋 Required Modules

Make sure you have the following modules installed:

```bash
smtplib
tkinter
```

## ⚙️ Requirements

Ensure you meet the prerequisites before using Samhiq-Mailer:

```bash
pkg install git -y 
pkg install python -y 
```

## 🔒 Setting Up App Password for SMTP Access

Supercharge Samhiq-Mailer with Gmail's SMTP by creating an App Password:

1. **Enable 2-Step Verification:**
   - Visit [Google Account Security](https://myaccount.google.com/security-checkup).
   - Enable 2-Step Verification if not already enabled.

2. **Access App Passwords:**
   - Under "Security," click on "App passwords" or a similar option.

3. **Generate App Password:**
   - In "Select app," choose "Other (Custom name)."
   - Specify a custom name (e.g., "Samhiq-Mailer") and click "Generate."

4. **Copy App Password:**
   - Google will generate a unique 16-digit app password.
   - Copy this password; you'll use it to authenticate Samhiq-Mailer with Gmail.

5. **Use App Password in Samhiq-Mailer:**
   - When prompted for your Gmail password, use the app password generated earlier.
   - This app password ensures secure access via SMTP without revealing your main password.

## 🌐 SMTP Configuration

Configure Samhiq-Mailer to use Gmail's SMTP for sending emails:

1. **SMTP Host Configuration** 🌐
   - Open `samhiqmail.py` in your text editor.
   - Find the SMTP host configuration section and set the SMTP host to `"smtp.gmail.com"`.

```python
# SMTP Configuration
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587  # Gmail's SMTP port
```

2. **App Password Integration** 🔑
   - In the same `samhiqmail.py`, locate the section where the password is prompted.
   - Replace the placeholder with the App Password generated earlier.

```python
# Email Account Information
EMAIL_ADDRESS = "your.email@gmail.com"  # Your Gmail email address
EMAIL_PASSWORD = "your_generated_app_password"  # App Password for Samhiq-Mailer
```

3. **Enjoy Sending Emails!** 🚀
   - Save your changes and run `python samhiqmail.py`.
   - Experience the magic of Samhiq-Mailer sending emails via Gmail's secure SMTP.

Now you're all set to elevate your email experience with Samhiq-Mailer. For any questions or assistance, feel free to reach out. Happy emailing! 📧✨

**Author: Samhiq**

**Thanks for Using Samhiq-Mailer!**

For inquiries or assistance, don't hesitate to reach out. Happy emailing! 🚀📧✨
