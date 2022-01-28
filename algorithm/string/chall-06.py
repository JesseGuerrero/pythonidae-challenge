'''
This one took a lot a lot of time!
'''

'''
\\x is an escape character for defining a hexadecimal pair.
The reason it comes in pairs is because a byte signifies 8 bits. Each
hex digit represents 4 bits. Each of these is a hex pair below.
'''
S = b'\x52\x65\x76\x65\x72\x73\x69\x6e\x67\x2e\x49\x44'
C = 0x53
listStr = []
for e in S:
    listStr.append(hex(e^C))#We xor as an int but reconvert into hex bytes.
    #hex keyword auto converts ints to hex oriented bytes.
print(listStr) #here we have our x pairs