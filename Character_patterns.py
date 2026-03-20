n=5
for i in range(n):
    for j in range(i+1):
        print("A",end=" ")
    print()
print("-------------------")

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=1
    print()
print("-------------------")

n=5
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p-=1
    print()
print("-------------------")

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=2
    print()
print("-------------------")

n=5

for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print("A",end=" ")
        else:
            print("B",end=" ")
    p+=1
    print()
print("-------------------")

n=5

for i in range(n):
    for j in range(i,n):
        if i%2==0:
            print("Z",end=" ")
        else:
            print("0",end=" ")
    p+=1
    print()
print("-------------------")


        
