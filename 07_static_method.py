class Employee:
    company="Google"
#self is instance of a class
    def getSalary(self,signature):#self gets passed automatically when object is called
        print(f"Salary is {self.salary}\n{signature}")
    @staticmethod
    def greet():#if we make it staticmethod then we don't need self
        print("Good morning, Sir")
    @staticmethod
    def time():
        print('The time is 9AM in the morning')

harry=Employee()
harry.salary=100000
harry.getSalary("Thanks!")#this line gets converted to below line
#Employee.getSalary(harry)#hence we need self in method getSalary() because we passed an argument
harry.greet()
harry.time()