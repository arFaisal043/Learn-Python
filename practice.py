
s, part = "daabcbaabcbc", "abc"

def find_str():
    if part in s:
        return s.replace(part, "$")
    


arr = [1, 2, 3, 4, 5, 6, 7, 8]

for i in arr:
    print(i, "Even") if i % 2 == 0 else print(i, "Odd")