# print("Hello) --> Syntax Error

# a = 1
# if(a > 100):
# print(a)    --> Indentation Error


# -------- Exception ---------


# Prob1:
# a = int(input("write a number: "))
# print(10 / a) # 10/0 ==> (ZeroDivisionError) undefined.that's why here will be error
# print("Done") # not execute this line

# solution1: (Only for handle ZeroDivisionError)
# a = int(input("write a number: "))
# try:
#     print(10 / a)
# except ZeroDivisionError:
#     print("Sorry you can not write zero.Try again..")
# print("Done")   

# solution2: (for any type of exception)
# a = int(input("write a number: "))
# try:
#     print(10 / a)
# except Exception as error: # error is variable. It can be anything
#     print(f"here is an error that is '{error}'")    
# print("Done")


# Prob2:
a = input("write a number: ") # it take a string
try:
    print(10 / a) # 10/str --> error
except Exception as error: # error is variable. It can be anything
    print(f"here is an error that is '{error}'")    
print("Done")