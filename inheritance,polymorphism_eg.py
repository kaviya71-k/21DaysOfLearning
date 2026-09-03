class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)
class manager(employee):  #inheritance
    def __init__(self,name,salary,department):
        super().__init__(name,salary)  #super keyword
        self.department=department
    def show(self):    #Polymorphism
        super().show()
        print("Department: ",self.department)
name=input("Enter name: ")
salary=int(input("Enter salary: "))
department=input("Enter department: ")
emp=manager(name,salary,department)
emp.show()
        
