import math

def function(x):
    return math.sin(math.cos(2 * x * x + 1))

def find_c(a, b):
    try:
        return a - (a - b)/(function(b)-function(a))*function(a)
    except ZeroDivisionError:
        return 0

def sign(x):
    return 1 if x > 0 else -1

def search(bracket, precision):
    a, b = bracket
    c = find_c(a, b)
    ## if function(c) is smaller than precision
    search = 1/function(c) > 1 / precision
    while not search:
        if sign(function(a)) == sign(function(b)):
            a = c
        else:
            b = c
        c = find_c(a, b)
    print(function(c), c)

search((0,1), 0.0001)