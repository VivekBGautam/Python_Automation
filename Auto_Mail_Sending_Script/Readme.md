# Auto Mail Sending Script (Python)

## Aim
To develop a Python script that sends emails using Gmail SMTP with secure authentication (App Password).

---

## Description
This project is a simple Python-based email automation script that uses the built-in `smtplib` and `email` libraries to send emails via Gmail.

The script creates an email message, connects securely to Gmail’s SMTP server using SSL, logs in with an App Password, and sends the email to the specified receiver.

---

## Features
- Send email using Gmail SMTP server
- Secure connection using SSL (SMTP_SSL)
- Uses App Password for authentication
- Custom subject and message body
- Function-based implementation
- Easy to reuse and extend

---

## Technologies Used
- Python
- smtplib
- email.message.EmailMessage

---

## File Structure
```
Auto_Mail_Sending_Script/
│── Auto_mail_sender.py
│── README.md
```

---

## Working Flow
1. Create an email object using EmailMessage
2. Set sender, receiver, and subject
3. Add email body
4. Establish secure SMTP SSL connection (smtp.gmail.com:465)
5. Login using Gmail and App Password
6. Send email
7. Close connection

---

## How to Run

### 1. Install Python
Make sure Python is installed on your system.

### 2. Enable App Password (Important)
- Go to your Google Account
- Enable 2-Step Verification
- Generate App Password
- Use that password in the script

### 3. Run the Script
```bash
python Auto_Mail_Sender.py
```
## Function Used

def Vivek_send_mail(sender, app_password, receiver, subject, body):
 Security Warning 

Do NOT expose your App Password in public repositories

Use environment variables or .env file instead

Always use a temporary/test email account

## Example Output
Vivek Mail sent Succesfully

Future Improvements

Add multiple recipients support

Add file attachments

Add scheduling feature

Add logging system

Build GUI interface

## 👨‍💻 Author

### Name
Vivek Bhauraj Gautam

### Email: 
vivekbgautam@gmail.com

### GitHub: 
https://github.com/vivekbgautam

### LinkedIn: 
https://www.linkedin.com/in/vivek-b-gautam/
