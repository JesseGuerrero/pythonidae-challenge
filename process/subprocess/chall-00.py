from subprocess import PIPE, run

command = ['resources/runme.exe', 'MII Cybersec']
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
print(result.stdout, result.stderr)