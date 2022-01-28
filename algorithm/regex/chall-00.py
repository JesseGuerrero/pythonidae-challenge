import re

long_text = "this is 0.0.0.0 and 255.255.255.255 or even 192.34.12.8"
reg = "((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"

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