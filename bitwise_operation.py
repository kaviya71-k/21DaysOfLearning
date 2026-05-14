def bitwise(a,b):
    AND=a&b
    OR=a|b
    XOR=a^b
    NOT_a=~a
    NOT_b=~b
    return AND,OR,XOR,NOT_a,NOT_b
a=int(input("Enter a number: "))
b=int(input("enter a number: "))
print(bitwise(a,b))
