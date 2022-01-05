# Global and Local Variables
**Local variables là những biến được khởi tạo bên trong một hàm và chỉ thuộc về hàm cụ thể đó. Nó không thể được truy cập ở bất kỳ đâu bên ngoài chức năng.**
```
Code example:
def printSomething():
    s="Duc Huy"
    print(s)
printSomething()

Result:
Duc Huy
```
**Global Variables là những biến được định nghĩa bên ngoài bất kỳ hàm nào và có thể truy cập được trong suốt chương trình, tức là bên trong và bên ngoài mọi hàm.**
```
Code example:
s="Nguyen Duc Huy"
def printSomething():
    print(s)
printSomething()

Result:
Nguyen Duc Huy
```

**Chúng ta chỉ sử dụng từ khóa global trong hàm nếu chúng ta muốn thực hiện các phép gán hoặc thay đổi biến toàn cục.**

```
Code example:
s="Nguyen "
def printSomething():
    global s
    s+="Duc Huy"
    print(s)
printSomething()
print(s)

Result:
Nguyen Duc Huy
Nguyen Duc Huy
```