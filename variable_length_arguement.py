def printinfo(arg1,*vartuple):
    print("Output is")
    print(arg1)
    for var in vartuple:
        print(var)
printinfo(10)
printinfo(10,20,30,40,50)
printinfo('a','b','c','d','e','f','g','h','i')
