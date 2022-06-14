with open('another.txt','w') as f:
    a=f.write("me")
with open('another.txt','r') as f:
    a=f.read()
print(a)
#if we use with statement then we don't need to close the file