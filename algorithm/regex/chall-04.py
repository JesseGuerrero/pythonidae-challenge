import re

long_text = "here are all my ssn numbers: 123787894 or 321 12 1234 or 123-12-1234"
reg = "(\d{3} \d{2} \d{4})|(\d{3}-\d{2}-\d{4})|(\d{9})"

# looping regex exp
i = 0
ssns = []
while(True):
    long_text = long_text[i:]
    ssn = re.search(reg, long_text)
    if ssn is None:
        break
    else:
        ssns.append(ssn)
        i = ssn.span()[1]


if len(ssns) == 0:
    print("No SSN found in string")
else:
    print("SSNs in string are:")
    for ssn in ssns:
        print("  -" + ssn.group())