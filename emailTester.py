# import smtplib, ssl

# port = 465  # For SSL
# password = input("Type your password and press enter: ")

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("ooduemailtest@gmail.com", password)
    
#     sender_email = "ooduemailtest@gmail.com"
#     receiver_email = "gubba.ricky@gmail.com"
#     message = """\
#     Subject: Hi there

#     This message is sent from Python."""

#     # Send email here
#     server.sendmail(sender_email, receiver_email, message)

import smtplib
from email.mime.text import MIMEText

subject = "Test 1"
body = "First Test!"
sender = "ooduemailtest@gmail.com"
recipients = ["gubba.ricky@gmail.com"] #Add your email here
password = "" #Add the App Password here


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)