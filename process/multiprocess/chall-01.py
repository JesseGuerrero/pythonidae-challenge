from multiprocessing import Process

def printChild():
    pass
if __name__ == '__main__':
    processes = []
    print("The Maker of Life")
    for i in range(0, 5):
        p = Process(target=printChild)
        p.start()
        processes.append(p)
    for p in processes:
        print("pid: " + str(p.pid))