from itertools import product
import string
N = 3
brute_force_List = []

def getBruteForce():
    global N
    for i in range(1, N+1):
        brute_force_List.append(list(map(''.join, product(string.ascii_lowercase, repeat=i))))

getBruteForce()
for l in brute_force_List:
    print(*l)

