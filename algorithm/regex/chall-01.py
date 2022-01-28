import re

long_text = "this is quite a challenge when my ip is 2001:0db8:0000:0000:0000:8a2e:0370:7334 or even 5001:0dc8:8eb3:0003:1000:8a2e:0370:abcd!"
reg = "([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})\:([A-Fa-f0-9]{1,4})"

# looping regex exp
i = 0
ips = []
while(True):
    long_text = long_text[i:]
    ip = re.search(reg, long_text)
    if ip is None:
        break
    else:
        ips.append(ip)
        i = ip.span()[1]


if len(ips) == 0:
    print("No ip found in string")
else:
    print("IPs in string are:")
    for ip in ips:
        print("  -" + ip.group())