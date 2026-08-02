def count(arr):
    arr.sort()
    for i in range(len(arr)):
        count=0
        current=arr[i]
        if i==0 or arr[i-1]!=current:
            for j in range(len(arr)):
                if arr[j]==current:
                    count+=1
            print(f"{current} appears {count} time(s)")
arr1=[1,3,4,2,5,6,4,3,2]
count(arr1)
                
        
