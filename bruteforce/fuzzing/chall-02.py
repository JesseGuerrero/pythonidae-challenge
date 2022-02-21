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

R = random.randint(1, 100)
R = (R / 100.0)*len(S) #Convert ratio to number of characters.

changedChars = 0
while(changedChars < R):
    for i in range(0, len(S)):
        O = random.randint(1, 10)
        if i % O == 0:
            S = S[:i] + randomUnicode() + S[(i + 1):]
            changedChars += 1
            if(changedChars > R): #Check characters...
                break


print(S)
print("Desired ratio: " + str(R) + "/" + str(len(S)))
print("Ratio: " + str(changedChars) + "/" + str(len(S)) + " changed chars...")
