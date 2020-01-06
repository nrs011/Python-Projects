import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

def send_email(user, pwd, recipient, subject, df):
    try:
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] =user
        msg['To'] = recipient

        #Create the body of the message (a plain-text and an HTML version).

        df_html = df.to_html()

        # Record the MIME types of both parts - text/plain and text/html.
        part2 = MIMEText(df_html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part2)

        # Send the message via local SMTP server.
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        server.sendmail(user, recipient, msg.as_string())
        server.close()

        print('successfully sent the mail')

    except Exception as e:
        print(str(e))
        print("failed to send mail")


