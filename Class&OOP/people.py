class People:
    __salary =0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showInfo(self):
        print(f'Hello, name is {self.name} and my age is {self.age}')
    
    def  __str__(self):
        return f'Hello, name is {self.name} and my age is {self.age}'
    
    def  addSalary(self,value):
        self.__salary+=value

class Employee(People):
    def __init__(self,name,age,phone):
        super().__init__(name,age)
        self.phone = phone
        
    def isEmployee(self):
        return True
    
    
class Manager(People):
    def isEmployee(self):
        return False