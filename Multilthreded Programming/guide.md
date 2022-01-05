#Multithreaded Programming

**Thread là một đơn vị cơ bản trong CPU. Một luồng sẽ chia sẻ với các luồng khác trong cùng process về thông tin data, các dữ liệu của mình. Việc tạo ra thread giúp cho các chương trình có thể chạy được nhiều công việc cùng một lúc**

**Process là quá trình hoạt động của một ứng dụng. Tiến trình (process)chứa đựng thông tin tài nguyên, trạng thái thực hiện của chương trình**

**Luồng (thread) là một khối các câu lệnh độc lập trong một tiến trình(process) và có thể được lập lịch bởi hệ điều hành. Hay nói một cách đơn giản, Thread là các hàm hay thủ tục chạy độc lập đối với chương trình chính. Một process dĩ nhiên có thể chứa nhiều thread bên trong nó.**

![img](https://images.viblo.asia/full/a57a2073-a363-4742-ae44-e9bdfeca8149.png)

**Một chương trình đa luồng chứa hai hoặc nhiều phần mà có thể chạy đồng thời và mỗi phần có thể xử lý tác vụ khác nhau tại cùng một thời điểm.Python cung cấp thread Module và threading Module để bạn có thể bắt đầu một thread mới cũng như một số tác vụ khác trong khi lập trình đa luồng. Mỗi một Thread đều có vòng đời chung là bắt đầu, chạy và kết thúc. Một Thread có thể bị ngắt (interrupt), hoặc tạm thời bị dừng (sleeping) trong khi các Thread khác đang chạy – được gọi là yielding.**

```
import time
import numpy as np
from threading import Thread
import threading

def cal_sum(arr):
    print("Calculating sum")
    time.sleep(0.5)
    s=0
    for i in arr:
        s+=i

def cal_multiplication(arr):
    print("Calculating multiplication")
    time.sleep(0.5)
    t=1
    for i in arr:
        t*=i
        
print("\nRun without Thread")
arr = np.arange(1,10)
t = time.time()
cal_multiplication(arr)
cal_sum(arr)
print ("done in ", time.time()- t)

print("\nRun with Thread")
try:
	t = time.time()
	t1 = threading.Thread(target=cal_multiplication, args=(arr,))
	t2 = threading.Thread(target=cal_sum, args=(arr,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("done in ", time.time()- t)
except:
	print ("error")

Result:
Run without Thread
Calculating multiplication
Calculating sum
done in  1.0028223991394043

Run with Thread
Calculating multiplication
Calculating sum
done in  0.5158565044403076
```
**=> Có thể chương trình chạy có sử dụng thread thì thời gian chạy nó ít hơn  so với chương trình không dùng thread do các luồng chạy đồng thời song song với nhau, không cần chạy lần lượt tuần tự. Nếu chạy process thì tài nguyên có thể khác nhau, cấu trúc khác nhau, kết quả khác nhau và hoạt động tuần tự, còn đa luồng thi các thread có thể cấu trúc giống nhau, tài nguyên dùng ít hơn.**

**Ngoài ra module Threading còn bổ sung thêm một số phương thức khác, đó là:**
  * run(): Là entry point cho một Thread.
  * start(): Bắt đầu một thread bởi gọi phương thức run().
  * join([time]): Đợi cho các thread kết thúc.
  * isAlive(): Kiểm tra xem một thread có đang thực thi hay không.
  * getName(): Trả về tên của một thread.
  * setName(): Thiết lập tên của một thread.
  * threading.activeCount(): Trả về số đối tượng thread mà là active.
  * threading.currentThread(): Trả về số đối tượng thread trong Thread control của Caller.
  * threading.enumerate(): Trả về một danh sách tất cả đối tượng thread mà hiện tại là active.
