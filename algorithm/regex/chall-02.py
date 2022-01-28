import re

long_text = "this www.ironman.org is cool and so is runescape.com"
reg = "(?:www.)?(\w+.(com|org|net|id))"

# looping regex exp
i = 0
dnss = []
while(True):
    long_text = long_text[i:]
    dns = re.search(reg, long_text)
    if dns is None:
        break
    else:
        dnss.append(dns)
        i = dns.span()[1]


if len(dnss) == 0:
    print("No DNS found in string")
else:
    print("DNSs in string are:")
    for dns in dnss:
        print("  -" + dns.group())