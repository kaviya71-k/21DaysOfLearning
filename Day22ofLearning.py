print("To repalce a space by hypen")
text=input("Enter your text")
new=""
for i in text:
    if i==" ":
        new+="_"
    else:
        new+=i
print(new)
      
