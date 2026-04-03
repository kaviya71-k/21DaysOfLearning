print("Reverse an array")
arr=[2,3,4,5,6,7,8,9]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)

print("Palindrome")
s="madam"
l=0
r=len(s)-1
is_palindrome=True
while l<r:
    if s[l]!=s[r]:
        is_palindrome=False
        break
    l+=1
    r-=1
print(is_palindrome)


print("Move the zeores to one end")
arr=[0,2,4,0,6,0]
l=0
for r in range(len(arr)):
    if arr[r]!=0:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
print(arr)

print("Count pairs with sum")
target=6
arr=[2,3,4,5,6,7,8,9]
count=0
left=0
right=len(arr)-1
while left<right:
    s=arr[left]+arr[right]
    if s==target:
        count+=1
        left+=1
        right-=1
    elif s<target:
        left+=1
    else:
        right-=1
print("Pairs",count)
    

    
