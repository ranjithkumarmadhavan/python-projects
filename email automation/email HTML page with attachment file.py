import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import os

from_address = os.environ['EMAIL']
to_address = ["TO_EMAIL_ADDRESS"] #REPLACE with the to addresses you wish to send
message = MIMEMultipart()
message['From'] = from_address
message['To'] = " ,".join(to_address)
message['subject'] = 'Hello from SMTP'

with open('shoefeature.html') as file:
    htmlBody = file.read()
message.attach(MIMEText(htmlBody,'html'))

# adding attachment to email
attachmentFileName = 'readme.txt'
with open(attachmentFileName) as file:
    attachmentFile = file.read()
attachment = MIMEApplication(attachmentFile)
attachment.add_header('Content-Disposition', 'attachment; filename={}'.format(attachmentFileName))
message.attach(attachment)

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = message.as_string()
mail.sendmail(from_address,to_address,text)
mail.quit()