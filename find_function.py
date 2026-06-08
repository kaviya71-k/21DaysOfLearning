def find(strng,ch):
    x=0
    while x<len(strng):
        if strng[x]==ch:
            return x
        x+=1
        return -1
test=find("Compsci","p")==3
print(test)
test=find("Compsci","C")==0
print(test)
test=find("Compsci","x")==-1
print(test)
print("_________________________________")

def count(text):
    count=0
    for i in text:
        if i =="o":
            count+=1
    return count
test=count("Problem Solving Python Programming")==4
print(test)
        
