try:
    fileobject = open("lorem.txt", "r")
    tartalom = fileobject.readline()
    print(tartalom)
    print(type(tartalom))
    print=len(tartalom)
    fileobject.close()
except FileNotFoundError:
    print("Nem található ilyen fájl")