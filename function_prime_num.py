def prime_num(n):
    primes=[]
    for num in range(2,n+1):
        is_prime=True
        for divisor in range(2,int(num**0.5)+1):
            if num%divisor==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes
print(prime_num(20))
