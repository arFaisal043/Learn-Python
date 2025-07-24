
# type of string
# a = 'Hello'
# a = "Hello"
#  a = """Hello"""


# # Problem of ' ':
# # a = 'How's it going?' 
# # solution id use " "


# # Foe multiple line and New line
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# #print(a)

"""
# String Are Array: --> strings in Python are arrays of bytes representing unicode characters.
a = "Faisal"
# print(a[1])  // a






## String Operation ##

# Concatenation:
a = "Hello" 
b = "World"
# print(a + " " + b)


# Looping Through a String:
# a = "Hello World"
# for val in a:
#     print(val)


# String Length:
a = "Faisal"
#print(len(a))   



# Slicing:
a = "Faisal"
print(a[1 : 3]) # ai
print(a[ : 3]) # Fai
print(a[3 : ]) # sal
print(a[-5 : -2]) # ais


# Important Method
print(a.count("a")) # 2
print(a.endswith("al")) # true
print(a.replace("i" , "y")) # Faysal
print(a.find("s")) # 3


"""

# Check String:
# str = "Abdur Rahman Faisal"
# print("Rahman" in str) // true

# if "Rahman" in str:
#     print("Yes")


# s, part = "daabcbaabcbc", "abc"

# while(len(s) > 0 and s.find(part) < len(s)):
#       s.replace(part, " ")

# print(s)

s, part = "daabcbaabcbc", "abc"

while(part in s):  # While 'part' exists in 's'
    s = s.replace(part, "")  # Remove the first occurrence each time

print(s)  # Output: "dab"