arr=[12,34,45,2,89,65]
largest=arr[0]
second=arr[0]
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print("The largest number in the arr is",largest)
print("The second largest number in the array is",second)

arr=[12,34,45,2,89,65]
smallest=arr[0]
second_smallest=arr[0]
for i in arr:
    if i<smallest:
        second_smallest=smallest
        smallest=i
    elif i<second_smallest and i!=smallest:
        second_smallest=i
print("The smallest number in the arr is",smallest)
print("The second smallest number in the array is",second_smallest)
