class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition: ",self.a+self.b)
    def sub(self):
        print("Subtraction: ",self.a-self.b)
    def mul(self):
        print("Multiplication: ",self.a*self.b)
    def div(self):
        print("Division: ",self.a/self.b)

N1=int(input("Enter value1: "))
N2=int(input("Enter value2: "))
obj=calculator(N1,N2)
obj.add()
obj.sub()
obj.mul()
obj.div()
