restAttVaxla = int(input("Ange totalt belopp"))

fem = restAttVaxla // 500
restAttVaxla = restAttVaxla % 500
print(f"Antal femhundringar {fem}")

etthundra = restAttVaxla // 100
restAttVaxla = restAttVaxla % 100
print(f"Antal etthundringar {etthundra}")

tjugo = restAttVaxla // 20
restAttVaxla = restAttVaxla % 20
print(f"Antal tjugor {tjugo}")


enkronor = restAttVaxla // 1
restAttVaxla = restAttVaxla % 1
print(f"Antal enkronor {enkronor}")

