class Electricity_bill():
    def __init__(self):
        self.__units=0
        self.__rate=0
        self.__bill=0
    def set_rate(self):
        self.__rate=int(input("enter the rate: "))
    def set_units(self):
        self.__units=int(input("enter the units: "))
    def calculate_bill(self):
        self.__bill=self.__rate*self.__units
    def display_bill(self):
        print("Unit consumed",self.__units)
        print("Rate per unit:",self.__rate)
        print("total bill:",self.__bill)
        
e=Electricity_bill()
e.set_rate()
e.set_units()
e.calculate_bill()
e.display_bill()
