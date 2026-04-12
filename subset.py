def subset(nums):
    res=[[]]
    for num in nums:
        temp_res=[]
        for subset in res:
            new_subset=temp_res+[num]
            temp_res.append(new_subset)
        res+=temp_res
    return res
print(subset([1,2,3]))
