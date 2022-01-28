S = "Hello sherlock https://www.google.com/ holmes"

def getURLFromStartIndex(start):
    global S
    end = start
    for ch in S[start:]:
        if ch.isspace():
            break
        else:
            end+=1
    return S[start:end]

print(getURLFromStartIndex(S.find("http://")))
print(getURLFromStartIndex(S.find("https://")))