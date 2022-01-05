# Moudels vs Packages
**Module và package là những cấp độ quản lý code cao hơn trong Python. Module cho phép lưu trữ hàm (và code khác) trên các file riêng rẽ để sau tái sử dụng trong các file và dự án khác. Package cho phép nhóm các module lại với nhau.**
###Moudle
**Trong python bất kì file script (file có đuôi py) đều được gọi là một module. Khi tạo một file python mới thì mình đang tạo 1 module. Mỗi module đều có thể được tải và thực thi bởi python interpreter.**
**Để sử dụng hàm,biến được định nghĩa trong module trong python sử dụng import. Có hai kiểu viết lệnh import khác nhau:**
```
import <module1>, <module2>, <module3>, ...
from <module> import <ten1>, <ten2>, ...
```
**Ngoài ra bạn có thể dùng alias  để import như sau:`import my_module as mod`**
```
Code example:
modules.py
# Ham kiem tra mot so co trong list khong
def checkElement(num, arr):
    if num in arr:
        return True
    else:
        return False

# Ham tinh tong tat ca cac phan tu trong list 
def calSumList(arr):
    s = 0
    for i in arr:
        s += i
    return s
---------------------------------------------------- 
import modules as mod
arr = [1, 6, 3, 2, 8, 9]
num = 4
def main():
    # Goi qua modules
    print('Goi thong qua modules')
    print(f"{num} in {arr}") if mod.checkElement(
        num, arr) else print(f"{num} not in {arr}")

    print(f"Sum of arr:{arr}= {mod.calSumList(arr)}")
if __name__ == '__main__':
    main()

Result:
Goi thong qua modules
4 not in [1, 6, 3, 2, 8, 9]
Sum of arr:[1, 6, 3, 2, 8, 9]= 29
```

###Package
**Trong python một số module trong cùng thư mục có thể kết hợp lại để tạo ra một package. Package giúp đơn giản hóa hơn nữa việc sử dụng nhiều module có liên quan với nhau.**

**Đặc trưng của package là có thêm file `__init__.py` có nghãi đặc thù trong python. Nếu python nhìn thấy thư mục nào có file với tên gọi `__init__.py` nó sẽ tự động coi thư mục này như một package, chứ không còn là thư mục bình thường nữa.**

**Nếu sử dụng lệnh `import <tên_package>` bạn có thể truy cập các hàm của từng module qua cú pháp `<tên_package>.<tên_module>.<tên_hàm>()`**

```
Code example:
---------------------------------
module1.py
# Ham kiem tra mot so co trong list khong
def checkElement(num, arr):
    if num in arr:
        return True
    else:
        return False
---------------------------------
module2.py
# Ham tinh tong tat ca cac phan tu trong list 
def calSumList(arr):
    s = 0
    for i in arr:
        s += i
    return s
---------------------------------
__init__.py
from my_packages.module1 import *
from my_packages.module2 import *
---------------------------------
import my_packages as mp
arr = [1, 6, 3, 2, 8, 9]
num = 4
def main():

    print('\nGoi thong qua packages')

    print(f"{num} in {arr}") if mp.module1.checkElement(
        num, arr) else print(f"{num} not in {arr}")

    print(f"Sum of arr:{arr}= {mp.module2.calSumList(arr)}")

if __name__ == '__main__':
    main()

Result:
Goi thong qua packages
4 not in [1, 6, 3, 2, 8, 9]
Sum of arr:[1, 6, 3, 2, 8, 9]= 29
```