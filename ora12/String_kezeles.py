def megtalal(karakter: str, szoveg: str) -> int:
    """
    A karakter poziciójának megkeresése

    :paraméter karakter: Egyetlen karakter, amit a szövegben keresünk
    :paraméter szöveg: A szöveg, amiben keressük a karaktert.
    :return: A karakter előfordulása a szövegben, vagy -1, ha nincs benne
    """
    pozicio = 1

    while pozicio == -1 and i < len(szoveg):
     if szoveg[i] == karakter:
         pozicio = i
         i += 1
    return pozicio

def kacsanevek(prefixes='JKLMNOPQ', suffixe ='ack') -> None:
    nevek = []
    for kezdo_betu in prefixes:
        nevek.append(kezdo_betu + suffix)
    return nevek

print(megtalal("a","Indul a pap aludni"))
print(megtalal("a","Indul a pap aludni"))
print(megtalal("Indul a pap aludni".find("x")))
print(kacsnevek())