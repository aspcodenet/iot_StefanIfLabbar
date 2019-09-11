secretUser = "stefan"
secretPassword = "hemligt"

namn = input("Ange inloggning:")
pwd = input("Ange password:")
if(namn != secretUser):
    print("Fel inloggning")
elif pwd != secretPassword:
    print("Fel lösen")
else:
    print("Du är inloggad")
