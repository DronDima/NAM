import math
eps = 0.0000000001


def f(x):
    return x**5 - 3*x**2 + 1
def fShtrix(x):
    return 5*x**4-6*x
def method(x):
    X = x - f(x)/fShtrix(x)
    count = 0
    while(math.fabs(X-x) > eps):
        x = X
        X = X - f(X) / fShtrix(X)
        count+=1
    print("X: ", X)
    print("Iterations count: ", count)
    print("Residual: ", f(X))

method(1.35)