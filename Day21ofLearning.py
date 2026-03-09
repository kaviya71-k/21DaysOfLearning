print("Single inheritance")
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name)
        print("Age",self.age)
class student(person):
    def __init__(self,name,age,course,marks):
        super().__init__(name,age)
        self.course=course
        self.marks=marks
    def print(self):
        print("Course",self.course)
        print("Marks",self.marks)
s1=student("kavzz",29,"Ds",67890)
s1.display()
s1.print()


print("Multiple inheritance")
class camera():
    def take_photo(self):
        print("The photo is taken")
class musicplayer():
    def play_music(self):
        print("The music is played")
class smartphone(camera,musicplayer):
    pass
phone=smartphone()
phone.take_photo()
phone.play_music()


print("Multilevel inheritance")
class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno=rollno
class graduate(student):
    def __init__(self,name,rollno,degree):
        super().__init__(name,rollno)
        self.degree=degree
    def display(self):
        print("Name",self.name)
        print("Rollno",self.rollno)
        print("Degree",self.degree)
k=graduate("Kavzz",707,"ECE")
k.display()
         
print("Hybrid inheritance")
class employee():
    def work(self):
        print("The employee is working")
class developer(employee):
    def develope(self):
        print("The developer is developing the software")
class designer(employee):
    def design(Self):
        print("The design are ready to showcase")
class Teamlead(developer,designer):
    def lead(self):
        print("Team lead manages the coordination of all works")
t=Teamlead()
t.work()
t.develope()
t.design()
t.lead()
    
    
print("Hierarchical inheritance")
class vehicle():
    def startengine(self):
        print("The engine is started")
class car(vehicle):
    def drive(self):
        print("Car is driving")
class bike(vehicle):
    def ride(self):
        print("The bike is riding")
c=car()
c.startengine
c.drive
b=bike()
b.startengine()
b.ride()

    
        
        
