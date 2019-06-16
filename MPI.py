import math
eps = 0.0000000001
x0 = 0.8
y0 = 0.1

def f1(x,y):
    return y - 0.5*x**2 + x - 0.5
def f2(x,y):
    return 2*x + y - (y**3)/6 - 1.6
def fi1(x,y):
    return y**3/3+0.8-y/2
def fi2(x,y):
    return 0.5*x**2-x+0.5
def method(x, y):
    X = fi1(x,y)
    Y = fi2(x,y)
    count = 0
    while(max(math.fabs(X-x), math.fabs(Y-y)) > eps):
        x = X
        y = Y
        X = fi1(x,y)
        Y = fi2(x,y)
        count+=1
    print("X: ", X)
    print("Y: ", Y)
    print("Iterations count: ", count)
    print("Residual 1: ", f1(X,Y))
    print("Residual 2: ", f2(X,Y))

method(x0, y0)