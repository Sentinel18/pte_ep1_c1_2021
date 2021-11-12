number = 35
if number > 100:
    print("A szám nagyobb, mint 100.")
else:
    print("A szám nem nagyobb, mint 100.")

if number % 2 == 0:
    print("A szám páros")
else:
    print("A szám nem páros")

number1= 36
number2 = 9
if number1 % number2 == 0:
    print("Az egyik szám osztható a másikkal")
else:
    if number2 % number1 == 0:
        print("A másik szám osztható az elsővel.")
    else:
        print("A számok nem oszthatóak.")
