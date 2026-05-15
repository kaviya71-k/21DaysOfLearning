a=int(input("Enter the integer: "))
b=int(input("Enter the integer: "))
if ((a>0) and (b>0)):
    print("Both the numbers are posotive")
if ((a/2==0) or (b/2==0)):
    print("One number is even")
AND=a&b
OR=a|b
print("AND operator",AND)
print("OR operator",OR)


a=int(input("Enter the integer: "))
b=int(input("Enter the integer: "))
both_positive=(a>0) and (b>0)
one_even=(a/2==0) or (b/2==0)
print("Both numbers are positive",both_positive)
print("One number is even",one_even)
AND=a&b
OR=a|b
print("AND operator",AND)
print("OR operator",OR)
