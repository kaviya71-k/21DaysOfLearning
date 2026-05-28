def pal(w):
    if len(w)==1:
        return True
    if len(w)==2:
        if w[0]==w[1]:
            return True
        else:
            return False
    else:
        if w[0]==w[-1]:
            return pal(w[1:-1])
        else:
            return False
str=input("Enter the word: ")
print(pal(str))
    
