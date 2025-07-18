list = [1, 2, 1, 3, 2, 1, 2, 2, 4, 3, 1, 1, 4]
dict = {}
for i in list:
    if i in dict.keys():
        dict[i] += 1
    else: 
        dict[i] = 1

print(dict)