for num in range(1,20):
    for i in range(2,num):
        if num/i==0:
            j=num/i
            print(f"{num} equal {i}*{j}")
            break
    else:
        print(num,"is a prime number")
                  
