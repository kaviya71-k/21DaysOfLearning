name="kaviya"
password="4567890"
for i in range(3):
    try:
        user_name=input("Enter the user name: ")
        user_password=input("Enter the password: ")
        if user_password==password and user_name==name:
            print("System unlocked")
        elif user_password=="" or user_name=="":
            raise ValueError("Username or password cannot be empty")
        else:
            print("Incorect password")
    except ValueError as e:
        print("Error",e)
    except TypeError as e:
        print("Error",e)
else:
    print("Too many failed attempts.system is locked...")
        
