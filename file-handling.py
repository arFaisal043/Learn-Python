# file handling --> perform CRUD operation

# 'r':
# a = open(r'set.py')
# print(a.read())

# 'w': -> Override
# w = open("file.txt", 'w') # create file.txt
# w.write("Hello, I am Abdur Rahman Faisal.") # write content. If write new content then previous content will remove
# w.close()

# 'a': -> add
# w = open("file.txt", 'a') # create file.txt
# w.write("I am doing my undergraduate program in CSE.")# write content. If write new content then it will add 
# w.close()

# remove file:
# import os
# os.remove("file.txt")

# import os
# if os.path.exists("file.txt"):
#   os.remove("file.txt")
# else:
#   print("The file does not exist")