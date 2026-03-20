#========================================================================
# Program    :   Simple Gmail Mail Sender
# Author     :   Vivek Bhauraj Gautam
# Purpose    :   Send mail using python SMTP
#========================================================================

import smtplib
from email.message import EmailMessage

#------------------------------------------------------------------------
# Function  : Vivek_send_mail
# Description    : Sends emial using  Gmail SMTP server
#------------------------------------------------------------------------
def Vivek_send_mail(sender,app_password, receiver,subject,body):

    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    #Step 3 : Add mail body
    msg.set_content(body)

    # Step 4: Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Step 5 : Login using Gmail + App Password
    smtp.login(sender,app_password)

    # St5ep 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close connection mannually
    smtp.quit()

#--------------------------------------------------------------------
# Funnction  : Main
# Description : Driver code 
#--------------------------------------------------------------------
def main():
    
    # Always use seprate temprary/ testing Account 
    sender_email = "vivekgautampython@gmail.com"

    # App Password genrate from google account
    app_password = "laxt gboy aeid gdlg"

    # your second email for testing
    reciever_email = "7498226486vivek@gmail.com"

    Subject = "Test mail from python Script"

    body = """ Jay Ganesh,

This is a test mail sent using Vivek Python Autmotion script

Regards,
Vivek Gautam
"""
    
    Vivek_send_mail(sender_email,app_password,reciever_email,Subject,body)

    print("Vivek Mail sent Succesfully")

    #------------------------------------------
    # program entry point
    #------------------------------------------
if __name__ == "__main__":
    main()

    
    

    