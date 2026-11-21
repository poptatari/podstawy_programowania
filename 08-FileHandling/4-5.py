# Write a program that uses regular expressions to fetch and print:
# - sender email address
# - recipient email address
# - email subject
# - email body
import emails

with open('email.txt', 'r', encoding='utf-8') as file:
    raw_email = file.read()

print("Sender:", emails.email_sender(raw_email))
print("Recipient:", emails.email_recipient(raw_email))
print("Subject:", emails.email_subject(raw_email))
print("\nBody:\n" + emails.email_body(raw_email))