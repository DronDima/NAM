import math
eps = 0.0000000001
m = 0.001
q = 0.5
x0 = 1.35

def f(x):
    return x**5 - 3*x**2 + 1
def fi(x):
    return (3*x**2-1)**0.2
def priorEstimate(m, q):
    return math.trunc(math.log10((eps*(1-q)/m))/math.log10(q) + 1)
def method(m, q, x):
    X = fi(x)
    count = 0
    while(math.fabs(X-x) > eps):
        x = X
        X = fi(X)
        count+=1
    print("X: ", X)
    print("Iterations count: ", count)
    print("Residual: ", f(X))


method(m, q, x0)
print("Prior estimate: ", priorEstimate(m, q))