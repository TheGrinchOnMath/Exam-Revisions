# import math

# the output of this funciton is the one that is being solved for
def function(x):
    return x**5 - x**2 - 1
    # return math.sin(math.cos(2 * x * x + 1))


bracket = (0, 2)
DIFFERENCE = 0.0001


def new_value(a, b):
    return (a + b) / 2


def sign(x):
    return 1 if x > 0 else -1


def dichotomy_search(DIFFERENCE, bracket):
    a, b = bracket
    step = function(new_value(a, b))
    while abs(a - b) > DIFFERENCE:
        if sign(step) != sign(function(a)):
            b = new_value(a, b)
        else:
            a = new_value(a, b)
        step = function(new_value(a, b))
        print(step)
    print(a, b, "\n", function(a), function(b))


dichotomy_search(DIFFERENCE, bracket)
