# list1 = [1 , 2 , 4 , 5 , 6]
# list2 = ["abc", 34, True, 40, "male"]
# list3 = [True, False, False]



# List are Mutable/changeable:
# list1 = [1 , 2 , 4 , 5 , 6]
# list1[0] = 100
# print(list1) # // [100, 2, 4, 5, 6]



# The list() Constructor:
# It is also possible to use the list() constructor when creating a new list.
a = list((1 , "a" , True)) # note the double round-brackets



# Slicing: - same as String
list = [1, 2, 3, 4, 5, 6]
# print(list[2 : 4])



# Check if Item Exists:
# list = [1, 2, 3, 4, 5, 6]
# if 1 in list:
#     print("Yes")



# Change a Range of Item Values:
# list = [1, 7, 8, 4, 5, 6]
# list[1 : 3] = [2 , 3]    
# print(list)  // [1, 2, 3, 4, 5, 6]



# Insert Items:
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# list = [1, 7, 8, 4, 5, 6]
# list.insert(1 , 2)
# print(list) // [1, 2, 7, 8, 4, 5, 6]



# insert that value in newList that's item has "a" 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for val in fruits:
    if "a" in val:
        newList.append(val)
# print(newList) // ['apple', 'banana', 'mango']
