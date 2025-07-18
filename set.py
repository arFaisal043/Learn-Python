# set = {1, 2, 3, 4}
# set[1] = 100
# print(set) // Error

# Empty Dict:
dict = {}
# print(type(value)) // Dict


# Empty Set:
collection = set()
# print(type(collection))



# Do not count duplicate value
# set = {1, 2, 3, 4, 3, 2}
# print(set) // {1, 2, 3, 4}



## Set Methods:

# add()
# set = {1, 2}
# set.add(3)
# print(set)

# union()
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.union(set2)) // {1, 2, 3, 4}

# Intersection()
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.intersection(set2)) // {2, 3}

# Difference()
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set = set1.difference(set2)
# s = set1 - set2 // shortcut
# print(set) // {1}
# print(s) 