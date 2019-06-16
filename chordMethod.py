import math
eps = 0.0000000001


def f(x):
    return x**5 - 3*x**2 + 1
def method(x, x0):
    X = x - f(x)*(x-x0)/(f(x)-f(x0))
    count = 0
    while(math.fabs(X-x) > eps):
        x = X
        X = x - f(x)*(x-x0)/(f(x)-f(x0))
        count+=1
    print("X: ", X)
    print("Iterations count: ", count)
    print("Residual: ", f(X))

method(1.35, 1.3)
