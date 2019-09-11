grader = float(input("Vad är din temp"))

if grader > 39.5:
    print("Uppsök läkare")
elif grader > 37.8:
    print("Du har feber")
elif grader < 37.8:
    print("Du har inte feber")

