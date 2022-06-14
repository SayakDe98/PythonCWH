#Printing multiplication table in reverse order:
num = int(input("Enter any number:"))

i=10
while(i>=1):
    print(f"{num}X{i}={i*num}")
    i-=1