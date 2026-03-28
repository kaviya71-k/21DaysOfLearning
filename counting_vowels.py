def vowels(s):
    count=0
    vowels="aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count+=1
    return count
print(vowels("hello world"))
        
