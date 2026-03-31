print("API rate limiter")
request_count=int(input("enter the number of request made by the user"))
if request_count<=5:
  status="Allowed"
  print(f"Status:{status}")
else:
  status="Blocked"
  print(f"Status:{status},Rate limit exceeded")
