import modules as mod
import numpy as np

def baseException():
    try:
        fr = open("demo.txt", 'r')
        a = fr.read()
        print(f"Content of file demo.txt:{a}")
    except Exception:
        print("Something went wrong ")

def main():
    # Base class for all exceptions
    baseException()
    
    # IO exception
    try:
        fo = open("text.txt", 'w')
        fo.write("Nguyen Duc Huy - TMA")
    except IOError:
        print("Error: File not found")
    else:
        print("Write file 'text.txt' successfully")
    finally:
        fo.close()
    
    #User defined  exception
    salary = np.random.randint(1,2000)
    if not 100 < salary < 1000:
        raise mod.SalaryNotInRangeError(salary)

if __name__ == '__main__':
    main()
