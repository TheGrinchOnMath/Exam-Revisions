def lignes_fonctions(nom_fonctions: str):
    f = open(nom_fonctions + ".py", "r")
    Taxt = f.read()
    ligne = ""
    lignes = []
    for x in Taxt:
        ligne = ligne + x
        if x == "\n" and not ligne == "def launch():" and not ligne == "launch()":
            lignes.append(ligne)
            ligne = ""
    return lignes


def create_text_function_window(function_name: str):
    fen2 = Tk()
    fen2.title(function_name)
    fen2.geometry("1000x350")
    fen.resizable(False, True)
    titre_fonction = Label(
        fen2,
        width=1000,
        text="code de " + function_name,
        font="Georgia 15",
        bg="#328563",
        fg="white",
    )
    titre_fonction.pack()
    scrollbar = Scrollbar(fen2, bg="#328563")
    scrollbar.pack(side=RIGHT, fill=Y)
    le_texte = Listbox(
        fen2,
        yscrollcommand=scrollbar.set,
        width=1000 - 16,
        bg="#2E2E2E",
        fg="white",
        font="Arial 12",
    )
    lignes = lignes_fonctions(function_name)
    for x in lignes:
        le_texte.insert(END, x)
    le_texte.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=le_texte.yview)
    fen2.mainloop()


def button_1():
    import bracketing

    bracketing
    create_text_function_window("bracketing")


def button_2():
    import dichotomie

    dichotomie
    create_text_function_window("dichotomie")


def button_3():
    import regula_falsi

    regula_falsi
    create_text_function_window("regula_falsi")


def button_4():
    import newton_raphson

    newton_raphson
    print("WU")
    create_text_function_window("newton_raphson")


def button_5():
    import secante

    secante
    create_text_function_window("secante")


def button_6():
    import traceur_de_courbe

    traceur_de_courbe
    create_text_function_window("traceur_de_courbe")


# Ici se trouve l'interface graphique (normalement les noms sont assez clair pour que vous comprenniez le code)
from tkinter import *


def la_grille(largeur, hauteur, nombres_de_cases):
    def calcul_grille(axe, add):
        grille = []
        x = 0
        while not x >= axe + add:
            grille.append(x)
            x += add
        return grille

    grille_x = calcul_grille(largeur, largeur / nombres_de_cases)
    grille_y = calcul_grille(hauteur, hauteur / nombres_de_cases)
    return grille_x, grille_y


fen = Tk()
hauteur = 650
largeur = 650
fen.geometry(str(largeur) + "x" + str(hauteur))
fen.resizable(FALSE, FALSE)
fen.title("trouvage de zéro")
canvas = Canvas(fen, width=largeur, height=hauteur, bg="white")
canvas.pack()

grille_x, grille_y = la_grille(largeur, hauteur, 30)
LA_GRILLE = []
for i in range(len(grille_x)):
    LA_GRILLE.append([grille_x[i], grille_y[i]])


def uwu(i):
    mouse_x = i.x
    mouse_y = i.y
    # print(mouse_x,mouse_y)
    canvas.delete("all")
    posx, posy = False, False
    for x in range(len(LA_GRILLE) - 1):
        if mouse_x >= LA_GRILLE[x][0] and mouse_x < LA_GRILLE[x + 1][0]:
            posx = [LA_GRILLE[x][0], LA_GRILLE[x + 1][0]]
        if mouse_y >= LA_GRILLE[x][1] and mouse_y < LA_GRILLE[x + 1][1]:
            posy = [LA_GRILLE[x][1], LA_GRILLE[x + 1][1]]
        if not posx == False and not posy == False:
            canvas.create_rectangle(
                posx[0], posy[0], posx[1], posy[1], fill="#82AEA5", outline="#82AEA5"
            )
            break


fen.bind("<Motion>", uwu)


Barre_du_haut = Label(
    fen,
    text="Quelle méthode voulez-vous utiliser ?",
    font="Georgia 18",
    fg="white",
    bg="#528A80",
    height=3,
    width=int(largeur / 9),
).place(in_=canvas, x=-180)
button_1 = Button(
    fen,
    text="Bracketing",
    font="Georgia 12",
    bg="#B1EAE2",
    height=4,
    width=16,
    relief=GROOVE,
    command=button_1,
)
button_1.place(in_=canvas, x=largeur * 3 / 16, y=hauteur * 3 / 16 + 30)
button_2 = Button(
    fen,
    text="Dichotomie",
    font="Georgia 12",
    bg="#B1EAE2",
    height=4,
    width=16,
    relief=GROOVE,
    command=button_2,
)
button_2.place(in_=canvas, x=largeur * 10 / 16, y=hauteur * 3 / 16 + 30)
button_3 = Button(
    fen,
    text="Regula falsi",
    font="Georgia 12",
    bg="#B1EAE2",
    height=4,
    width=16,
    relief=GROOVE,
    command=button_3,
)
button_3.place(in_=canvas, x=largeur * 3 / 16, y=hauteur * 7 / 16 + 30)
button_4 = Button(
    fen,
    text="Newton-Raphson",
    font="Georgia 12",
    bg="#B1EAE2",
    height=4,
    width=16,
    relief=GROOVE,
    command=button_4,
)
button_4.place(in_=canvas, x=largeur * 10 / 16, y=hauteur * 7 / 16 + 30)
button_5 = Button(
    fen,
    text="Sécante",
    font="Georgia 12",
    bg="#B1EAE2",
    height=4,
    width=16,
    relief=GROOVE,
    command=button_5,
)
button_5.place(in_=canvas, x=largeur * 3 / 16, y=hauteur * 11 / 16 + 30)
button_6 = Button(
    fen,
    text="Traceur de courbe",
    font="Georgia 12",
    bg="#B1EAE2",
    height=4,
    width=16,
    relief=GROOVE,
    command=button_6,
)
button_6.place(in_=canvas, x=largeur * 10 / 16, y=hauteur * 11 / 16 + 30)


fen.mainloop()
