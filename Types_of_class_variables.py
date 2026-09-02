#class variale
class laptop:
    chargetype="C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand: ",self.brand)
        print("Price: ",self.price)
        print("Charging type: ",self.chargetype)

b1=input("Enter brand: ")
p1=int(input("Enter price: "))

b2=input("Enter brand: ")
p2=int(input("Enter price: "))

dell=laptop(b1,p1)
hp=laptop(b2,p2)
dell.display()
hp.display()
