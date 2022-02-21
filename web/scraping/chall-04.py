import requests
import re

URL = "https://www.tamusa.edu/information-technology-services/its-staff.html"

web_source = requests.get(URL).text
reg = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"

# looping regex exp
i = 0
emails = []
while(True):
    web_source = web_source[i:]
    email = re.search(reg, web_source)
    if email is None:
        break
    else:
        emails.append(email)
        i = email.span()[1]


if len(emails) == 0:
    print("No email found in string")
else:
    print("Emails in string are:")
    for email in set(emails):
        print("  -" + email.group())