import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = ""     #SAMHIQ MAILER USERNAME AND EMAIL , USE SENDER EMAIL OR YOUR EMAIL ID
    sender_password = ""  # SAMHIQ MAILER CONFIGURATION, USE GMAIL APP PASSWORD

    recipient_email = recipient_entry.get()
    body = message_entry.get()

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Samhiq Pvt Ltd"
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        messagebox.showinfo("Success", "Email sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Samhiq Mailer")
root.geometry("400x300")  # SET THE INITIAL SIZE OF THE WINDOW FOR SAMHIQ MAILER

title_label = tk.Label(root, text="Samhiq Mailer", font=("Arial", 18, "bold"), pady=10)
title_label.pack()

recipient_label = tk.Label(root, text="Recipient Email:", font=("Arial", 12))
recipient_label.pack()

recipient_entry = tk.Entry(root, font=("Arial", 12))
recipient_entry.pack(pady=5)

message_label = tk.Label(root, text="Message:", font=("Arial", 12))
message_label.pack()

message_entry = tk.Entry(root, font=("Arial", 12))
message_entry.pack(pady=10)

send_button = tk.Button(root, text="Send Email", command=send_email, bg="#4CAF50", fg="white", font=("Arial", 12))
send_button.pack()

root.mainloop()
