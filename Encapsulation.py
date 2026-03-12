class atm():
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def check_balance(self):
        entered_pin=int(input("Enter the pin: "))
        if self.__pin==entered_pin:
            print("The balance in the account is",self.__balance)
        else:
            print("the PIN is incorrect")
    def withdraw(self):
        entered_pin=int(input("Enter the pin: "))
        if self.__pin==entered_pin:
            withdraw=int(input("Enter the amount to withdraw"))
            if withdraw>=self.__balance:
                print("There is no suffient amount in the account")
            else:
                self.__balance-=withdraw
                print("The balance after the withdraw is: ",self.__balance)
        else:
            print("the PIN is incorrect")
    def deposit(self):
        entered_pin=int(input("Enter the pin: "))
        if self.__pin==entered_pin:
            amount=int(input("Enter the amount to deposit: "))
            self.__balance+=amount
            print("The balance after the deposit is: ",self.__balance)
        else:
            print("the PIN is incorrect")

pin=atm(6787,3000)


while True:
    print("1.Check balance")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        pin.check_balance()
    elif choice==2:
        pin.withdraw()
    elif choice==3:
        pin.deposit()
    elif choice==4:
        print("Thank you...Vist again!")
        break
    else:
        print("Invalid choice")
           
    
        
                      
                
                       
        
        
                
