class mobile:
    network="5G"
    def __init__(self,brand):
        self.brand=brand
        self.price=12000
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print("The price is: ",self.price)
    @classmethod
    def changeNetwork(cls):
        cls.network="6G"
        print("The network is changed to 6G")
    @staticmethod
    def info():
        print("This is mobile class")
b1=input("Enter the brand: ")
samsung=mobile(b1)
p1=int(input("Enter the price: "))
samsung.setprice(p1)
samsung.getprice()
mobile.changeNetwork()
print("Network: ",mobile.network)
samsung.info()
