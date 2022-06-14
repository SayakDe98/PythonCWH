f=open("sample.txt")
data=f.readline()#reads a single line,here reads first line
print(data,end="")
data=f.readline()#reads second line
print(data)
f.close()
