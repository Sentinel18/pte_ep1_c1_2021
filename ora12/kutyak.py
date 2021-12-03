class Kutya:
    """ A kutyák osztálya
    """

    def __init__(self, nev: str, fajta:str):
        self.nev = nev
        self.fajta = fajta

    def __init__(self):
        return ("A {} nevű kutya {} fajtájú".format(self.nev,self.fajta))

Kutya = kutya("Bodri","Kuvasz")
Kutya = Kutya2("Buksi","puli")
print(kutya1)
print(kutya2)