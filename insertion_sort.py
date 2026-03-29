arr=[5,4,6,8,1,2]
count=0
print("Count the number of shifts in a array")
for i in range(1,len(arr)):
    cur=arr[i]
    j=i-1
    while j>=0 and cur<arr[j]:
        arr[j+1]=arr[j]
        j-=1
        count+=1
    arr[j+1]=cur
print("The sorted array",arr)
print("The number of shifts",count)

print("Insertion sort by step by step output")
arr=[5,4,6,8,1,2]
for i in range(1,len(arr)):
    cur=arr[i]
    j=i-1
    while j>=0 and cur<arr[j]:
        arr[j+1]=arr[j]
        j-=1
        
    arr[j+1]=cur
    print("Pass",i,":",arr[j])
print(arr)

arr=[5,4,6,8,1,2]

print("Stop after 2 pass")
for i in range(1,len(arr)):
    cur=arr[i]
    j=i-1
    while j>=0 and cur<arr[j]:
        arr[j+1]=arr[j]
        j-=1
        
    arr[j+1]=cur
    if i==2:
        print("After 2nd pass:",arr)
        break
               
