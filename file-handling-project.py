from pathlib import Path
import os

# Function for show all file
def show_file():
    path = Path('')
    items = list(path.rglob('*'))
    print("All file is here: ")

    for idx, items in enumerate(items):
        print(f"{idx+1} : {items}")



# Create a new file
def create_file():
    try:
        name = input("Enter your file name: ")
        p = Path(name)

        if (not p.exists()):
            with open(p, 'w') as fs:
                data = input("Write file content: ")
                fs.write(data)
            print("File Created Successfully...")
        else:
            print("This file is already exist.")

    except Exception as err:
        print(f"Error is {err}")



# Read file:
def read_file():
    try:
        name = input("Enter your file name: ")
        p = Path(name)
        if(p.exists() and p.is_file()):
            with open(p , 'r') as fs:
                data = fs.read()
                print(data)
            print("File Read Successfully...") 
        else:
            print("Not found!")       

    except Exception as err:
        print(f"Error is {err}")    



# Update file:
def update_file():
    try:
        name = input("Which file do you want to read? ")
        p = Path(name)
        if(p.exists() and p.is_file()):
            data = input("Rename file")
            p2 = Path(data)
            p.rename(p2)
        print("File Rename Successfully") 

    except Exception as err:
        print(f"Error is {err}")            



# Delete File:
def delete_file():
    try:
        name = input("Which file do you want to delete? ")
        p = Path(name)
        if(p.exists() and p.is_file()):
            os.remove(p)
            print("File removed successfully...")
        else:
            print("Not Found!")    

    except Exception as err:
        print(f"Error is {err}")        


# Option
print("Press '1' for Show all file")
print("Press '2' for Create file")
print("Press '3' for Read file")
print("Press '4' for Update file")
print("Press '5' for Delete file")

option = int(input("Choose one option: "))

match option:
    case 1:
        show_file()
    case 2:
        create_file()
    case 3:
        read_file()
    case 4:
        update_file()
    case 5:
        delete_file()
    case _:
        print("Invalid option!")
