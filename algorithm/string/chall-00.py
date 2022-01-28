S = "This is a string"

bytes = S.encode()

print("Encoded in utf-8, the string is " + str(type(bytes)) + " and the pay load:")
print(bytes)