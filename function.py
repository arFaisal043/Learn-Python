# def printHelloWorld():
#     print("Hello World!")
# printHelloWorld()


# def sum(a , b):
#     return a + b
# print(sum(10 , 20))


# def passStr(str):
#     print("string:", str)
# passStr("Faisal")


# def findUniqueVal():
#     list = [1, 2, 3, 1, 3]
#     ans = 0
#     for i in list:
#         ans ^= i
#     print(ans)
# findUniqueVal() // call


# Pass Keyword: function definitions cannot be empty,put in the pass statement to avoid getting an error.
# def none():
#     pass
# none()




# -- Lambda Function:
# def sum(a , b):
#     return a + b
# print(sum(2 , 3))

# Sum using lambda function:
# sum = lambda x , y: x + y
# print(sum(2 , 3))

# cube = lambda x: x * x * x
# print(cube(2))

# ternary = lambda a: f"{a} is a Even Number" if(a % 2 == 0) else f"{a} is a Odd Number"
# print(ternary(11))

# square = lambda x: x*x
# print(square(10))
    



# --- Map function:

# Problem1: square a list 
# l = [1, 2, 3, 4]
# # way 1
# newList = list(map(lambda a: a**2, l))
# print(newList) #[1, 4, 9, 16]
# # way 2
# a = []
# for i in l:
#     a.append(i**2)
# print(a) #[1, 4, 9, 16]


# Problem2: Find Area on a list
# import math
# l = [1, 2, 3, 4]

# # Way 1: using for loop
# a = []
# for i in l:
#     a.append(math.pi * (i**2))
# print(a)    

# # Way 2: using map and lambda function
# b = list(map(lambda r: math.pi * (r**2) , l))
# print(b)


# Problem2: Add 2 list and Multiply
# list1 = [1, 2, 3, 4]
# list2 = [4, 3, 2, 1]
# newList = list(map(lambda a, b: a*b , list1, list2))
# print(newList) #[4, 6, 6, 4]


# Problem 3: convert Celsius To Fahrenheit.
# celScale = [10, 20, 30, 40, 50]
# # Way 1:
# farScale = []
# for i in celScale:
#     farScale.append(i*(9 // 5) + 32 )
# print(farScale) # [42, 52, 62, 72, 82]

# # Way 2:
# farScale = list(map(lambda c: c*(9 // 5)+ 32 , celScale))
# print(farScale) # [42, 52, 62, 72, 82]

# # Way 3:
# def CelsiusToFahrenheit(c):
#     return c*(9 // 5) + 32

# farScale = list(map(CelsiusToFahrenheit , celScale))
# print(farScale) # [42, 52, 62, 72, 82]




# ---- Filter function:
# - It filter some value based on the condition

# prob 1:
# l = [3.98, 2.75, 3.0, 3.50, 3.75]
# val = list(filter(lambda val: val > 3.0 , l))
# print(val) # [3.98, 3.5, 3.75]




# ---- Reduce method:
# from functools import reduce

# l = [1, 3, 2, 5, 4]
# max = reduce(lambda curr,prev: curr if(curr > prev) else prev, l)
# print(max) 

# sum = reduce(lambda curr,prev: curr + prev, l)
# print(sum)