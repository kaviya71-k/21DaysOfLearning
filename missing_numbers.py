def missing_num(nums):
    res=len(nums)
    for i in range(len(nums)):
        res+=1
        res-=nums[i]
    return res
print(missing_num([0,1,3]))
