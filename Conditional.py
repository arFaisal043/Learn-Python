a = 2
b = 3
#if(a > b or a == b): print("a > b")


# Find max value in a list
# l = [1, 3, 2, 5, 4]
# max = float('-inf')

# for i in l:
#     if(i > max): 
#         max = i
#         continue
# print(max)


# Ternary Operator:
#print("a < b") if a < b else print("a > b")


# Pass Statement:
# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.
if(a < b):
    pass



# Switch Case/ Match statement:
# day = 1
# match day:
#   case 1: print("Monday")
#   case 2: print("Tuesday")
#   case 3: print("Wednesday")
#   case 4: print("Thursday")
#   case 5: print("Friday")
#   case 6: print("Saturday")
#   case 7: print("Sunday")
   


# Combine Values: Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case
# day = 7
# match day:
#    case 1 | 2 | 3 | 4: print("Today is workday")
#    case 5 | 6: print("This is weekend")
#    case _: print("Looking for weekend")
    


# check vowel
#Sol1
def checkVowel(str):
 cnt = 0
 for val in str:
    if(
        val == 'a' or
        val == 'e' or
        val == 'i' or
        val == 'o' or
        val == 'u'
    ):
        cnt += 1
    #print(cnt)
checkVowel("hello")

# sol2

def checkVowel(s):
    cnt = 0
    for char in s.lower():  # Convert to lowercase to handle all cases
        if char in {'a', 'e', 'i', 'o', 'u'}:  # Use a set for clarity
            cnt += 1
    print(cnt)  # Print total count after the loop

checkVowel("Hello")  # Output: 2 (e, o)
