def majority(nums):
    res=None
    count=0
    for num in nums:
        if count==0:
            res=num
        if num==res:
            count+=1
        else:
            count-=1
    return res
print(majority([1,1,1,2,2,2,5,4,6,2,2]))
        
