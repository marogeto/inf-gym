#!/usr/bin/python3
'''
Aufgabe 6:

Schreiben Sie ein Programm, das die ersten n Primzahlen bestimmt und ausgibt.

Hinweise:
Der einfachste Algorithmus um zu ermitteln, ob eine Zahl x eine Primzahl ist, besteht darin, x durch jede Zahl kleiner als x zu teilen und zu überprüfen, ob ein Rest übrig bleibt.
Für die 25 würde der Algorithmus (ob 25 prim ist) also folgendermaßen ablaufen:

25 / 2 = 12 Rest 1
25 / 3 = 8 Rest 1
25 / 4 = 6 Rest 1
25 / 5 = 5 Rest 0 -> 25 ist keine Primzahl

Wenn der Algorithmus durchgelaufen ist, ohne einen Teiler für x gefunden zu haben, so muss x eine Primzahl sein.
Der Modulo-Operator % gibt den Rest zurück, der beim Teilen von zwei Zahlen übrig bleibt.
Sie brauchen zwei verschachtelte Schleifen. Eine, die die Zahlen 1 bis n hochzählt und eine, die jede dieser Zahlen mit jeder kleineren Zahl auf Teilbarkeit überprüft.
'''
prim = []
ausgabe = ""
x = 2
print("Bestimmen der ersten x Primazahlen...")
while 1 :
	try:
		x = int(input("Bitte x eingeben (x>1): "))
		if x > 1:
			break
		else:
			print("x muss größer 1 sein!")
	except ValueError:
		print("Falsche Eingabe!")

prim = [ i for i in range(x) ]
prim[0] = ""
prim[1] = ""
for i in range(2,x):
	for j in range(2,i):
		if i%j == 0:
			prim[i] = ""
			break

# 2 Dim Ausgabe
# Ausgabestring zusammen zimmern
for i in range(x):
	ausgabe += str(prim[i])+'\t'
	if (i+1)%10 == 0:
		ausgabe += "\n"

print(ausgabe)

		 
