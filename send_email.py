import smtplib
import config
import email_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message


sender_address = config.username
sender_pass = config.password

def compose_email(email_body,recipient):
    message=email.message.Message()
    message['From'] = sender_address
    message['To'] = recipient
    message['Subject'] = 'Birthday Greetings!'
    message.add_header('Content-Type', 'text/html')
    message.set_payload(email_body)
    return message

def send_email(message,receiver_address):
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    email_text = message.as_string()
    session.sendmail(sender_address, receiver_address, email_text)
    session.quit()

def compose_and_send_email(user):
    try:
        email_body=email_template.email_format.format(user.get("First Name"),user.get("Last Name"))
        message=compose_email(email_body,user.get("email"))
        send_email(message,user.get("email"))
        print ("Email sent successfully.")
    except:
        print ("There is an error sending the email.")
