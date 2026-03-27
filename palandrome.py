def palandrome(s):
    reversed = ""
    
    for ch in s:
        reversed = ch + reversed   

    if reversed == s:             
        return "Palindrome"
    else:
        return "Not a Palindrome"

print(palandrome("madam"))


def is_palindrome(num):
    original=num
    reversed=0
    while num>0:
        digit=num%10
        reversed=reversed*10+digit
        num=num//10
    if original==reversed:
        return "Palindrome"
    else:
        return "Not a palindrome"
print(is_palindrome(234))


def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "Anagram"
    else:
        "Not anagram"
print(anagram("listen","silent"))

