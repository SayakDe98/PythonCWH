class Employee:
    company="Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    
    language="Python"
    #company='Youtube'

    def getLang(self):
        print(f"The language is {self.language}")

e=Employee()
e.showDetails()

p=Programmer()
p.showDetails()
p.getLang()
print(p.company)