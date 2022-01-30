from subprocess import run

with open("chall-01.txt", "w+") as log:
    run(['resources/runme.exe', 'MII Cybersec'], stdout=log)
    print("Written to log...")


