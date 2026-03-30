marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

# Average
avg = sum(marks) / n

# Highest & Lowest
highest = max(marks)
lowest = min(marks)

# Pass/Fail (pass >= 50)
pass_count = 0
fail_count = 0

for m in marks:
    if m >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Average:", avg)
print("Highest:", highest)
print("Lowest:", lowest)
print("Pass:", pass_count)
print("Fail:", fail_count)
