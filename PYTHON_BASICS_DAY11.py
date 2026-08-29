#Even numbers using list comprehension
n=int(input("Enter the number: "))
nums=[j for j in range(1,n+1) if j%2==0]
print(nums)

#Square of Odd numbers
n=int(input("Enter the number: "))
number=[]
for i in range(n):
    num=int(input("Enet the number: "))
    number.append(num)
result=[i*i for i in number if i%2!=0]
print(result)

#Positive numbers using list comprehension
n=int(input("Enter the number: "))
number=[]
for i in range(n):
    num=int(input("Enet the number: "))
    number.append(num)
result=[i for i in number if i>0]
print(result)

    
    
