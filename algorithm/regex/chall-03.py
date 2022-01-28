import re

long_text = "this is john@gmail.com but not joe@minecraft.com"
reg = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"

# looping regex exp
i = 0
emails = []
while(True):
    long_text = long_text[i:]
    email = re.search(reg, long_text)
    if email is None:
        break
    else:
        emails.append(email)
        i = email.span()[1]


if len(emails) == 0:
    print("No email found in string")
else:
    print("Emails in string are:")
    for email in emails:
        print("  -" + email.group())