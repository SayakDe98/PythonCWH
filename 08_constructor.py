class Employee:
    company="Google"
#self is instance of a class
    def __init__(self):
        print("Employee is created!")
    
    def __init__(self,name,salary,submit):
        self.name=name
        self.salary=salary
        self.submit=submit
        print("Employee is created")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The submit of the employee is {self.submit}")

    def getSalary(self,signature):#self gets passed automatically when object is called
        print(f"Salary is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():#if we make it staticmethod then we don't need self
        print("Good morning, Sir")
    
    @staticmethod
    def time():
        print('The time is 9AM in the morning')

harry=Employee("Sayak",100,"Youtube")
#harry=Employee()#Throws an error(missing 3 required positional arguments)
harry.getDetails()