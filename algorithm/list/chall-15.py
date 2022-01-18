N = 15
K = 4
L = []

for i in range(1, N):
    if i % K == 0:
        continue
    L.append(i)

print(L)