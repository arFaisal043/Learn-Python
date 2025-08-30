expenses = [
    {"category" : "Food", "amount" : 2000},
    {"category" : "Transport", "amount" : 1000},
    {"category" : "Shopping", "amount" : 3000},
    {"category" : "Food", "amount" : 3000},
    {"category" : "Tuition fee", "amount" : 15000},
    {"category" : "Shopping", "amount" : 2000},
    {"category" : "Rent", "amount" : 20000},
    {"category" : "Course", "amount" : 1500}
]

# total income
income = 50000
print(f"Total income is: {income}")

# Total expense
total_expense = 0

for i in expenses:
    total_expense += i["amount"]
print(f"Total Expense is: {total_expense}")


# total cost in each category
category_wise = {}
for i in expenses:
    category = i["category"]
    amount = i["amount"]

    if(category in category_wise):
        category_wise[category] += amount
    else :
        category_wise[category] = amount    
print(f"Total cost in each category →  {category_wise}")



# compare with income and if have any saving?

savings = income - total_expense
if(savings > 0):
    print(f"Total savings is {savings}")
elif(savings == 0):
    print("No savings")
else:    
    print("Loss")



# highest expense category in dictionary    

import math
max_category = None
max_amount = -math.inf

for category,amount in category_wise.items():
    if(amount > max_amount):
        max_amount = amount
        max_category = category

print(f"Max Category and Amount is: '{max_category} : {max_amount}'")
