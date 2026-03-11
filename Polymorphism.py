print("payment system")
class creditcard():
    def pay(self):
        print("payment done using Credit card")
class debitcard():
    def pay(self):
        print("payment done using Debit card")
class upi():
    def pay(self):
        print("Payment done using UPI")
c=creditcard()
d=debitcard()
u=upi()
for payment in(c,d,u):
    payment.pay()
        
