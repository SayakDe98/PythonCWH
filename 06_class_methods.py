class Employee:
    company="Camel"
    salary=100
    location="Delhi"

    def changeSalary(self,sal):
        self.salary=sal
    
    
    # def changeSalary(self,sal):#__class__ means dunder class
    #     self.__class__.salary=sal#thisis used to change the value

    # @classmethod #decorator used called classmethod,it is connected to class to change class attributes
    # def changeSalary(cls,sal):#this is another way of changing value
    #     cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)