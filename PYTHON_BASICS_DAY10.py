#Creating a dictionary
n=int(input("Enter the number of students: "))
students={}
for i in range(n):
    name=input("Enter the name: ")
    mark=int(input("Enter the mark: "))
    students[name]=mark
print(students)

#Traverse and print the dictionary
for key,val in students.items():
    print(key,val)
    
#Search a student in the dictionary
stu=input("Enter the student name: ")
if stu in students:
    print(students[stu])
else:
    print("The student",stu, "is not in the above list of data")

#Change the value in a dictionary
change=input("Enter the student name: ")
if change in students:
    new=int(input("Enter the updated mark: "))
    students[change]=new
    print("The updated dictionary is:",students)
else:
    print("The student",change, "is not in the above list of data")
