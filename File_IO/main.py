import os

def main():
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

if __name__=='__main__':
    main()