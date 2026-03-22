def bubble_sort(arr):

    swap=0
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap+=1
    return arr,swap
arr=[7,3,4,6,9,1]
sorted,swap_count=bubble_sort(arr)
print("Sorted array: ",sorted)
print("Swap count: ",swap_count)


def bubble_sort(arr):

    comparison=0
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            comparison+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return comparison
arr=[7,3,4,6,9,1]
comparison_count=bubble_sort(arr)
print("Comparison count: ",comparison_count)


                
