from subprocess import PIPE, run

p = run(['resources/runme.exe', 'MII Cybersec'])
print("Exit code is", p.returncode)