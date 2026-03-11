class bikedelivery():
    def delivery(Self):
        print("Order will be delivered by bike")
class truckdelivery():
    def delivery(Self):
        print("Order will be delivered by truck")
class dronedelivery():
    def delivery(Self):
        print("Order will be delivered by drone")

cart=[]

n=int(input("Enter the number of items: "))
for n in range(1,n+1):
    items=input("Enter the items: ")
    cart.append(items)
print("The items in your cart are: ",cart)

print("Choose Delivery method")
print("1.Bike delivery")
print("2.Truck delivery")
print("3.Drone delivery")

choice=int(input("Enter the choice: "))
if choice==1:
    d=bikedelivery()
elif choice==2:
    d=truckdelivery()
elif choice==3:
    d=dronedelivery()
else:
    print("Invalid choice")
    exit()

d.delivery
()

        


    
          
          
          

        
