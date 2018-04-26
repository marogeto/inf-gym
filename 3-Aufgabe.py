#!/usr/bin/python3
import os
import sys
import termios
import tty

os.system("clear")
w, h = 8, 8;
aktPos = [0,0]
ein = ""
# Initialisieren eines 2. Dim Arrays
spielfeld = [[0 for x in range(w)] for y in range(h)] 
# Spielfeld Definieren
for i in range(8):
    for j in range(8):
        if i == 0 and j == 0:
            spielfeld[i][j] = "X"
            aktPos[0] = j
            aktPos[1] = i
        else:
            spielfeld[i][j] = " "
print("LOS!")
print("-----------------------------")
for i in range(8):
        print(" | ".join(spielfeld[i]))
print("-----------------------------")


while ein != ".":
    # Code für das Eingeben von einem Zeichen auf der Tastatur
	old = termios.tcgetattr(sys.stdin)
	try:
		tty.setraw(sys.stdin)
		ein = sys.stdin.read(1)
	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old)
		
	os.system("clear") # Bildschim sauber machen
	spielfeld[aktPos[0]][aktPos[1]] = " "
	if ein == "a" or ein == "A":
		aktPos[1] = (aktPos[1]-1)%8
		print("X Richtung: ", aktPos[0],aktPos[1])
	elif ein == "d" or ein == "D":
		aktPos[1] = (aktPos[1]+1)%8
		print("X Richtung: ", aktPos[0],aktPos[1])
	elif ein == "w" or ein == "W":
		aktPos[0] = (aktPos[0]-1)%8
		print("Y Richtung: ", aktPos[0],aktPos[1])
	elif ein == "s" or ein == "S":
		aktPos[0] = (aktPos[0]+1)%8
		print("Y Richtung: ", aktPos[0],aktPos[1])
	elif ein == "x" or ein == "X":
		ein = "x"
		print("ByeBye!....")
		sys.exit(0)
	else:
		print("Falsche Eingabe!")
    #Spielfeld immer neu zeichen
	spielfeld[aktPos[0]][aktPos[1]] = "X"
	print("-----------------------------")
	for i in range(8):
		print(" | ".join(spielfeld[i]))
	print("-----------------------------")
        
