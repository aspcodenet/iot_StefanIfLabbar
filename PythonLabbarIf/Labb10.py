kronor = int(input("Ange hur mycket pengar du har"))
harRabatt = input("Har du rabatt J/N") == "J"
if kronor >= 15 and kronor <= 25  and harRabatt == false:
    print("Du kan köpa en liten hamburgare")
elif kronor >= 15 and kronor <= 25  and harRabatt:
    print("Du kan köpa en liten hamburgare och en pommes frites")
elif kronor > 25 and kronor <= 50  and harRabatt == false:
    print("Du kan köpa en stor hamburgare")
elif kronor > 25 and kronor <= 50  and harRabatt == true:
    print("Du kan köpa en stor hamburgare och en pommes frites")
elif kronor > 60 or (kronor >=50 and kronor <=60 and rabatt == true):
    print("Du kan köpa ett meal med dryck")



    ## början
    #from dataclasses import dataclass

    #@dataclass
    #class Person:
    #    name: str
    #    age: int
    #    weight: float

    #    def __repr__(self):
