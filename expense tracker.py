expenses = {}

n = int(input("Enter number of entries: "))

for i in range(n):
    category = input("Enter category (food/travel/etc): ")
    amount = float(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

# Total
total = sum(expenses.values())

print("\nTotal Expense:", total)

print("\nCategory-wise Expense:")
for cat, amt in expenses.items():
    print(cat, ":", amt)
