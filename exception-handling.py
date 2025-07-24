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
#  

# solution2: (for any type of exception) --> [when we not know what's type of error will come]
# a = int(input("write a number: "))
# try:
#     print(10 / a)
# except Exception as error: # error is variable. It can be anything
#     print(f"here is an error that is '{error}'")    
# print("Done")


# Prob2:
# a = input("write a number: ") # it take a string
# try:
#     print(10 / a) # 10/str --> error
# except Exception as err: # error is variable. It can be anything
#     print(f"here is an error that is '{err}'")    
# print("Done...")
   



# a = int(input("write a number: ")) # int
# try:
#     print(10 / a) # valid
# except Exception as err:
#     print(f"Error is: {err}")
# else: # It's work when if no exception occurs
#     print("Here is no any Exception.")    
# print("Done") 



# a = int(input("write a number: ")) # int
# try:
#     print(10 / a) # valid
# except Exception as err:
#     print(f"Error is: {err}")
# else: # It's work when if no exception occurs
#     print("Here is no any Exception.")
# finally:
#     print("I will run always, no matter what.")        
# print("Done")



# a = int(input("write a number: ")) # int
# try:
#     print(10 / a) # valid
# except Exception as err:
#     print(f"Error is: {err}")
# else: # It's work when if no exception occurs
#     print("Here is no any Exception.")
# finally:
#     print("I will run always, no matter what.")        
# print("Done")




age = int(input("Enter your age: "))

try:
    if(age < 18 or age > 22):
        raise ValueError("You can't admitted. Because your age is out of limit.") # not execute next any line
    else:
        print("Congratulation, your are welcome")
except Exception as err:
    print(f"Error is: {err}")      

print("The admission coming soon.")