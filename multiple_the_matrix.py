a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]=a[i][k]*b[k][j]
print("Matirx A")
for r in a:
    print(r)
print("Matirx B")
for r in a:
    print(r)
print("Resultant matrix")
for r in a:
    print(r)
    
