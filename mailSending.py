#!/usr/bin/python3
from ssl import create_default_context
from smtplib import SMTP

def send_Email(your_mail,your_passwd,to_,msg):
    try:
        context = create_default_context()  
        server = SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(your_mail,your_passwd)
        server.sendmail(your_mail,to_,msg)

    except Exception as e:
        print("Error: ",e)