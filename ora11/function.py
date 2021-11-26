import random
import math
"""""
print(chr(80), chr(121), chr(116), chr(104), chr(111), chr(110), sep="")
print(ord("p"))
print(ord("a"))
print(ord("A"))
print(ord(chr(80)))
print(float("3.5"))
print(type(float(3.5)))
print(int("12"))
print(int("12", base=16))
print(bin(18))
print(hex(18))
print(oct(18))
number = 23.6546564
print(number)
print(round(number, 2))
print(round(number, 0))


print("Adjon meg egy sebességet km/h-ban")
a = int(input())
a= a * 3.6
print(a, "m/s a sebesség")


randomlist = []
paros = []
paratlan = []
for i in range(0,10):
    n = random.randint(1,30)
    randomlist.append(n)
    if n %2 == 0:
        paros.append(n)
    else:
        paratlan.append(n)
print(randomlist)
print(paros)
print(paratlan)

print("Adja meg a háromszög hosszának az oldalait:")
print("Első oldal: ")
a = int(input())
print("Második oldal: ")
b = int(input())
print("Harmadik oldal: ")
c = int(input())
kerulet=(a+b+c)
d = (a+b+c) /2
terulet = (d* (d-a) * (d-b) * (d-c))
print(kerulet)
print(math.sqrt(terulet))


print("Írjon be számokat enter végjelig!")
lista = []
while len(lista) == 0 or lista[-1] != "":
    lista.append(input())
lista.remove("")
print(lista)

numbers = []
for i in range(20):
    numbers.append(random.randint(1,100))
print(numbers)
min = numbers[0]
max = numbers[0]
for number in numbers:
    if min > number:
        min = number
for number in numbers:
    if max < number:
        max = number
print(min, max)
"""

nev = input("Név: ")
