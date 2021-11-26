number = 5
number2 = number * 2
print("A number változó értéke:", number,
      "\b. Ha megszorzom kettővel, akkor", number2, "\b-t kapok.")
print("A number változó értéke:", number,
      ". Ha megszorzom kettővel, akkor", number2, "-t kapok.", sep="")
print(f"A number változó értéke:{number}. Ha megszorzom kettővel, akkor {number2}-t kapok.")
print("A number változó értéke: {}. Ha megszorzom kettővel, akkor {}-t kapok." .format(number,number2))


#igazítások
print(f"A number változó értéke: {number:<3}. Ha megszorzom kettővel, akkor {number2:<3}-t kapok.")
print("A number változó értéke: {:^3}. Ha megszorzom kettővel, akkor {:^4}-t kapok.".format(number,
                                                                                      number2))

#számformátumok
number= 13
print("A number változó bináris értéke: {number:b.")
print("A number változó oktális értéke: {:0}".format(number))
print(f"A number változó decimális értéke: {number:d}.")
print("A number változó hexadecimális értéke: {:x} és {:x}".format(number) )





#valós számok
number = 100.1232