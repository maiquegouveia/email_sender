from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from smtplib import SMTPException

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'ENTER SENDER EMAIL HERE'
password = "ENTER SENDER'S EMAIL PASSWORD HERE" # YOU NEED TO ENABLE 2-STEP VERIFICATION AND THEN GENERATE PERSONALIZED APP PASSWORDS
receiver_email = 'ENTER RECEIVER EMAIL HERE'

msg = MIMEMultipart()
msg['From'] = 'ENTER SENDER NAME HERE'
msg['To'] = receiver_email
msg['Subject'] = 'ENTER THE SUBJECT HERE'
message = 'ENTER THE BODY MESSAGE HERE'
msg.attach(MIMEText(message))

# Secure ssl context
context = ssl.create_default_context()
# Trying to log in to server
server = smtplib.SMTP(smtp_server, port)
try:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Message has been sent")
except SMTPException:
    print('Message could not be sent')
finally:
    server.quit()