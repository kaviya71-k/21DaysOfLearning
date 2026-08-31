#Factorial using recursion
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("Enter the value: "))
print("Factorial: ",fact(n))

#Sum of numbers using recursion
def find_sum(n1):
    if n1==0:
        return 0
    return n1 + find_sum(n1-1)
n1=int(input("Enter the value: "))
print("Sum: ",find_sum(n1))

#Fibonacci using recursion
def fibonacci(n2):
    if n2<=1:
        return n2
    return fibonacci(n2-1)+fibonacci(n2-2)
n2=int(input("Enter the value: "))
for i in range(n2):
    print(fibonacci(i),end=' ')





