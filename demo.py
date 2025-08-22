# p = open(r"set.py")
# print(p.read())

# c = open("file.txt", 'w')
# c.write("Hi there! I am Abdur Rahman Faisal. ")

# c = open("file.txt", 'a')
# c.write("I am doing my undergraduate program in CSE.")


import os
if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")