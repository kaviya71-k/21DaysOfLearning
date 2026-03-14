print("To reverse an array")
n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    num=int(input("Enter the elements: "))
    arr.append(num)
print(arr)
arr.reverse()
print("The reserved array is",arr)

print("To find the largest number")
n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    num=int(input("Enter the elements: "))
    arr.append(num)
print(arr)
max=arr[0]
for i in arr:
    if i>max:
        max=i
print("The largest number in the array is:",max)


print("To find the second largest number")
n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    num=int(input("Enter the elements: "))
    arr.append(num)
print(arr)
arr.sort()
print("The second largest number is",arr[-2])
