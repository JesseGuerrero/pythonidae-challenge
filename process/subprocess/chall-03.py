import subprocess
process = subprocess.Popen("C:\WINDOWS\system32\cmd.exe",
       stdin=subprocess.PIPE,
       stdout=subprocess.PIPE,
       stderr=subprocess.PIPE)
process.stdin.write("dir")
process.stdin.flush()
print(process.stdout.readline())
