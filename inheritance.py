class account:
    def __init__(self,account_no,holder_name):
        self.account_no=account_no
        self.holder_name=holder_name
    def display(self):
        print("Account number: ",account_no)
        print("Name: ",holder_name)
class Savingsaccount(account):
    def __init__(self,account_no,display,balance):
        super().__init__(account_no,holder_name)
        self.balance=balance
    def show(self):
        super().display()
        print("Balance: ",self.balance)
account_no=int(input("Enter account number: "))
holder_name=input("Enter name: ")
balance=int(input("Enter balance: "))
a1=Savingsaccount(account,holder_name,balance)
a1.show()
        
    
    
