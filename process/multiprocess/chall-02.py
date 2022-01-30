from multiprocessing import Pool, current_process

def printChild(name):
    print("I am a child and my name is " + name + " and my pid is: " + str(current_process().pid))
if __name__ == '__main__':
    processes = []
    print("I am the father and I make children...")
    p = Pool(5)
    p.map(printChild, ["Henry", "Nick", "Trent", "John", "Devin"])
