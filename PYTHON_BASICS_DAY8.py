#Create a list and print the values
n=int(input("Enter the number of elements: "))
list1=[]
for i in range(n):
    num=int(input("Enter the value: "))
    list1.append(num)
print("The marks of the student is ",list1)

#print the first and last value using indexing
print("The first value is ",list1[0])
print("The last value is ",list1[-1])

#To find the maximum and minimum values in a list
list2=sorted(list1)
print("The sorted list is: ",list2)
print("The maximum mark is: ",list1[-1])
print("The minimum mark is: ",list1[0])

#To count the how many times a number occurs in a list
n1=int(input("Enter the value to count: "))
if n1 in list2:
    print(list2.count(n1))
else:
    print(0)

#To find the index of the element in a list
n2=int(input("Enter the value to find the index: "))
if n2 in list2:
    print(list2.index(n1))
else:
    print("The Value ",n2," is not found in the list")






