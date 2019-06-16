import numpy as np
np.set_printoptions(precision = 4)
N = 11
nodes = np.zeros(N)
h = np.pi/4/10

for i in range(11):
    nodes[i] = 0 + i*h

x1 = nodes[0] + h / 2.6
x2 = nodes[5] + h / 2.6
x3 = nodes[9] + h / 2.6

def f(x):
    return 1.8 * np.power(np.e, -x) - 0.8 * np.tan(x)

def l(i, x):
    result = 1
    for j in range(N):
        if(i != j):
            result *= (x - nodes[j])/(nodes[i] - nodes[j])
    return result

def L(x):
    result = 0
    for i in range(N):
        result += f(nodes[i])*l(i, x)
    return result

def w(x):
    result = 1
    for i in range(11):
        result *= x-nodes[i]
    return result

def f12Shtrix(x):
    return 1.8*np.e**(-x) - 3.83201*10**8*np.tan(x)**13 - 1.66054*10**9*np.tan(x)**11 - 2.87827*10**9*np.tan(x)**9 - 2.5198*10**9*np.tan(x)**7 - 1.14885*10**9*np.tan(x)**5 - 2.47869*10**8*np.tan(x)**3 - 1.78946*10**7*np.tan(x)

def r(x, ksi):
    return f12Shtrix(ksi)*w(x)/np.math.factorial(N+1)


print("///////////////")
res1 = np.abs(f(x1) - L(x1))
res2 = np.abs(f(x2) - L(x2))
res3 = np.abs(f(x3) - L(x3))
print("x* = ", x1)
print("f = ", f(x1))
print("fi = ", L(x1))
print("|f-L| = ", res1)
print("r(x, ksi) = ", r(x1, np.pi/4/2))
print("///////////////")
print("x** = ", x2)
print("f = ", f(x2))
print("fi = ", L(x2))
print("|f-L| = ", res2)
print("r(x, ksi) = ", r(x2, np.pi/4/2))
print("///////////////")
print("x*** = ", x3)
print("f = ", f(x3))
print("fi = ", L(x3))
print("|f-L| = ", res3)
print("r(x, ksi) = ", r(x3, np.pi/16))
print("r(x, ksi) = ", r(x3, np.pi/8))
print("r(x, ksi) = ", r(x3, np.pi*3/16))
print("max = ", np.max(np.array([res1, res2, res3])))
print("///////////////")