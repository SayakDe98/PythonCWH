#Use open function to read the content of a file!
f = open("sample.txt","r")#if mode isn't specified it will be r by default
data=f.read()
print(data)
f.close()

print("Now if we read first 5 character from file:")
f=open("sample.txt")
data=f.read(5)#reads first 5 characters
print(data)
f.close()
