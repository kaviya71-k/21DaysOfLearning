def relational(a,b):
    equal=a==b
    not_equal=a!=b
    greater_than=a>b
    smaller_than=a<b
    greater_than_equal=a>=b
    smaller_than_equal=a<=b
    return equal,not_equal,greater_than,smaller_than,greater_than_equal,smaller_than_equal
a=int(input("Enter a number: "))
b=int(input("enter a number: "))
print(relational(a,b))
