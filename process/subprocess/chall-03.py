from subprocess import run, PIPE
'''
I was at this one for 3 hours trying a variety of things.
The echoer exe works in command prompt and I learned a great deal about
echoer.exe
'''

p = run("echoer.exe",
        stdin=PIPE,
        capture_output=True,
        check=True,
        text=True)
print(p.stderr)