# Exceptions
**Exception là một sự kiện, xảy ra trong quá trình thực thi chương trình làm gián đoạn luồng hướng dẫn bình thường của chương trình. Nói chung, khi một tập lệnh Python gặp một tình huống mà nó không thể đối phó, nó sẽ tạo ra một ngoại lệ. Một ngoại lệ là một đối tượng Python đại diện cho một lỗi. Khi một tập lệnh Python tạo ra một ngoại lệ, nó phải xử lý ngoại lệ đó ngay lập tức nếu không nó sẽ kết thúc và thoát.**

**Có nhiều loại exception như:**
  * Exception
  * StopIteration
  * SystemExit
  * OverflowError
  * ...

```
Syntax
try:
    You do your operations here.
    ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
    If there is ExceptionII, then execute this block.
    ......................
else:
    If there is no exception then execute this block.
    ......................
finally:
    This would always be executed
    ......................

Code example:
    def baseException():
        try:
            fr = open("demo.txt", 'r')
            a = fr.read()
            print(f"Content of file demo.txt:{a}")
        except Exception:
            print("Something went wrong ")
            
    baseException()
    try:
        fo = open("text.txt", 'w')
        fo.write("Nguyen Duc Huy - TMA")
    except IOError:
        print("Error: File not found")
    else:
        print("Write file 'text.txt' successfully")
    finally:
        fo.close()
Result:
Something went wrong
Write file 'text.txt' successfully
```
####Raising an Exceptions
**Bạn có thể raise các exceptions theo một số cách bằng cách sử dụng câu lệnh raise. Cú pháp chung cho câu lệnh tăng như sau:** `raise [Exception [, args [, traceback]]]
`
####User-Defined Exceptions
**Python cũng cho phép bạn tạo các ngoại lệ của riêng mình bằng cách Class trong Python**

```
Code example:
    import numpy as np
    class SalaryNotInRangeError(Exception):
        """Exception raised for errors in the input salary.

        Attributes:
            salary -- input salary which caused the error
            message -- explanation of the error
        """

        def __init__(self, salary, message="Salary is not in (100, 1000) range"):
            self.salary = salary
            self.message = message
            super().__init__(self.message)

        def __str__(self):
            return f'{self.salary} -> {self.message}

    salary = np.random.randint(1,2000)
    if not 100 < salary < 1000:
        raise SalaryNotInRangeError(salary)
Result:
Traceback (most recent call last):
  File "main.py", line 33, in <module>
    main()
  File "main.py", line 30, in main
    raise mod.SalaryNotInRangeError(salary)
modules.SalaryNotInRangeError: 1512 -> Salary is not in (100, 1000) range
```