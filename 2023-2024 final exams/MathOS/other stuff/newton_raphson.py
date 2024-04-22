def fct(x):
    return pow(x,3)-pow(x,2)+1
def fct_der(x):
    return 3*x**2-2*x

x = 5
ok = False
while ok == False :
    z = x
    x1 = x-(fct(x)/fct_der(x))
    x = x1
    if z == x1:
        ok = True

print("le zero/un des zeros est :" ,x)
