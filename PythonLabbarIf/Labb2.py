antal = int(input("Hur många liter finns det kvar"))

if antal < 10: 
    print("Beställ 30 paket")
elif antal >= 10 and antal <= 20: 
    print("Beställ 20 paket")
else:
    print("Du behöver inte beställa någon mjölk")
