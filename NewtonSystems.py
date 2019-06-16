import math
eps = 0.0000000001

def F1(x,y):
    return 2-y**2
def F2(x,y):
    return -2
def F3(x,y):
    return -4
def F4(x,y):
    return 2-2*x
def f1(x, y):
    return y-0.5*x**2+x-0.5
def f2(x, y):
    return 2*x+y-(y**3)/6-1.6
def znam(x, y):
    return x*y**2-2*x-y**2-2

def method(x, y):
    X = x - (F1(x, y)*f1(x, y)+F2(x, y)*f2(x, y))/znam(x, y)
    Y = y - (F3(x, y)*f1(x, y)+F4(x, y)*f2(x, y))/znam(x, y)
    count = 0
    while(max(math.fabs(X-x), math.fabs(Y-y))):
        x = X
        y = Y
        X = x - (F1(x, y) * f1(x, y) + F2(x, y) * f2(x, y)) / znam(x, y)
        Y = y - (F3(x, y) * f1(x, y) + F4(x, y) * f2(x, y)) / znam(x, y)
        count+=1
    print("X: ", X)
    print("Y: ", Y)
    print("Iterations count: ", count)
    print("Residual 1: ", f1(X, Y))
    print("Residual 2: ", f2(X, Y))

method(0.8, 0.1)