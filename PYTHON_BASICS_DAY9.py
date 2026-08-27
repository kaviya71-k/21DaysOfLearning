#Create a list and convert it into tuple
n=int(input("Enter the number of values: "))
mark=[]
for _ in range(n):
    mark1=int(input("Enter the value: "))
    mark.append(mark1)
    tup_mark=mark
print("The marks are: ",tup_mark)

#Get the index of first and last value
print(mark[0])
print(mark[-1])

#traversing through the tuple
for i in mark:
    print("The elements are: ",i)

#Search the index of an element
search=int(input("Enter the value to be searched: "))
if search in tup_mark:
    print("The index value of ",search,"is",tup_mark.index(search))
else:
    print("The element does not exist")

#Counting the number of times the value occured in the tuple
value=int(input("Enter the value to be searched: "))
if value in tup_mark:
    count = tup_mark.count(value)
    print("The element occurred", count, "times")
else:
    print("The element does not exist")

    
