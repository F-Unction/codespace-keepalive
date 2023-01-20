
import os

for line in os.popen('gh cs list').read().splitlines():
    line=line.split("\t")[0]
    print(line+os.popen("gh cs ssh -c "+ line +" \"echo ok && exit\"").read())
