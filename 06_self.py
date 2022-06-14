class Employee:
    company="Google"
#self is instance of a class
    def getSalary(self):#self gets passed automatically when object is called
        print(f"Salary is {self.salary}")

harry=Employee()
harry.salary=100000
#harry.getSalary(),this line gets converted to below line
Employee.getSalary(harry)#hence we need self in method getSalary() because we passed an argument