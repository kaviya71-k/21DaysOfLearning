#Create a list and print the values
n=int(input("Enter the number of elements: "))
list1=[]
for i in range(n):
    num=int(input("Enter the value: "))
    list1.append(num)
print("The total price in the list is ",list1)

#To find the length of the list
print("Te total number of elements in the list are: ",len(list1))

#To find the sum of the values inside the list
total=0
for i in list1:
    total+=i
print("The total price is: ",total)

#Reverse a list
list1.reverse()
print("The reversed list is: ",list1)

#To remove a value at specific index
ind1=int(input("Enter the index value: "))
if 0<=ind1<=len(list1):
    list1.pop(ind1)
    print("The list after pop operation is: ",list1)
else:
    print("The index is not present in the list")

#To insert the value at specific index
value2=int(input("Enter the value: "))
index=int(input("Enter the index value: "))
if 0<=index<=len(list1):
    list1.insert(index,value2)
    print("The list after adding ",value2," at the index",index,"is",list1)
else:
    print("The index does not exist")

#Copy the list
list3=list1.copy()
print("The copied list is:",list3)

#Clear the copied list and print both the lists
list3.clear()
print("THe final lists are: ",list1,list3)
