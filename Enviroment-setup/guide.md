#  Virtual Environments
**Virtual Environment dịch nôm na là môi trường ảo, cho phép bạn nghịch ngợm lung tung với các packages của Python mà không làm ảnh hưởng đến những packages đã được cài đặt sẵn trên Python. Ví dụ bạn muốn thử nghiệm với Django 1.8 trong khi trên hệ thống đang cài đặt Django 1.4.**

### Các bước để sụng Virtual Enviroment
 * Cai dat virtualenv bang lenh `pip install virtualenv`
 * Tao Virtual Environment bang lenh `virtualenv [projectname]` eg: `virtualenv project_of_huy`.
    * Nếu trên server có nhiều phiên bản Python (2.x, 3.x) bạn hoàn toàn có thể khởi tạo Virtual Environment với một phiên bản chỉ định: `virtualenv -p /usr/bin/python2.7 [project_name]`
    * Hoặc bạn có thể tạo một Virtual Environment mà không có các packages đã được cài đặt sẵn (trong trường hợp bạn muốn làm mọi thứ từ đầu: `source [project_name]/bin/activate`
 * Khởi động Virtual Environment bằng câu lệnh: `source [project_name]/bin/activate` eg `source project_of_huy/bin/activate`
 * Thoát khỏi Virtual Environment: `deactivate`

# System interpreter
Chi tiet tai: https://www.youtube.com/watch?v=GqTsFOtZiQI
