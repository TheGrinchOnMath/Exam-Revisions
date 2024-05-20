import math

#dans les commentaires les # sont pour expliquer ce que l'on fait et les """ sont utilises pour donner les limites du code

#on definit bords, où -bords et bords serons les bornes de l'intervale initiale dans lequel nous allos chercher nos zeros de fonction
bords = float(2000.0)
#ici on definit la fonction que l'on veut analyser
def f(num):

    return ((num-20)*(num-0.1)*(num-0.102)*((num-4.11)**2)) #fonction qui montre les cas limites, que ce bracketing ne trouve pas"""
    ##return ((num-98)*(num-13)*(num-2001)*(num-380.2)*(num-69.4266218726)*(num+0.1)*(num+0.1)*(num+0.2))
#on definit  la fonction sign qui donne 1 ou -1 suivant le sign du nombre que nous analysons
def sign(x): math.copysign(1, x)

#zeros est la liste des zeros trouvees
zeros = []

#on donne a combien de decimales nous allons chercher des zeros
arondi = 10

#on definit une fonction qui peut additionner des nombres a virgule sans avoir des valeurs parasitaires que l'on a si lon arondi pas
def add(num,b):
    num = num+b
    #round est une fonction de base de python qui arondi le nombre(num) a x-1 (ici arondi donc 10-1 car apres des donnees parasitaires s'incrustent) de decimales
    num = round(num, arondi)
    return num


#on definit la donction boucle qui cherche le changement de signes dans un intervale donne
#elle accepte le debut de l'intervale(start), sa fin(stop) et la distance entre chaque etapes(pas)
#on veut qu'elle sorte, les valeurs qu'elle trouve comme zeros et les valeurs qui ont un zeros peu apres
def boucle(start, stop, pas):
    utile=[]
    while start <= stop:
        #met la valeur dans le groupe contenant les zeros de la fonction si la valeur start en est une
        if f(start)== 0 :
            zeros.append(start)
        #fait la meme chose pour la valeur stop
        if f(stop)==0 :
            zeros.append(stop)
        #compare le signe entre une valeur et une valeur juste apres et:
        #soit passe a la prochaine valeur si elle on le meme signe,
        #soit met la premiere valeur dans une liste pour la garder puis continue avec la prochaine etape
        if sign(f(start)) == sign(f(add(start,pas))) :
            start = add(start, pas)
        if sign(f(start)) != sign(f(add(start,pas))) :
            utile.append(start)
            start=add(start,pas)
    return utile
    #utile est le groupe contenant les valeurs avec un zero peut apres, elles seront utilisees pour definir un intervale plus precis

"""il ne faut pas que r soit plus grand que arrondi"""

def cherche(r):
    #fait un premier scan dans l'intervale initiale afin de trouver les valeur où le signe change avec un certain taux de precision(ici 0.1)
    utile2=boucle(-bords,bords,0.1)

    for y in range(r):
        #fait une sauvegarde de utile2
        utile1=utile2
        #vide utile2 afin de le reremplir avec des valeurs plus precises
        utile2=[]
        for x in utile1:
            #utilise utile1 pour trouver des valeurs plus precises
            utile2=utile2+boucle(x,x+10**(-y),10**(-y-1))
    print ('les valeurs les plus proche de zeros trouvees sont:', utile1)

cherche(10)

zeros = list(set(zeros))
print('les zeros trouves sont:', zeros)
