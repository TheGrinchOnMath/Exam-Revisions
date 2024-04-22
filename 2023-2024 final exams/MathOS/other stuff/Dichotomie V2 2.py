from math import *
#listes des intervalles créés
interlist = []
interlist2 = []
def add(x) : #fonction d'addition en boucle qui évite les valeurs parasites
    x = x + 1
    x = round(x, 2)
    return x
def f(x) : #fonction qui pour un x associe son image par la fonction f
    try :
        y = (x - 24) * (x + 24)
        return y
    except ZeroDivisionError : #sécurité si division par zéro
        return float(10**5)
    except TypeError : #sécurité si problème de racine de nbr négatif
        return float(10**5)
def test(g, d) : #fonction qui teste si le signe des bornes est le même ou pas
    if f(g)*f(d) > 0 :
        return False
    else :
        return True
def intercut(g,d) : #adapte l'intervalle en fonction des signes
    m = (g+d)/2
    inter = [g,d]
    if f(g)*f(m) > 0 :
        inter = [m ,d]
        #print(inter)
    elif f(d)*f(m) >= 0 :
        inter = [g, m]
        #print(inter)
    return inter
def geninter(g, d) : #fonction qui génère des petits intervalles à partir des bornes choisies intervalles
    while g <= d :
        interlist.append(g)
        g = add(g)
    return interlist
#===================================
#bornes de l'intervalle et précision désirée
ga = -1000
dr = 1000
pr = 0.01
geninter(ga,dr) #on génère des petits intervalles en fonction des bornes gauches et droites de l'intervalle souhaité
for i in range(len(interlist) - 1) :
    n_inter = [interlist[i], interlist[i + 1]]
    #print(type(f(n_inter[0])), type(f(n_inter[1])))
    #on vérifie que les images des bornes des petits intervalles sont des nombres réels ou entiers
    if type(f(n_inter[0])) == float and type(f(n_inter[1])) == float or type(f(n_inter[0])) == int and type(f(n_inter[1])) == int:
        while abs(n_inter[0] - n_inter[1]) > pr : #on applique la fonction "intercut" (dichotomie) jusqu'à la précision voulue
            n_inter = intercut(n_inter[0], n_inter[1])
            if abs(n_inter[0] - n_inter[1]) < pr :
                #print(f(n_inter[0]), n_inter[0], f(n_inter[1]), n_inter[1])
                if abs(f(n_inter[0])) < pr or abs(f(n_inter[1])) < pr : #si les images sont proches de 0, ce sont des zéros probables et on les mets dans une liste
                    interlist2.append(n_inter)
                    break
print("il y a", len(interlist2), "zéros probables qui sont dans ces intervalles :", interlist2)


