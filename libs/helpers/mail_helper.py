import email
import imaplib
import re
import os
from utilities.readProperties import ReadConfig
from bs4 import BeautifulSoup
import urllib.request

detach_dir = 'locationWhereYouWantToSaveYourAttachments'

def get_cloudflare_code():
    SMTP_SERVER = ReadConfig.getSmtpServer()
    FROM_EMAIL = ReadConfig.getFromEmail()
    FROM_PWD = ReadConfig.getFromPwd()
    print(SMTP_SERVER, ":", FROM_EMAIL,":", FROM_PWD)
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')

    data = mail.search(None, 'ALL')
    mail_ids = data[1]
    id_list = mail_ids[0].split()

    last_email_id = int(id_list[-1])
    data = mail.fetch(str(last_email_id), '(RFC822)')
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            msg = email.message_from_string(str(arr[1], 'utf-8'))
            # email_subject = msg['subject']
            # email_from = msg['from']
            # print('From : ' + email_from + '\n')
            # print('Subject : ' + email_subject + '\n')
            for payload in msg.get_payload():
                result = payload.get_payload()
                code= result.split("login screen:")[1].split("This code")[0].strip()
                print("CODECODE:", code)
                return code

def get_inbox():
    mail = imaplib.IMAP4_SSL(ReadConfig.getSmtpServer())
    mail.login(ReadConfig.getFromEmail(), ReadConfig.getFromPwd())
    mail.select('inbox')

    _, searched_data = mail.search(None, 'UNSEEN')

    for searched in searched_data[0].split():
        data_to_return = {}
        _, mail_data = mail.fetch(searched, "(RFC822)")
        _, data = mail_data[0]
        message = email.message_from_bytes(data)

        headers = ["From", "To", "Date", "Subject" ]
        for header in headers:
            data_to_return[header] = message[header]

        for msg_part in message.walk():
            if msg_part.get_content_type() == "text/plain":
                data_to_return["Body"] = msg_part.get_payload(decode=False)
        # print("data:-->",msg_part.get_payload(decode=False))
        f = open("htmlgetformmail.html", "a")
        f.write(msg_part.get_payload(decode=False))
        f.close()
        soup = BeautifulSoup(msg_part.get_payload(decode=False), "html.parser")
        for link in soup.findAll('a'):
            a = link['href']
            print("data hr:-->",a)
            return a

    return "null"
                             

def get_one_time_password():
    mail = imaplib.IMAP4_SSL(ReadConfig.getSmtpServer())
    mail.login(ReadConfig.getFromEmail(), ReadConfig.getFromPwd())
    mail.select('inbox')

    data = mail.search(None, 'ALL')
    mail_ids = data[1]
    id_list = mail_ids[0].split()

    last_email_id = int(id_list[-1])
    data = mail.fetch(str(last_email_id), '(RFC822)')
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            msg = email.message_from_string(str(arr[1], 'utf-8'))
            return int(msg.get_payload().split(";\"")[2][1:7])  # ugly
