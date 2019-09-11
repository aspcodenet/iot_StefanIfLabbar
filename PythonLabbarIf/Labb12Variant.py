valorer = [500,100,20,1]
restAttVaxla = int(input("Ange totalt belopp"))

for valor in valorer:
    antal = restAttVaxla // valor
    restAttVaxla = restAttVaxla % valor
    if antal > 0:
        print(f"Antal av {valor}:{antal}")
