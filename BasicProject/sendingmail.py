
"""
For sending mails we have to use SMTP packages.
sending a request to the server
ALso using email.message module
"""
import smtplib

from email.message import EmailMessage

email = EmailMessage() ## Creating a object for EmailMessage
email['from'] = 'youremailid'   ## Person who is sending
email['to'] = 'senders email'       ## Whom we are sending
email['subject'] = 'Mail using python'  ## Subject of email
email.set_content("This is the mail you receive from python programming language.") ## content of email

#You to allow access in google account to send mail using smtp
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    #sending request to server
    smtp.ehlo()

    smtp.starttls()
    smtp.login('youremailid@gmail.com','Your password')
    smtp.send_message(email)
    print("Email Send")
