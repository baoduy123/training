# File I/O
**Python cũng hỗ trợ việc đọc và ghi dữ liệu tới các file giống như các ngôn ngữ lập trình khác.**

####Mở file
**Trước khi làm việc với bất cứ File nào, bạn phải mở File đó. Để mở một File, Python cung cấp hàm open().** `doi_tuong_file = open(ten_file [, access_mode][, buffer])`
Trong do:
 * ten_file là tên File bạn muốn truy cập.
 * access_mode xác định chế độ của File đã được mở. Có nhiều mode sẽ được trình bày trong phần dưới. Bạn nên xác định mode này phụ thuộc vào các hoạt động mà bạn muốn thực hiện trên File đó. Chế độ truy cập mặc định là read.
 * buffer Nếu buffer được thiết lập là 0, nghĩa là sẽ không có trình đệm nào diễn ra. Nếu xác định là 1, thì trình đệm dòng được thực hiện trong khi truy cập một File. Nếu là số nguyên lớn hơn 1, thì hoạt động đệm được thực hiện với kích cỡ bộ đệm đã cho. Nếu là số âm, thì kích cỡ bộ đệm sẽ là mặc định (hành vi mặc định)
####Đóng một File  
**Khi bạn đã thực hiện xong các hoạt động trên File thì cuối cùng bạn cần đóng File đó.v Sử dụng phương thức close() để đóng một file có cú pháp như sau:** `fileObject.close()`
####Ghi tới một File
**Phương thức write() được sử dụng để ghi bất kỳ chuỗi nào tới một File đã mở. Phương thức write này không thêm một ký tự newline (dòng mới) ('\n') vào cuối chuỗi. Cú pháp của write() là:** `doi_tuong_file.write(string)`
####Đọc một File
**Để đọc một File, bạn sử dụng phương thức read() trong Python. Cú pháp là:**`doi_tuong_file.read(giatri)`
*Ở đây, giatri là số byte để được đọc từ file đã mở. Phương thức này bắt đầu đọc từ phần đầu file và nếu bạn không cung cấp tham số giatri thì phương thức này cố gắng đọc nhiều dữ liệu nhất có thể, có thể tới cuối File.*

####Các thuộc tính của File trong Python
 * file.closed:	Trả về true nếu file đã được đóng, nếu không là false
 * file.mode: Trả về chế độ truy cập nào mà file đã mở với
 * file.name: Trả về tên file
 * file.softspace: Trả về false nếu space được yêu cầu tường minh với print, nếu không là true

####Thay tên file trong Python
**Phương thức rename() trong os Module được sử dụng để thay tên file. Phương thức này nhận hai tham số là tên file cũ và tên file mới.** `os.rename(ten_file_hien_tai, ten_file_moi)`
####Xóa file trong Python
**Sử dụng phương thức remove() của os Module để xóa các file với tham số là tên file bạn cần xóa.** `os.remove(ten_file)`

```
Code Example:
    import os
    #Open a file
    fo=open('text.txt','w')

    # The file Object Attributes
    print('\nThe file Object Attributes:')
    print(f"Name of the file:{fo.name}")
    print(f"Closed or not:{fo.closed}")
    print(f"Opening mode:{fo.mode}")

    #Write a file
    fo.write("Nguyen Duc Huy - TMA")

    #Close a file
    fo.close()

    #Read a file
    fo=open('text.txt','r') 
    t_5=fo.read(6)
    #Reposition pointer at the beginning of the file because the current pointer's position is 6
    fo.seek(0,0)
    print(f'\nRead 6 first character of file: {t_5}')
    t_full=fo.read()
    print(f'\nContent of file: {t_full}')
    fo.close()

    #Renaming a file 
    os.rename('text.txt','final_text.txt')
    print("\nChanged name of file from text.txt to final_text.txt")

    #Remove a file
    os.remove('final_text.txt')
    print("\nfile final_text.txt has been removed")

Result:
    The file Object Attributes:
    Name of the file:text.txt
    Closed or not:False
    Opening mode:w

    Read 6 first character of file: Nguyen

    Content of file: Nguyen Duc Huy - TMA

    Changed name of file from text.txt to final_text.txt

    file final_text.txt has been removed
```
