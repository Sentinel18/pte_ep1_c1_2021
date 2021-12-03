def rendezes(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()
    for i in range(1, len(lista)):
        for j in range (len(lista)-1):
            if rendezett_lista[j] > rendezett_lista[j+1]:
                seged = rendezett_lista[j]
                rendezett_lista[j] = rendezett_lista[j-1]
                rendezett_lista[j+1] = seged
    return rendezett_lista


def minimum(lista:list[int], hanyadik=0) -> int:
    return rendezes(lista)[haynadik]

def osszeg(lista:list[int]) -> int:
    osszeg = 0
    for elem in lista:
        osszeg +=elem
    return osszeg

def atlag(lista: list[int]) -> float:
    return osszeg(lista) / len(lista)
lista = [42,12,76,23,51,23,36]
print(lista)
print(rendezes(lista))

