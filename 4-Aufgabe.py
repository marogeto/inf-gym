#!/usr/bin/python3
import random as r
import os
from time import sleep
feld = []
eingabe = ""

'''Aufgabe 4:
Gegeben ist ein Array mit Zahlen als Werten:
[2, 17, 10, 9, 16, 2, 9, 16, 5, 1, 17, 14, 16, 1, 1, 2]
# In diesem Zahlenfeld ist der größte (Maximum)  bzw. der kleinste Wert (Minimum) zu ermitteln.
# Das Array ist dahingehend zu untersuchen, ob Werte mindestens doppelt vorkommen.
# Es soll festgestellt werden, wie oft ein bestimmter Wert bzw. Zeichen in einem Array vorkommt.
# In diesem Array sollen die 2 kleinsten Werte ermittelt werden.'''

def maxWert(f):
	print(f)
	t = f[0]
	for i in range(1,len(f)):
		if t < f[i]:
			t = f[i]
	print("Größte Zahl in der Liste ist:", t)
	input("Bitte beliebige Taste drücken zum fortsetzen...")
	return 0

def minWert(f):
	print(f)
	t = f[0]
	for i in range(1,len(f)):
		if t > f[i]:
			t = f[i]
	print("Kleinste Zahl in der Liste ist:", t)
	input("Bitte beliebige Taste drücken zum fortsetzen...")
	return 0

def doppelteWerte(f):
	print(f)
	w = [ 0 for i in range(len(f)) ]
	for i in range(len(f)):
		w[f[i]] += 1
	for i in range(len(w)):
		print(i, "kommt", w[i],"mal vor")
	input("Bitte beliebige Taste drücken zum fortsetzen...")
	return 0

def anzWerte(f):
	return 0

def zweiMin(f):
	return 0

# Erzeugen eines zufälligen Feldes
def createListe(t):
	for i in range(30):
        	t.append(r.randint(0,30))
		
while eingabe != 'x':
	feld = []
	createListe(feld)
	os.system('clear')
	print("Menü:")
	print("  Maximaler Wert: ma")
	print("  Minimaler Wert: mi")
	print("  Doppelte Werte: do")
	print("  Wie oft kommen Werte vor: an")
	print("  Bestimmung der zwei kleinsten Werte: 2m")
	eingabe = input("> ")
	if eingabe == "ma":
		a = maxWert(feld)
	elif eingabe == "mi":
		a = minWert(feld)
	elif eingabe == "do":
		a = doppelteWerte(feld)
	elif eingabe == "an":
		a = anzWerte(feld)
	elif eingabe == "2m":
		a = zweiMin(feld)
	elif eingabe == "x":
		print("ByeBye...")
	else:
		print("Falsche Eingabe.")
		sleep(0.5)
