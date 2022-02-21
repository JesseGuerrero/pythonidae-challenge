import random
S = """
Python is a super popular high level language in the current times, 
2019. Universities teach the language, programming gurus preach it, 
meaning there are plenty of ways to learn it. Its popularity makes 
most Python code Googlable and many companies use it for various 
fields like data analytics, machine learning and miscellaneous app 
development.
"""

#Reference: https://www.reddit.com/r/learnpython/comments/8e51gp/need_help_generating_random_unicode_character/
def randomUnicode():
    rand = random.randint(0, 10000)
    return chr(rand)

changedChars = 0
for i in range(0, len(S)):
    O = random.randint(1, 10)
    N = random.randint(1, O)
    if i % O == 0:
        for k in range(i, i+N):
            S = S[:k] + randomUnicode() + S[(k+1):]
            changedChars+=1

print(S)
print("Ratio: " + str(changedChars) + "/" + str(len(S)) + " changed chars...")
