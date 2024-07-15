"""
https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4
"""

import os
import smtplib
import logging


phone_number = os.environ['PHONE_NUMBER']
email = os.environ['GMAIL_EMAIL']
password = os.environ['GMAIL_PASSWORD']

smtp_host = 'smtp.gmail.com'
smtp_port = 587

recipient = phone_number + "@vtext.com"

def send(message: str):
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(email, password)

    server.sendmail(email, recipient, message)
    logging.info("Sent message.")
    server.close()
