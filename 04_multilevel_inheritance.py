class Person:
    
    country="India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print("No salary to programmers")
    
    def takeBreath(self):
        print("I am an Programmer so I am breathing++...")

p=Person()
p.takeBreath()

e=Employee()
e.takeBreath()

pr=Programmer()
pr.takeBreath()
print(pr.country)#gets property from Person which is grandparent of this class