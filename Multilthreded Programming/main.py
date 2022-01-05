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
def main():
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

if __name__ == '__main__':
    main()
        