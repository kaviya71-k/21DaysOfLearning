def sum_array(nums):
    sum=[]
    total=0
    for i in nums:
        total+=i
        sum.append(total)
    print(sum)
sum_array([1,2,3,4])
