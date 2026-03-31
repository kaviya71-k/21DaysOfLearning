logs= ["INFO", "ERROR", "ERROR", "INFO", "ERROR", "ERROR", "ERROR", "INFO"]
total_error=0
current_streak=0
longest_streak=0
for log in logs:
  if log=="ERROR":
    total_error+=1
    current_streak+=1
    if current_streak>longest_streak:
      current_streak=longest_streak
print(f"the total error:{total_error},Streak:{longest_streak}") 
    

