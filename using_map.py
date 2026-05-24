print("Using map")
my_list=[1,2,3,4,5,6,7]
def sqr(n):
    return n**2
print(list(map(sqr,my_list)))

def sqrt(x):
    return x**2
def cube(x):
    return x**3
function=[sqrt,cube]
for i in range(1,6):
    value=list(map(lambda x:x(i),function))
    print(value)
