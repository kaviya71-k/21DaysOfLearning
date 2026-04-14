def longest_prefix(strs):
    min=float("inf")
    for s in strs:
        if len(s)<min:
            min=len(s)
    i=0
    while i<min:
        for s in strs:
            if s[i]!=strs[0][i]:
                return s[:i]
        i+=1
    return strs[0][:i]
print(longest_prefix(["flowers","flow","flight"]))
    
