import base64

H = "\x52\x65\x76\x65\x72\x73\x69\x6e\x67\x2e\x49\x44"
print("Converting the string \"" + H + "\"...")
print(base64.b16encode(H.encode()))


H = base64.b16decode(b'526576657273696E672E4944')
print("Decoding the hexpair: " + str(H))