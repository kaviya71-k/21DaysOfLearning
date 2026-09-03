"""Here self.name is public
self._age is protected
self.__mark is private"""
#Encapsulation
class student:
    def __init__(self,name,age,mark):
        self.name=name
        self._age=age
        self.__mark=mark
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self._age)
        print("Mark: ",self.__mark)
    
    def set_mark(self,mark):
        self.__mark=mark
        print("updated marks: ",self.__mark)

name=input("Enter name: ")
age=int(input("Enter age: "))
mark=int(input("Enter marks: "))

s1=student(name,age,mark)
s1.display()

set1=int(input("Enter marks to be updated: "))
s1.set_mark(set1)
