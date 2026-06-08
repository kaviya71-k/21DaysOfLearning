def remove_vowels(s):
    vowels="aeiouAEIOU"
    scan_vowels=""
    for x in s:
        if x not in vowels:
            scan_vowels+=x
    return scan_vowels
test=remove_vowels("computer")=="cmptr"
print(test)
test=remove_vowels("aAebFUMkhiU")=="bFMkh"        
print(test)
