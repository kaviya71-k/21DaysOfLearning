class fruits:
    def __init__(self):
        self.colour=""
    def display(self):
        print("Colour: ",self.colour)
apple=fruits()
apple.colour=input("Enter the colur of the fruit: ")
apple.display()

class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("Name: ",self.name)
        print("Regno: ",self.regno)
name1=input("Enter the teacher 1 name: ")
regno1=int(input("Enter the register number of teacher 1: "))
name2=input("Enter the teacher 2 name: ")
regno2=int(input("Enter the register number of teacher 2: "))
t1=teacher(name1,regno1)
t2=teacher(name2,regno2)
t1.display()
t2.display()
        
