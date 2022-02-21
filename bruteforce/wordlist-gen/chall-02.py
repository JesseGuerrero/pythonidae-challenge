from itertools import product
import string
S = 1
E = 3
brute_force_List = []

def getBruteForce():
    global N
    for i in range(S, E+1):
        brute_force_List.append(list(map(''.join, product(string.ascii_lowercase, repeat=i))))

getBruteForce()

with open("chall-02.txt", 'w+') as file:
    for l in brute_force_List:
        file.write(" ".join(l))
        file.write("\n")

