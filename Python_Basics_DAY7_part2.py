print("COMBINING LOOPS+CONDITIONS")
#Program for printing tables only for odd numbers
num=int(input("Enter the number: "))
for i in range(1,num+1):
    if i%2==0:
        continue
    else:
        print(i,"*",2,"=",2*i)
print("----------------------------------------------------")

print("NESTED LOOPS")
#Program to print a matrix in nested loop (Row wise)
n=int(input("Enter the value: "))
for i in range(n+1):
    for j in range(n+1):
        print(i,end=" ")
    print()
print("----------------------------------------------------")

print("NESTED LOOPS")
#Program to print a matrix in nested loop(Column wise)
n=int(input("Enter the value: "))
for i in range(n+1):
    for j in range(n+1):
        print(j,end=" ")
    print()
print("----------------------------------------------------")

print("NESTED LOOPS")
#Program to print star pattern
n=int(input("Enter the value: "))
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()
