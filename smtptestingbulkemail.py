from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import pandas as pd

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'email@gmail.com'
SENDER_PASSWORD = 'password##'
#https://www.google.com/settings/security/lesssecureapps

# Read CSV file and get email list
emaillist = pd.read_csv("testemails.csv")
to = emaillist['email_list'].tolist()

# Read email body text
with open('emailbodytext.txt', 'r') as f:
    emailbody = f.read()

def send_email(subject="Python email automation notification", text="", img=None, attachment=None):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        if img is not None:
            if not isinstance(img, list):
                img = [img]
            
            for one_img in img:
                with open(one_img, 'rb') as f:
                    img_data = f.read()
                msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

        if attachment is not None:
            if not isinstance(attachment, list):
                attachment = [attachment]
                
            for one_attachment in attachment:
                with open(one_attachment, 'rb') as f:
                    file = MIMEApplication(f.read(), name=os.path.basename(one_attachment))
                file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
                msg.attach(file)

        smtp.sendmail(from_addr=SENDER_EMAIL, to_addrs=to, msg=msg.as_string())

# Call the send_email function
send_email("Good!", emailbody, "imgtest.png", "testing.pdf")
