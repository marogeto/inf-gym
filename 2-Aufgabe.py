#!/usr/bin/python3
''' Listenoperationen '''

print("Programm zur Berechnung des Notendurchschnitts von x Zahlen...")
print("Ein Punkt beendet die Eingabe der Zahlen")
# Variablendefinition
liste = []
summe = 0
stringliste = ""
i = 1
# Eingabe der Noten:
while 1:
	try:
		a = input("Bitte die %d Note eingeben: " % i)
		if a == ".":
			break
		else:
			i += 1
			a = int(a)
			liste.append(a) # Für spätere Verarbeitung
			summe += a
			stringliste += str(a)+" "
	except ValueError: 
		i -= 1
		print("Fehler: Keine Zahl eingegeben.")

print("Eingegebene Noten:")
print(stringliste)
print("Der Duchschnitt ist: %.02f" % (summe/(i-1)) )	

