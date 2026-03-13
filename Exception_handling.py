list=[10,20,30,40,50]
try:
    index=int(input("Enter the value: "))
    value=list[index]
    result=100/value
    print("The answer the answer is: ",result)
except ValueError as e:
    print("error:",e)
except IndexError as e:
    print("error:",e)
except TypeError as e:
    print("error:",e)
except:
    print("Something went wrong")
    
              
