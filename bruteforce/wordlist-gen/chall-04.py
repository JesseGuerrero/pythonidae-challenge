WORD = 'password'
substitutes = {
    'a': ['a', 'b', 'A', '@', '4'],
    'd': ['3', 'p', 'd']
}

brute_list = []
WORD = list(WORD)
for key,value in substitutes.items():
    for i in range(0, len(WORD)):
        if WORD[i] == key:
            for v in value:
                buff = WORD.copy()
                buff[i] = v
                brute_list.append("".join(buff))

print(brute_list)