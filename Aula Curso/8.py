import random   

check = random.choice([True, False, "Hamburger", "Pizza"])

if check == False:
    print("Its False")
    
elif check == "Hamburger":
    print("Yummy")
elif check == "Pizza":
    print("Yummy")
else:
    print("Its actually True")