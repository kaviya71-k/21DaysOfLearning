no_prime=[j for i in range(2,500) for j in range(i**2,500,i)]
prime=[x for x in range(2,500) if x not in no_prime]
print(prime)
