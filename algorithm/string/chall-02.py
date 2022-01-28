D = "MII CyberSec Consulting Service"
S = 4
E = 11

print("String:")
newString = D[:4] + "x"*(11+1-4) + D[11+1:]
print(newString)
print(D)

print("Byte:")
B = D.encode()
newByte = B.replace(B[4:11+1], ("x"*(11+1-4)).encode())
print(newByte)