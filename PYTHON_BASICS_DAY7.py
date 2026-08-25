print("TO FIND THE AVERAGE OF A RANGE OF NUMBERS")
#Program to find the average of the given numbers
n=int(input("Enter the number: "))
sum1=0
for i in range(n):
    nums=int(input("Enter the value: "))
    sum1+=nums
average=sum1/n
print("The average of the given numbers is: ",average)
print("----------------------------------------------------")


print("TO FIND THE UNIT DIGIT OF A NUMBER")
#Program to find the unit digit
n=int(input("Enter the number: "))
print("The unit digit of the given number ",n," is: ",n%10)
print("----------------------------------------------------")

print("COMBINING OPERATORS+CONDITIONS")
#Program to find whether the number lies within the range
num=int(input("Enter the number: "))
if num>=10 and num<=50:
    print("The number ",num," is inside the range")
else:
    print("The number ",num," is out of the range")
print("----------------------------------------------------")






      


