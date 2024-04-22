def fct(x):
    return pow(x,3)-pow(x,2)+1

#il nous faut d'abord un x et un xn-1 on peut trouver le xn-1 grâce à la méthode de Newton Raphson

def fct_der(x):
    return 3*x**2-2*x

x = 5
xn = x-(fct(x)/fct_der(x))
xn_1 = x

ok = False
while ok == False :
    x1 = xn-((xn-xn_1)/(fct(xn)-fct(xn_1)))*fct(xn)
    if xn == x1:
        ok = True
    xn_1 = xn
    xn = x1
print("le zero/un des zeros est :" ,x)
