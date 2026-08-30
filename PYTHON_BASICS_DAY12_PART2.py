#Function+Loop
def find_sum(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
result=int(input("Enter the value: "))
print(find_sum(result))

#Function with "return" that returns multiple values
def calculate(a,b):
    return a+b,a*b
v1=int(input("Enter the value1: "))
v2=int(input("Enter the value2: "))
print(calculate(v1,v2))

#Student mark Analyzer
def calculate_total(m1,m2,m3):
    total=m1+m2+m3
    return total
def calculate_average(total):
    average=total/3
    return average
def check_result(average):
    if average>=50:
        return "PASS"
    else:
        return "FAIL"    
m1,m2,m3=map(int,input("Enter the values: ").split())
total=calculate_total(m1,m2,m3)
average=calculate_average(total)
result=check_result(average)
print("The total marks is: ",total)
print("The average is: ",average)
print("The result is: ",result)


    
