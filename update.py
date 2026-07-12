with open("text.txt","a")as f:
    f.write("Hello World!")

import subprocess
import datetime

subprocess.run(["git","add","."])
cdt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

commit = subprocess.run(["git","commit","-m",f"{cdt}"])
push = subprocess.run(["git","push"])
print("Successfull 1")