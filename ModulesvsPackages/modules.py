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
