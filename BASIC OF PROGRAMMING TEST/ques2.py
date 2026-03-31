print("Context management system")
total_msg=int(input("enter the number of messages"))
if total_msg>100:
  status="Normal"
  active="total_msg"
  comprssed=0
else:
  status="optimized"
  active=100
  compressed=total_msg-100
print(f"Status:{status},active:{active},compressed:{compressed}")
