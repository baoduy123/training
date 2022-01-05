import numpy as np

def main():
    a = np.random.randint(0, 10)
    if a > 5:
        print(f"{a}>5")
    elif a == 5:
        print(f"{a}=5")
    else:
        print(f"{a}<5")

if __name__ =='__main__':
    main()
