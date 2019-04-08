import smtplib
from email.mime.text import MIMEText

body = "This is a test email from Pranay.\nCreated from python.\nMy course on python has been completed successfully."

msg = MIMEText(body)
msg['From'] = "tyu@gmail.com"
msg['To'] = "xyz@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()
server.login("tyu@gmail.com", "tangocharlie")
server.send_message(msg)

print("Mail sent")

server.quit()