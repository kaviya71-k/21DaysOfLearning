def sqrt(n):
    sign=0
    if n <0:
        sign=-1
        n=-n
    val=n
    while True:
        last=val
        val=(val+n/val)*0.5
        if abs(val-last)<0.000000001:
            break
    if sign<0:
        return complex(0,val)
    return val

n=int(input("Enter the number: "))
for i in range(1,n+1):
    print("Square root of",i,"is: ",sqrt(i))
    
