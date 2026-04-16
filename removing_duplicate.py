def remove_duplicate(nums):
    l=1
    for r in range(1,len(nums)):
        if nums[r]!=nums[r-1]:
            nums[l]=nums[r]
            l+=1
    return nums[:l]

print(remove_duplicate([0,0,0,1,1,2,3,4,4]))
