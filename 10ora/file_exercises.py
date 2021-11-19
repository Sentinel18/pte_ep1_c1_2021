"""
Írjon programot, ami soronként beolvassa a lorem.txt fájl tartalmát
 és megjeleníti a kijelzőn!
"""
fileobject = open("lorem.txt", "r")
sor = fileobject.readline()
while len(sor) > 0:
  #  print(sor)
    sor = fileobject.readline()
fileobject.close()
"""
Írjon programot, ami beolvassa a lorem.txt fájl tartalmát és kiírja a konzolra,
 a leghosszabb sorát!
"""
fileobject = open("lorem.txt", "r")
leghosszabb = fileobject.readline()
for sor in fileobject: # ezzel amegoldással is kiiratható minden sor
    if (len(leghosszabb) < len(sor)):
        leghosszabb = sor
print(leghosszabb)
fileobject.close
"""
Írjon programot, ami átmásolja egyik fájl tartalmát egy másikba!
"""
fileobject = open("lorem.txt", "r")
fileobject2 = open("lorem_copy.txt", "w")
fileobject2.write(fileobject.read())
fileobject.close()
fileobject2.close()
"""
Az előző programot módosítsa úgy, hogy minden szóközt 3 másikra cseréli!
"""

"""
Írjon programot, ami 2 fájlt tartalmát egy harmadikba fésüli össze!
"""