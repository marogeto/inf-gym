#!/usr/bin/python3
import random as r
print(r.randint(0, 5))
''' Listenoperationen '''

print("Programm zum Suchen von Zahlen in einer Liste...")
# Variablendefinition
i = 0
f = []
liste = []
# Zufallsliste erzeugen
for i in range(40):
	liste.append(r.randint(0, 20))

print(liste)

# Eingabe der gesuchten Zahl:
a = "x"
while a == "x":
	try:
		a = int(input("Bitte Zahl eingeben, die in der Liste sein soll: "))
	except ValueError: # geh hier hin...
		print("Fehler: Keine Zahl eingegeben.")

# Suchen der Elemente in der Liste
# Ergebnisse werden in einem Array abgespeichert
for i in range(len(liste)):
	if a == liste[i]:
		f.append(i)

# Länge des Ergebnisfeldes
l_f = len(f)

# Aufgrund der Länge des Feldes ist Ausgabe formatieren
if l_f == 0:
	print("Zahl",a,"konnte nicht gefunden werden!")
elif l_f == 1:
	print("Einziges vorkommen der Zahl",a,"an der Stelle",f[0]+1)
else:
	for i in range(l_f):
		print("Vorkommen der Zahl",a,"an der Stelle",f[i]+1)


