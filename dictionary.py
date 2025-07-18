dict = {
    "Name" : "Faisal",
    "Age" : 22,
    "ID" : 2023200000043,
    "Courses" : ["Java", "EEE", "Management", "Statistics"],
    "isAdult" : True
}
# print(dict["Name"]) // Faisal
# print(dict["ID"]) // 2023200000043


# Nested Dictionary:

nestedDict = {
    "Name" : "Faisal",
    "Age" : 22,
    "ID" : 2023200000043,
    "Courses" : ["Java", "EEE", "Management", "Statistics"],
    "isAdult" : True,
    "Marks" : {
        "C" : 3.75,
        "Ethics" : 3.5,
        "Algebra" : 3
    }
}
# print(nestedDict["Marks"]["C"]) // 3.75


# Sum if key value are same:
# a = {1:100, 2:200, 3:300}
# b = {3:900, 4:400, 5:500}

# for i in b:
#     if i in a.keys():
#         a[i] += b[i]
#     else: a[i] = b[i]    
# print(a)    