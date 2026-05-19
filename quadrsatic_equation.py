import cmath
a=int(input("Enter the coefficent of x^2: "))
b=int(input("Enter the coefficent of x: "))
c=int(input("Enter the coefficent of constant: "))
d=(b**2)-4*a*c
if d>0:
    print("The roots are real and unequal")
    r1=(-b+d**0.5)/2*a
    r2=(-b-d**0.5)/2*a
    print("The roots are:",r1,r2)
elif d==0:
    print("The roots are real and equal")
    r1=-b/2*a
    print("The root is:",r1)
else:
    print("The roots are imaginary and unequal")
    r1=(-b+cmath.sqrt(d))/2*a
    r2=(-b-cmath.sqrt(d))/2*a
    print("The roots are:",r1,r2)


      
