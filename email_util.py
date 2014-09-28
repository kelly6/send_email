#!/usr/bin/python
#encoding=utf8
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header
import zipfile

from_addr = "123456@qq.com"
pass_word = "password"

def send_mail(to_addrs, title, content):
    smtphd = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    #smtphd.connect("smtp.exmail.qq.com", 465)
    smtphd.login(from_addr, pass_word)
 
    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = ";".join(to_addrs)
    msg['Subject'] = Header(title, 'utf8')
    msg['Reply-To'] = from_addr
    
    msg.attach(MIMEText(content, 'plain', 'utf8'))

    smtphd.sendmail(from_addr, to_addrs, msg.as_string())
    smtphd.quit()

if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description='Short sample app')

    parser.add_argument('--to_addrs', action="store", nargs="*", dest="to_addrs", default=[])
    parser.add_argument('--title', action="store", dest="title", default="")
    parser.add_argument('--content', action="store", dest="content", default="")
    
    p = parser.parse_args(sys.argv[1:])
    print p

    send_mail(p.to_addrs, p.title, p.content)
