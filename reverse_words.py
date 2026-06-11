string=input("Enter the string: ")
reversed_string=''
index=len(string)
while index>0:
    reversed_string+=string[index-1]
    index-=1
print("Original string: ",string)
print("reversed string: ",reversed_string)
