def fct(x):
    x = pow(x,3)-pow(x,2) + 1
    return x

def fct_derive(x):
    x = 3*pow(x,2)-2*x
    return x

x = 10
x_actuel = x-(fct(x)/fct_derive(x))
x_precedent = x

vrai = False
while not vrai:
    z = x_actuel
    x1 = x_actuel - ((x_actuel-x_precedent)/(fct(x_actuel)-fct(x_precedent)))*fct(x_actuel)
    print(x1)
    x_precedent = x_actuel
    x_actuel = x1
    if x1==z :
        vrai = True
print(x1)
