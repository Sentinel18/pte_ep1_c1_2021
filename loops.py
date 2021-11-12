is_number = False
number = 0
while not is_number:
    try:
        number = int(input("Kérek egy egész számot"))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám")

    if number % 2 == 0:
        print("páros")
    else:
        print("Páratlan")

i = 1
while i <= 5:
    print(i)
    i += 1
print()

for j in [1, 2, 3, 4, 5]:
    print(j)
print()

for k in range(100):
    print(k, end=" ")
print()

for l in range(50,60):
    print(l)

for m in range (0,101):
    if m % 2 != 0:
        print(m)

