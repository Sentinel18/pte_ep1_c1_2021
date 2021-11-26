import datetime
import time

def get_afa(termek_ara: int, afa =27) -> float:
    return termek_ara * afa/ 100

def brutto(termek_ara: int, afa=27) -> float:
    return termek_ara + get_afa(termek_ara, afa)

ar = 1000
print(get_afa(ar))
print(brutto(ar))





"""
def pontos_ido():
    print(datetime.datetime.now())

def varakozas(masodperc: int):
    pontos_ido()
    time.sleep(masodperc)
    pontos_ido()

pontos_ido()
varakozas(10)



def benev() -> str:
    return input("Ki v\n")

def koszones(nev ="") -> None:
    print(f"Szia {nev}")

koszones()
koszones(benev())
"""