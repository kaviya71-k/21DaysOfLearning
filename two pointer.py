arr=[1,3,5,7,8,9]
target=10
l=0
r=len(arr)-1
while l<r:
    act=arr[l]+arr[r]
    if act==target:
        print("The numbers are",arr[l],"and", arr[r])
        break
    elif act<target:
        l+=1
    else:
        r-=1

arr=[1,3,5,7,8,9]
target=18
h=1
l=0
r=len(arr)-1
while l<r:
    act=arr[l]+arr[r]
    if act==target:
        h=0
        print("The numbers are",arr[l],"and", arr[r])
        break
    elif act<target:
        l+=1
    else:
        r-=1
if h==1:
    print("The target is not possible")
        
