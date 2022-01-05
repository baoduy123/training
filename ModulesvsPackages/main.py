import modules as mod
import my_packages as mp

arr = [1, 6, 3, 2, 8, 9]
num = 4

def main():
    # Goi qua modules
    print('Goi thong qua modules')
    print(f"{num} in {arr}") if mod.checkElement(
        num, arr) else print(f"{num} not in {arr}")

    print(f"Sum of arr:{arr}= {mod.calSumList(arr)}")

    print('\nGoi thong qua packages')

    print(f"{num} in {arr}") if mp.module1.checkElement(
        num, arr) else print(f"{num} not in {arr}")

    print(f"Sum of arr:{arr}= {mp.module2.calSumList(arr)}")

if __name__ == '__main__':
    main()
