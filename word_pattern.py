s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1
    print()
print("---------------")

s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p-=1
    print()
print("---------------")

s="CODER"
n=len(s)

for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end=" ")
        p+=1
    print()
print("---------------")

s="CODER"
n=len(s)

for i in range(n):
    p=n-1
    for j in range(i+1):
        print(s[p],end=" ")
        p-=1
    print()
print("---------------")

s="CODER"
n=len(s)
for i in range(n):
    p=n-1
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p],end=" ")
        p-=1
    print()
print("---------------")
