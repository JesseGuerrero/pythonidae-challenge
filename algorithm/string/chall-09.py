from itertools import permutations
N = "ABC"

for p in permutations(N):
    print(''.join(p))