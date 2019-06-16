import math
eps = 0.0000000001

def f1(x, y):
    return y-0.5*x**2+x-0.5
def f2(x, y):
    return 2*x+y-(y**3)/6-1.6

def method(x, y):
    X = x - (-0.55*f1(x, y)+0.56*f2(x, y))
    Y = y - (1.11*f1(x, y)-0.11*f2(x, y))
    count = 0
    while(max(math.fabs(X-x), math.fabs(Y-y))):
        x = X
        y = Y
        X = x - (-0.55 * f1(x, y) + 0.56 * f2(x, y))
        Y = y - (1.11 * f1(x, y) - 0.11 * f2(x, y))
        count+=1
    print("X: ", X)
    print("Y: ", Y)
    print("Iterations count: ", count)
    print("Residual 1: ", f1(X, Y))
    print("Residual 2: ", f2(X, Y))

method(0.8, 0.1)