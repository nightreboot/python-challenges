from pathlib import Path
import os
print("1 for creating the file")
print("2 for reading the file")
print("3 for updating the file")
print("4 for deleting the file")
decision = int(input("Enter Tour Decision "))

def available_files():
    path = Path('')
    items = list(path.rglob("*"))
    for i , items in enumerate(items):
        print(f"{i}. {items}")

def creating_file():
    available_files()
    user = input("Enter your file name : ")
    write = input("Write something: ")
    p = Path(user)
    if not p.exists():
        with open(p, "w") as file:
            file.write(write)
        print("File is succesfully created")

def readfile():
    available_files()
    read = input("Enter Your existing file read: ")
    p = Path(read)
    if p.exists():
        with open(p, "r") as file:
             content = file.read()
             print(content)

def update_file():
    available_files()
    update = input("Choose your file: ")
    print("choose 1 for update the given file name")
    print("choose 2 for over write the given file name")
    print("choose 3 for append the given file name")
    choose = int(input("Enter Your Decision: "))
    p = Path(update)
    if p.exists():
        if choose == 1:
            file = input("Enter the updating file name")
            p.rename(file)
        if choose == 2:
            inp = input("Do you want Write Something")
            with open(p, "w") as file:
                file.write(inp)
        if choose == 3:
            append = input("Do you want Write Something")
            with open(p, "a") as file:
               file.write(append)
    else:
        print("Something went wrong")

def delete_file():
    available_files()
    user = input("which file you want delete: ")
    p = Path(user)
    if p.exists() and p.is_file():
        os.remove(p)
        print("file is delete Successfully")  
    else:
        print("Such file is not available")
if decision == 1:
    creating_file()       
if decision == 2:
    readfile()          
if decision == 3:
    update_file()  
if decision == 4:
    delete_file()


