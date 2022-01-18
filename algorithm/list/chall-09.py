import random
S = 3
E = 10

uniques = []
i = S
while i <= E:
    newInt = random.randint(S, E)
    if newInt in uniques:
        continue
    uniques.append(newInt)
    i+=1

print(uniques)