from threading import Thread
import random, time


S = "My lords..."
locked = False

def changeS(change):
    global S, locked
    time.sleep(random.randint(2, 8))
    if(locked):
        changeS(change)
        return
    else:
        locked = True
        S = change
        print(S)
        locked = False

print(S)
for change in ["Henry", "Nick", "Trent", "John", "Devin"]:
    Thread(target=changeS, args=(change,)).start()