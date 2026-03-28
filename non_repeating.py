def non_repeating(s):
    count={}
    
    for ch in s:
        count[ch]=count.get(ch,0)+1
    result=[]
    for ch in s:
        if count[ch]==1:
            result.append(ch)
    return result
print(non_repeating("aabbcdef"))
