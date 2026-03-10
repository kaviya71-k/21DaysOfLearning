print("Password checker")
password=input("Enter the password: ")
cleaned=password.replace(" ","")
cleaned=cleaned.lower()
print("The cleaned password is: ",cleaned)
length=len(cleaned)
if length>8:
    print("The password is strong")
else:
    print("the password is weak")
