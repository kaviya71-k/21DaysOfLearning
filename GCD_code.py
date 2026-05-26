def gcd(a,b):
    small=min(a,b)
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
a=int(input("enter a: "))
b=int(input("Enter b: "))
print(gcd(a,b))
    
