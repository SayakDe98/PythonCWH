import os
oldname="sample2.txt"
newname="renamed_by_python.txt"
with open(oldname) as f:
    content=f.read()

with open(newname,"w") as f:
    f.write(content)#renamed_by_python.txt is created

os.remove(oldname)#sample2.txt is deleted