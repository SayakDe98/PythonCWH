#WAP to sum a list with 4 numbers

m1 = int(input("Enter Marks for Student Number 1 "))
m2 = int(input("Enter Marks for Student Number 2 "))
m3 = int(input("Enter Marks for Student Number 3 "))
m4 = int(input("Enter Marks for Student Number 4 "))


l = [m1 , m2, m3, m4]
print(l[0]+l[1]+l[2]+l[3])
print(sum(l))