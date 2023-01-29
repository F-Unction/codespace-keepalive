
import subprocess

for line in subprocess.getoutput('gh cs list').splitlines():
    line=line.split("\t")[0]
    print(line + subprocess.getoutput('gh cs ssh -c '+ line +' \"echo ok && exit\"'))
    subprocess.run('gh codespace stop -c ' + line)
    
