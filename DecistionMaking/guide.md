# Decision making
**Decision making là đưa ra các điều kiện có thể xảy ra trong khi thực hiện chương trình và cụ thể hóa các hành động được thực hiện theo các điều kiện. Bạn cần xác định hành động nào cần thực hiện và câu lệnh nào sẽ thực hiện nếu kết quả là True hoặc False nếu ngược lại.**

**Ngôn ngữ lập trình Python giả định bất kỳ giá trị nào khác không và không rỗng là TRUE và nếu nó là 0 hoặc null, thì nó được giả định là giá trị FALSE**

![img](https://www.tutorialspoint.com/python/images/decision_making.jpg)

###Code example:
```
import numpy as np
a = np.random.randint(0, 10)
if a > 5:
    print(f"{a}>5")
elif a == 5:
    print(f"{a}=5")
else:
    print(f"{a}<5")
```