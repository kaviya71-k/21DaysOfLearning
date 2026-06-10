avg=0
sum=0
n=int(input("Enter the number: "))
for i in range(1,n+1):
    a=int(input("Enter the integer: "))
    sum+=a
    avg=sum/n
print("Sum=",sum,"Average=",avg)
