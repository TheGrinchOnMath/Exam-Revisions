import math  

def signum (x):
    if x >0 :
        return 1
    elif x <0 :
        return -1
    else :
        return 0

def fonctiondebase(x):
    x = (x-2)#(x**2+1)*(x+7)
    return x

def intervalle(borne_gauche,largeur,borne_sup):    # retourne le premier moment ou le signe de la fonction change
    uwu = 0
    try :
        while not borne_gauche >= borne_sup:
            borne_droite = borne_gauche + largeur
            if signum(fonctiondebase(borne_gauche))!=signum(fonctiondebase(borne_droite)):
                return [borne_gauche,borne_droite]              #return une LISTE
            borne_gauche = borne_droite
            uwu += 1
    except TypeError :
        print("il n'y a pas de zeros dans cette fonction",str(uwu))

def ladroite(petite_borne_gauche,petite_borne_droite):
    a = petite_borne_gauche                                        # pour avoir le meme calcul que sur la feuille
    b = petite_borne_droite
    c = a - ((b-a)/(fonctiondebase(b) - fonctiondebase(a))) * fonctiondebase(a)                    # c c'est comme sur la feuille le point d'intersection sur l'axe x
    return c

def laboucle(petite_borne_gauche,petite_borne_droite):
    global elzero
    c = ladroite(petite_borne_gauche,petite_borne_droite)    # c'est le nouveau c
    try :
        if fonctiondebase(petite_borne_droite) == 0:               # on test si le zero se trouve pas sur un de ces 3 elements
            print("le zero vaut", petite_borne_droite)
            elzero = petite_borne_droite
            return petite_borne_droite
        elif fonctiondebase(petite_borne_gauche)== 0 :
            print("le zero vaut", petite_borne_gauche)
            elzero = petite_borne_gauche
            return petite_borne_gauche
        elif fonctiondebase(c) == 0 :
            print("le zero vaut", c)
            el_zero_mouchachos = c
            return c
        if fonctiondebase(petite_borne_droite) == c or fonctiondebase(petite_borne_gauche) == c: #si le zero se trouve soit a gauche ou a droite de la droite OU si le zero est egale a la borne on a trouve le zero et on stop
            return c
        elif abs(petite_borne_gauche-petite_borne_droite) <= degree_precision_intervalle_boucle: #norme (valeur exclusivement positive) de la difference entre borne gauche et borne droite
            print("Le zero se situe entre", petite_borne_gauche,petite_borne_droite)
            return
        if signum(fonctiondebase(c))== signum(fonctiondebase(petite_borne_gauche)) :
            laboucle(c,petite_borne_droite)                         # a cette etape le c devient le nouveau a si ils ont le meme signe
        if signum(fonctiondebase(c))== signum(fonctiondebase(petite_borne_droite)) :
            laboucle(petite_borne_gauche,c)         # a cette etape le c devient le nouveau b si ils ont le meme signe
    except TypeError :
        print("il n'y a pas de zeros dans cette fonction")


#a fixer par l'utilisateur


borne_inf = -1000
borne_sup = 1000
precision = 500
degree_precision_intervalle_boucle = 3 *pow(10,-1)

largeur = (borne_sup - borne_inf) / precision  #largeur d'un intervalle selon la precision


petite_borne_gauche = intervalle(borne_inf,largeur,borne_sup)[0] # le premier [0] element de la liste est la borne Gauche
petite_borne_droite = intervalle(borne_inf,largeur,borne_sup)[1]  # le deuxieme [1] element de la liste est la borne Droite
while petite_borne_droite < borne_sup:
    laboucle(petite_borne_gauche,petite_borne_droite)
    petite_borne_gauche = petite_borne_droite
    petite_borne_droite = petite_borne_droite+precision
    nouveau_intervalle = intervalle(petite_borne_gauche,largeur,borne_sup)
    if nouveau_intervalle == None:
        break
    petite_borne_gauche = nouveau_intervalle[0]
    petite_borne_droite = nouveau_intervalle[1]
    