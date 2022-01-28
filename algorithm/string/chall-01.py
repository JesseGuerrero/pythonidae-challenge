U = "https://pythonidae.herokuapp.com/"
E = ["web/generate", "web/identify", "web/cookies"]

answers = []
for sub in E:
    answers.append(U+sub)

for answer in answers:
    print(answer)