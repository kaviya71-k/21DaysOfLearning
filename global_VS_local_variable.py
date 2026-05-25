print("Example 1")
a=5
def funct():
    global a  # a is declared as global variable
    print("The value of a is",a) #value of a inside the function
    a=3
    print("The changed value of a is",a) #changed value of a inside a function
funct()
print("The value of a is:",a) #value of a outside the function

print("Example 2")
total=0
def sum(a,b):
    global total
    total=a+b # inside the function(local variable)
    print("The sum os a and b is(inside the function): ",total)
    return total
sum(100,200) # outside the function(Global variable)
print("The sum of a and b is(outside the function): ",total)

