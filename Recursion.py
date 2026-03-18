def linear_Search(arr,n,key):
    if n==0:
        return -1
    if arr[n-1]==key:
        return n-1
    return linear_Search(arr,n-1,key)
print(linear_Search([2,3,4,5,6],5,4))

def binary_Search(arr,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return binary_Search(arr,low,mid-1,key)
    else:
        return binary_Search(arr,mid+1,high,key)
arr=[10,20,30,40,50,60]
print(binary_Search(arr,0,len(arr)-1,40))
    
    

