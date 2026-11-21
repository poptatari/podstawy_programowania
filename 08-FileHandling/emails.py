import re


def email_sender(email_text):
    return re.findall(r'From:.*<(.+)>', email_text)[0]


def email_recipient(email_text):
    return re.findall(r'To:.*<(.+)>', email_text)[0]


def email_subject(email_text):
    return re.findall(r'Subject: (.+)', email_text)[0]


def email_body(email_text):
    return re.findall(r'\n\n([\s\S]+)', email_text)[0]