class Employee:
    company="Google"
    salary=100

harry=Employee()
rajni=Employee()

# Creating instance attribute salary for both the objects
# harry.salary=300
# rajni.salary=400

print(harry.company)
print(rajni.company)

Employee.company="Youtube"

print(harry.company)
print(rajni.company)

print(harry.salary)#there is no instance attribute so it prints class attribute
print(rajni.salary)#there is no instance attribute so it prints class attribute

harry.salary=45

print(harry.salary)#prints 45 since we have instance attribute
print(rajni.salary)

print(rajni.address)#below line throws error as we don't have instance/class attributes