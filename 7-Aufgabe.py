#!/usr/bin/python3
import sys

x = 0
x = int(sys.argv[1])

'''Aufgabe 7:
Die Aufgabe, wie oft die Gläser klingen, wenn jeder mit jedem anstößt, ist bekannt. 
Es handelt sich um die Formel von Gauß und bei n Personen wird n*(n-1)/2 mal angestoßen.

Doch diese Party ist anders.

Nach und nach betreten die 20 Gäste den Ballsaal. Einer nach dem anderen. Leider vergeht 
von Gast zu Gast so viel Zeit, dass alle Anwesenden bereits wieder ausgetrunken haben. 
'''

print("Die etwas andere Party...")
print("Du bist Single und feierst Deinen Geburtstag")

if x == 0:
	while 1 :
		try:
			x = int(input("Wieviele Gäste erwartest Du? "))
			if x < 1:
				print("Eingabe macht keinen Sinn!")
			else:
				break
		except ValueError:
			print("Bitte eine Ganzzahl eingeben!")


anz = 0
# 
for i in range(1,x+1):
	temp = i*(i+1)/2
	anz += temp
	print("Der", i, "te Gast: ",temp )		

print("In der Summe erklingen", anz,"mal die Gläser!")
