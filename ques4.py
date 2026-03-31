print("Fraud detection system")
amount=int(input("Enter the amount"))
location=input("Enter the location(1.Home  2.New)")
time=input("Enter the time in HH:MM format")
failed_attempts=int(input("Enter the number of failed attempts"))
if failed_attempt>=3:
  print("Risk level:LOCK")
else:
  risk=0
  if amount>50000:
    risk+=1
  if 0<time<5:
    risk+=1
  if location=="new":
    risk+=1
  if risk>=3:
    print("Risk level:High")
  else:
    print("Risk level:Low")
               
               
