#Task 1
import re

def extract_emails(file):
    with open(file, 'r') as file:
        print('Emails: ')
        for line in file:
            emails = re.findall(r"[A-za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", line)
            for email in emails:
                print(f'- {email}')

email_input = input("Enter file/path to be checked: ")

extract_emails(email_input)