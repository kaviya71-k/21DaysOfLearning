def fact(n):
    print("fact has been called with n=="+str(n))
    if n==1:
        return 1
    else:
        res=n*fact(n-1)
        print("Inter mediate result for",n,"*fact(",n-1,"):",res)
        return res
n=int(input("Enter the number: "))
print(fact(n))
