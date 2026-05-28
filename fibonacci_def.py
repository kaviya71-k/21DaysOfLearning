def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the number: "))
for i in range(1,n):
    print(fib(i))
