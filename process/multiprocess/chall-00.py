from multiprocessing import Process

'''
Process class runs the entire script except the part under
the if '__main__' part. By adding this flag we allow distinction
between main process and everything else. 

From this runned script Process grabs the target and runs it!
'''

def printChild():
    print("The Child of Pythonidae")
if __name__ == '__main__':
    print("The Maker of Life")
    Process(target=printChild).start()