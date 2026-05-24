print("Using lambda")
double= lambda n:n*2
print(double(10))

print("Using filtering")
my_list=[1,2,3,4,5,6,7,8,9,10]
new_list=list(filter(lambda n:(n%2==0),my_list))
print(new_list)

print("lambda within lambda")
add_two= lambda n:n+2
multiple_two=lambda n:add_two(n*2)
print(multiple_two(3))




