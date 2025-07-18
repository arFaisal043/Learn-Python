# Recursion is a function that can call itself.

# print 5 to 0 using recursive function.
# def rec(x):
#     if(x == -1):
#         return
#     print(x , end=" ")
#     rec(x - 1)
# rec(5)    



# find 5! using recursion.
# def fact(n):
#     if(n == 0 or n == 1): return 1   
#     return fact(n - 1) * n
# print(fact(5)) 



# Sum operation using recursion:
def sumByRecursion(n):
    if(n == 0): return 0
    return sumByRecursion(n - 1) + n

sum = sumByRecursion(5)
print(sum)