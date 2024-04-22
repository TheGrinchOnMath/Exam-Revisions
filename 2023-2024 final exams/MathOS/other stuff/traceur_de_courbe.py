from tkinter import *
from math import *
fen = Tk() #fenêtre graphique
#dimensions de la fenêtre graphique
LX = 1000
LY = 500
zerolist = [] #liste des zéros
zerolist2 = [] #liste des zéros probables
xlist = ['- 400', '-300', '-200', '-100', '0', '100', '200', '300', '400'] #graduation x
ylist = [ '200', '100', '0', '-100', '-200'] #graduation y
def add(x) : #fonction d'addition en boucle qui évite les valeurs parasites
    x = x + 0.01
    x = round(x, 2)
    return x
def f(x) : #fonction qui pour un x associe son image par la fonction f(x)
    try :
        y = 100/x
        if y == 0 : #test si il y a un zéro
            zerolist.append(x)
        return y
    except ZeroDivisionError : #sécurité si division par zéro
        return float(10**5)
    except TypeError : #sécurité si problème de racine de nbr négatif
        return float(10**5)
def signe(w) : #fonction qui retourne le signe d'un nombre
    if w >= 0 :
        return '+'
    elif w < 0 :
        return '-'
can = Canvas(fen, bg='white', width=LX, height=LY) #espace où on va dessiner (centré à gauche)
can2 = Canvas(fen, bg='white', width=LX/2, height=LY) #espace où on affiche les zeros (centré à droite)
can.pack(side=LEFT)
can2.pack(side=RIGHT)
for i in range(100) : #cadrillage x
    can.create_line(0, 10*i, LX, 10*i, width=1, fill='gray75')
for i in range(100) : #cadrillage y
    can.create_line(10*i, 0, 10*i, LY, width=1, fill='gray75')
#graduation de l'axe x
for i in range(len(xlist)) :
    can.create_text( 100*i + 100 , LY/2 - 10, text=str(xlist[i]))
#graduation de l'axe y
for i in range(len(ylist)) :
    can.create_text( LX/2 - 10, 100*i + 50, text=str(ylist[i]))
#axe x
can.create_line(0, LY/2, LX, LY/2, width=1, fill='black')
#axe y
can.create_line(LX/2, 0, LX/2, LY, width=1, fill='black')
x = 0
while x <= LX : #on trace la courbe
    can.create_line(x, -f(x-500) + 250, x+1, -f(x-500)+251, width=1, fill='blue')
    if signe(f(x)) != signe(f(add(x))) : #test s'il y a un changement dde signe (donc un zéro)
        zerolist2.append((x, add(x)))
    x = add(x)
if x >= LX : #affichage des listes des zéros
    can2.create_text(LX/4, 20, text=str(list(set(zerolist))))
    can2.create_text(LX/4, 40, text='il peut y avoir des zéros vers ces x :')
    can2.create_text(LX/4, 60, text=str(list(set(zerolist2))))
fen.mainloop()
