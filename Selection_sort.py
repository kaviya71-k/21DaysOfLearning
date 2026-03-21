arr=[5,6,8,2,4,1]
for pos in range(len(arr)-1):
    min=pos
    for i in range(pos+1,len(arr)):
        if arr[i]<arr[min]:
            min=i
    arr[min],arr[pos]=arr[pos],arr[min]

print("The sorted array: ",arr)

arr=[5,6,8,2,4,1]
while True:
    a=True
    for pos in range(len(arr)-1):
        min=pos
        for i in range(pos+1,len(arr)):
            if arr[i]<arr[min]:
                min=i
                arr[min],arr[pos]=arr[pos],arr[min]
                a=False
            
    if a==False:
        continue
    elif a==True:
        break

print("The sorted array: ",arr)
