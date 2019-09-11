totalaMinuter = int(input("Ange antal minuter"))

if totalaMinuter < 60:
    print(f"Antal minuter {totalaMinuter}")
elif totalaMinuter >= 60 and totalaMinuter < 24*60:
    print(f"Timmar: {totalaMinuter//60} Minuter: {totalaMinuter%60}")
elif totalaMinuter >= 24*60:
    dygn = totalaMinuter//(24*60)
    restPaDygnet = totalaMinuter%(24*60)
    print(f"Dygn{dygn} Timmar: {restPaDygnet//60} Minuter: {restPaDygnet%60}")



    ## början
    #from dataclasses import dataclass

    #@dataclass
    #class Person:
    #    name: str
    #    age: int
    #    weight: float

    #    def __repr__(self):
