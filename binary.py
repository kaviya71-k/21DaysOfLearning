print("To search a number in an array using binary search:")
arr=[2,4,6,8,10]
target=8
l=0
r=len(arr)-1
while l<=r:
    n=(l+r)//2
    if arr[n]==target:
        print("The element is found at the index",n)
        break
    elif target>arr[n]:
        l=n+1
    elif target<arr[n]:
        r=n-1
else:
    print("The element is not found")

print("To check whether a number is present i an array or not:")
arr=[2,4,6,8,10]
target=8
l=0
r=len(arr)-1
found=False
while l<=r:
    n=(l+r)//2
    if arr[n]==target:
        found= True
        break
    elif target>arr[n]:
        l=n+1
    elif target<arr[n]:
        r=n-1
else:
    print("The element is not found")
print(found)
