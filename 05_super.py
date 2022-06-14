class Person:
    country="India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"
    
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()#runs the takeBreath() of its super class that is of Person class
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company="Fiverr"
    def __init__(self):
        #super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print("No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()#runs the takeBreath() of its superclass where we see there is another super keyword so first takeBreath() of Person runs then of Employee then of Programmer
        print("I am an Programmer so I am breathing++...")

# p=Person()
# p.takeBreath()

# e=Employee()
# e.takeBreath()

pr=Programmer()
#pr.takeBreath()