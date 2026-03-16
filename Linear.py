def linear_search(nums,target):
    for i in range(len(nums)):
        if target==nums[i]:
            return i
    else:
        return -1
nums=[4,5,6,3,2]
target=8
print(linear_search(nums,target))

def occurance(num,target):
    count=0
    for i in num:
        if i==target:
            count+=1
    return count
num=[4,4,5,6,4,3,2]
target=4
print(occurance(num,target))

def largest_num(numbers):
    max_num=num[0]
    for i in numbers:
        if i>max_num:
            max_num=i
    return max_num
numbers=[9,4,3,2,1,3,4]
print(largest_num(numbers))

    
