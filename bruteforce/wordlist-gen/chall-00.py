from itertools import product
import string
N = 3
brute_force_List = []

brute_force_List = list(map(''.join, product(string.ascii_lowercase, repeat=N)))

print(brute_force_List)

