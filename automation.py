import re

with open('assets/potenial-contacts.txt', 'r') as f:
    text = f.read().replace('\n', '')  # clean text file

regex_phone = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''',
                         re.VERBOSE)
# extract phone numbers
phone = []
for i in regex_phone.findall(text):
    phone_number = '-'.join([i[1], i[3], i[5]])
    phone_number = re.sub(r'[(|)]', '', phone_number)
    phone.append(phone_number)
phone.sort()
with open("./phone_list.txt", "w+") as f:
    for numbers in phone:
        f.write(numbers + "\n")
# extract emails
regex_email = re.compile(r'''([a-zA-Z\d._%+-]+ @[a-zA-Z\d.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)
email = []
for i in regex_email.findall(text):
    email.append(i[0])
email.sort()
with open("./email_list.txt", "w+") as f:
    for emails in email:
        f.write(emails + "\n")
