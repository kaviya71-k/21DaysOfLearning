print("array sorted in ascending order")
def mergesort(array):
    if len(array)>1:
        middle=len(array)//2
        left=array[:middle]
        right=array[middle:]
        mergesort(left)
        mergesort(right)
        lp=0
        rp=0
        fp=0
        while (lp<len(left) and rp<len(right)):
            if left[lp]<right[rp]:
                array[fp]=left[lp]
                lp+=1
            else:
                array[fp]=right[rp]
                rp+=1
            fp+=1
        while lp<len(left):
            array[fp]=left[lp]
            fp+=1
            lp+=1
        while rp<len(left):
            array[fp]=right[rp]
            fp+=1
            rp+=1

array=[4,6,7,2,1,9]
print(array)
mergesort(array)
print(array)

print("array sorted in desending order")
def mergesort1(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort1(left)
        mergesort1(right)
        lp=rp=fp=0
        while (lp<len(left) and rp<len(right)):
            if left[lp]>right[rp]:
                arr[fp]=left[lp]
                lp+=1
            else:
                arr[fp]=right[rp]
                rp+=1
            fp+=1
        while lp<len(left):
            arr[fp]=left[lp]
            fp+=1
            lp+=1
        while rp<len(right):
            arr[fp]=right[rp]
            fp+=1
            rp+=1




arr=[4,6,7,2,1,9]
print(arr)
mergesort1(arr)
print(arr)
