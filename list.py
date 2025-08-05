## Power of List --> "Mutable", "Ordered", "Heterogenous", "Alow Duplicates Value"

# list1 = [1 , 2 , 4 , 5 , 6]
# list2 = ["abc", 34, True, 40, "male"]
# list3 = [True, False, False]


# l = [1, 2, 3]
# x = l
# x[0] = 100
# print(x) // [100, 2, 3]

# List are Mutable/changeable:
# list1 = [1 , 2 , 4 , 5 , 6]
# list1[0] = 100
# print(list1) # // [100, 2, 4, 5, 6]



# The list() Constructor:
# It is also possible to use the list() constructor when creating a new list.
a = list((1 , "a" , True)) # note the double round-brackets



# Slicing: - same as String
list = [1, 2, 3, 4, 5, 6]
# print(list[2 : 4]) // [3, 4]



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



# --------- Practice Questions: ----------

# 1. insert that value in newList that's item has "a" 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for val in fruits:
    if "a" in val:
        newList.append(val)
# print(newList) // ['apple', 'banana', 'mango']



# 2. Find max/min elm on the list.
l = [2, 5, 1, 9, 7]
max = float("-inf") 
for i in l:
    if(i > max):
        max = i
# print(f"Maximum number is {max}") 



# 3. Find largest & second largest number.
arr = [2, 5, 1, 9, 7]
largest = float("-inf")
secLargest = float("-inf")

for i in arr:
    if(i > largest):
        secLargest = largest #  -inf/ 2 / 5
        largest = i #  2 / 5 / 9
    elif(i > secLargest):
        secLargest = i  # 7  
# print(f"Largest Value: {largest},", f"Second Largest Value: {secLargest}")



# 4. List is sorted or not?
def isSorted(list):
    for i in range(len(list) - 1):
        if(list[i] > list[i + 1]): return False
    return True    
# print(isSorted([1, 33, 3, 4, 5]))

  

# 5. Count value:
# (for any 1 value)
# l = [1, 2, 3, 1, 2, 1]
# cnt = 0
# for i in l:
#     if(i == 1): cnt += 1
# print(cnt) // 3

# (for all value) -- use Dictionary
# l = [1, 2, 3, 1, 2, 1, 4, 3, 2, 2, 100]
# d = {} 
# for i in l:
#     if i in d.keys(): # is i exist in dict?
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)  


"""
6. Diagonal Sum: O(n2)
def diagonal_sum(l , n):
    sum = 0
    for i in range(0 , n):
        for j in range(0 , n):
            if(i == j):
                sum = sum + l[i][j]
            elif(j == n - i -1):
                sum = sum + l[i][j] 
    return sum


l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = 4
print(diagonal_sum(l , n))


-- Optimize solution -> O(n):
def diagonal_sum(l , n):
    sum = 0
    for i in range(0 , n):
        sum = sum + l[i][i]
        if(i != n-1-i):
            sum = sum + l[i][n-1-i]

    return sum


l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = 4
print(diagonal_sum(l , n))
"""