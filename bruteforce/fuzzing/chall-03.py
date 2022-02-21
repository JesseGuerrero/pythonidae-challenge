import random, string
def getRandomAlphabet():
    return random.choice(string.ascii_letters + string.digits
                         + string.whitespace + string.punctuation)
def randomUnicode():
    rand = random.randint(0, 10000)
    return chr(rand)

def removeSyntax(stringArg : str):
    return stringArg.replace("(", "").replace(")", "")\
        .replace("\f", "").replace("[", "").replace("]", "")

S = """
(Simple times are good rest but)\f hardship brings character
and wisdom. [We need times of trial to shape us.]
"""

editPermission = 0 #0 is immutable, 1 is alphabet, 2 is complete mutation
for i in range(0, len(S)):
    if S[i] == ")":
        editPermission = 1
    if editPermission == 0:
        continue
    if editPermission == 1:
        if S[i] == "]":
            editPermission = 0
    if S[i] == "(":
        editPermission = 0
    if S[i] == "[":
        editPermission = 1
    if S[i] == "\f":
        editPermission = 2
    O = random.randint(1, 10)
    if i % O == 0:
        if editPermission == 0:
            continue
        if editPermission == 1:
            S = S[:i] + getRandomAlphabet() + S[(i+1):]
        if editPermission == 2:
            S = S[:i] + randomUnicode() + S[(i + 1):]
S = removeSyntax(S)

print(S)