import re

def decipher(cipher_text):
    cipher = []
    reg = ":(.*)"
    field = re.search(reg, cipher_text)
    if field is None:
        pass
    else:
        cipher.append(field.group()[1:].split("$")[0:3])
    if len(cipher) == 0:
        print("No tags found in string")
    else:
        print("Cipher fields in string are:")
        for field in cipher:
            print(field)

shadow_file1 = """
hello:key$zer$sozemy life is good $or is it?
"""
shadow_file2 = """
Dude! is there life on mars? I have no idea: although I can bet you $50 there is. What do you say? I will even go for $25 dude. Come on man. Otherwise we can just fo $5, just for fun??
"""

decipher(shadow_file1)
decipher(shadow_file2)


