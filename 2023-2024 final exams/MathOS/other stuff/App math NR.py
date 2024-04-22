def fct(x) :
    x = pow(x,3)-pow(x,2) + 1
    return x

def fct_derive(x):
    x = 3*pow(x,2)-2*x
    return x

x = 10

ok = False
while not ok:
    z = x
    x1 = x-(fct(x)/fct_derive(x))
    print(x1)
    x = x1
    if x1==z :
        ok = True
print(x)




