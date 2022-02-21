N = 2
L = ['a', 'b', 'c']

from itertools import product
brute_force_List = list(map(''.join, product(L, repeat=N)))
print(brute_force_List)