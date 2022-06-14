#WAP to print multiplication table of given number
n = int(input("Enter a number:"))

for i in range(1,11):
    print(n,"X",i,"=",(n*i))

print("Alternate way:")
for i in range(1,11):
    print(str(n),"X",str(i),"=",(n*i))

print("Using f string()")
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
