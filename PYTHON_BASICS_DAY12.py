#Basci function
def greet():
    print("Welcome to Python Programming")
greet()

#Arguments
def square(n):
    print(n**2)
result=int(input("Enter the number: "))
square(result)

#Return value
def add():
    a=int(input("Enter the value1: "))
    b=int(input("Enter the value2: "))
    return a+b
print(add())

#Function+Condition
def check_even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
result=int(input("Enter the value: "))
print(check_even(result))
