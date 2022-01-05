#Class and OOP

###OOP
**Lập trình hướng đối tượng (OOP) là một kỹ thuật hỗ trợ, cho phép lập trình viên trực tiếp làm việc với các đối tượng mà họ định nghĩa lên.**


**Lớp (Class): có thể được định nghĩa như là một template mô tả trạng thái và hành vi mà loại đối tượng của lớp hỗ trợ. Một đối tượng là một thực thể (instance) của một lớp**

**Đối tượng (Object): có trạng thái và hành vi. Trong đối tượng sẽ bao gồm những thuộc tính phương thức đặc trưng của đối tượng đó**
```
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def move(self):
        print(f'self.name is moving')
#instance the People class
huy=People("Huy",22)
```
####Kế thừa (Inheritance)
**Tính kế thừa cho phép một lớp (class) có thể kế thừa các thuộc tính và phương thức từ các lớp khác đã được định nghĩa. Lớp đã có gọi là lớp cha, lớp mới phát sinh gọi là lớp con. Lớp con kế thừa tất cả thành phần của lớp cha, có thể mở rộng các thành phần kế thừa và bổ sung thêm các thành phần mới.**

####Đóng gói (Encapsulation)
**Chúng ta có thể hạn chế quyền truy cập vào trạng thái bên trong của đối tượng. Điều này ngăn chặn dữ liệu bị sửa đổi trực tiếp, được gọi là đóng gói. Trong Python, chúng ta biểu thị thuộc tính private này bằng cách sử dụng dấu gạch dưới làm tiền tố: “_” hoặc “__“**
####Đa hình (Polymorphism)
**Tính đa hình là khái niệm mà hai hoặc nhiều lớp có những phương thức giống nhau nhưng có thể thực thi theo những cách thức khác nhau.**
```
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

---------------------main.py--------------------
from people import *
p=People("Huy",22)
em=Employee("Nam",30,"039678901")
print(f"{em}. My phonenumber: {em.phone}")
```

