from threading import Thread
import random, time

N = 30
queue = [i for i in range(0, N)]
random.shuffle(queue)
locked = False

def popElement(i):
    global queue, locked
    time.sleep(random.randint(3, 13))
    if(locked):
        popElement(i)
        return
    else:

        if len(queue) == 0:
            return
        else:
            locked = True
            print("P" + str(i) + " pops: " + str(queue.pop()))
            locked = False
            popElement(i)

for i in range(0, 5):
    Thread(target=popElement, args=(i+1, )).start()