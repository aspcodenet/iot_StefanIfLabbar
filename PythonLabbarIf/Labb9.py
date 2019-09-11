bil = input("Mata in en bil")

if bil != "Volvo":
    if bil == "Volkswagen" or bil == "BMW" or bil == "Audi":
        print("Bilen är tysk")
    elif bil == "Renault" or bil == "Peugeot" or bil == "Citroen":
        print("Bilen är fransk")
    else:
        print("Bilen är inte tysk eller fransk eller svensk")
