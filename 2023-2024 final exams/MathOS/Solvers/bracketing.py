import math


BOUND = float(4000)
ZEROS = []  # all zeros will be added to this list
PRECISION = 10


def sign(x):
    math.copysign(1, x)


def f(num):
    return ((num-98)*(num-13)*(num-2001)*(num-380.2)*(num-69.4266218726)*(num+0.1)*(num+0.1)*(num+0.2))


def add(num1, num2):
    num1 += num2
    num = round(num1, PRECISION)
    return num


def loop(start, stop, step):
    zero_close = []
    while start <= stop:
        ZEROS.append(start) if f(start) == 0 else None
        ZEROS.append(stop) if f(stop) == 0 else None

        inter = add(start, step)
        start_sgn = sign(f(start))
        inter_sgn = sign(f(inter))

        if start_sgn == inter_sgn:
            start = inter
        else:
            zero_close.append(start)
            start = inter

    return zero_close


def search(r):
    zeros = loop(-BOUND, BOUND, 0.1)
    for i in range(r):
        _list = zeros
        zeros = []
        for j in _list:
            zeros = zeros + loop(j, j + 10 ** (-i), 10 ** (-i - 1))
        print(f'closest values to zero are: {zeros}')

search(10)
ZEROS = list(set(ZEROS))
print(f"found zeros are: {ZEROS}")