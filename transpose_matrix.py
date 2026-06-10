a=[[1,2],[3,4],[5,6]]
result=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[j][i]=a[i][j]
print("Original matrix: ")
for r in a:
    print(r)
print("Transpose matrix: ")
for r in result:
    print(r)
