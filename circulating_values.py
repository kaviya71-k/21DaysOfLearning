n=int(input("Enter the number of values: "))
list=[]
for i in range(0,n):
    x=int(input("Enter the values: ",))
    list.append(x)
print("The list is: ",list)
for i in range(0,n):
    x=list.pop(0)
    list.append(x)
    print("The circulating list: ",list)
