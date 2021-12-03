def menu_opciok():
    print("Válasszon az alábbi menűpontok közül:\n\t0 - Kilépés"
          "\n\t1 - Új fa rögzítése"
          "\n\t2 - Fa lekérdezése"
          )


def egesz_szam_bekerese(koordinata: str):
    szam = ""
    while szam == "":
        try:
            szam = int(input(f"Adja meg {koordinata} kordinátát"))
        except ValueError:
            print("Nem egész szám")
    return szam

def fa_regisztralasa(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x,y)
    if hely in fak:
        print("Itt már áll egy fa")
    else:
        fak[hely] = input("Kérem adja meg a fa fajtáját: ")
        print("Sikeres regisztráció")

        def szotar_kiitarasa(szotar, filepath):
            fileobject = open(filepath, "w")
            for kulcs in szotar:
                fileobject.write(str(kulcs[0]))
                fileobject.write("\t")
                fileobject.write(str(kulcs[1]))
                fileobject.write("\t")
                fileobject.write(str(kulcs))
                fileobject.write("\n")
                fileobject.close()

def szotar_betoltes(filepath: str):
    szotar = {}
    fileobject = open(filepath, "r")
    for sor in fileobject:
        adat = sor.strip().split("\t")
        szotar[(int(adat[0]), int(adat[1]))] = adat[2]
    fileobject.close()
    return szotar

def fafajta_lekeredezese(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x,y)
    if hely in fak:
        print(fak[hely])
    else:
        print("Ezen a koordinátán nincs fa")
menu = ""
fak_szotar_filepath = "fak.csv"
fak = {}
while menu != "0":
    menu_opciok()
    menu = input()
    if menu== "1":
        fa_regisztralasa(fak)
    elif menu == "2":
        fafajta_lekeredezese
szotar_kiiratasa(fak_szotar_filepathk)