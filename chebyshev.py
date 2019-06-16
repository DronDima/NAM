import numpy as np
np.set_printoptions(precision = 4)

a = 0
N = 11
b = np.pi/4
n = 11
nodes = np.zeros(11)
h = np.pi/4/10

for i in range(11):
    nodes[i] = 0 + i*h

x1 = nodes[0] + h / 2.6
x2 = nodes[5] + h / 2.6
x3 = nodes[9] + h / 2.6

for k in range(11):
    nodes[k] = (a+b)/2 +(b-a)*(np.cos((2*k+1)*np.pi/(2*n+2)))/2

def f(x):
    return 1.8 * np.power(np.e, -x) - 0.8 * np.tan(x)

def mul(x, k):
    result = 1
    for i in range(k+1):
        result *= x-nodes[i]
    return result

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

def P(x, DD):
    result = 0
    for i in range(1, 12):
        result += DD[0, i] * mul(x, i-2)
    return result

def r():
    return np.power(np.pi/4, 12)/np.math.factorial(12)/2**(2*12+1)

def interNewton(nodes):
    DD = np.zeros((11, 12))
    for i in range(11):
        DD[i, 0] = nodes[i]
        DD[i, 1] = f(nodes[i])

    col = 2
    for i in range(10, -1, -1):
        for j in range(i):
            DD[j, col] = (DD[j + 1, col - 1] - DD[j, col - 1]) / (DD[j + 11 - i, 0] - DD[j, 0])
        col += 1

    print("Divided differences: ", DD[0, :])
    print("///////////////")
    res1 = np.abs(f(x1) - P(x1, DD))
    res2 = np.abs(f(x2) - P(x2, DD))
    res3 = np.abs(f(x3) - P(x3, DD))
    print("x* = ", x1)
    print("f = ", f(x1))
    print("fi = ", P(x1, DD))
    print("|f-fi| = ", res1)
    print("///////////////")
    print("x** = ", x2)
    print("f = ", f(x2))
    print("fi = ", P(x2, DD))
    print("|f-fi| = ", res2)
    print("///////////////")
    print("x*** = ", x3)
    print("f = ", f(x3))
    print("fi = ", P(x3, DD))
    print("|f-fi| = ", res3)
    print("max = ", np.max(np.array([res1, res2, res3])))
    print("///////////////")

def interLagrange(nodes):
    print("///////////////")
    res1 = np.abs(f(x1) - L(x1))
    res2 = np.abs(f(x2) - L(x2))
    res3 = np.abs(f(x3) - L(x3))
    print("x* = ", x1)
    print("f = ", f(x1))
    print("fi = ", L(x1))
    print("|f-fi| = ", res1)
    print("///////////////")
    print("x** = ", x2)
    print("f = ", f(x2))
    print("fi = ", L(x2))
    print("|f-fi| = ", res2)
    print("///////////////")
    print("x*** = ", x3)
    print("f = ", f(x3))
    print("fi = ", L(x3))
    print("|f-fi| = ", res3)
    print("max = ", np.max(np.array([res1, res2, res3])))
    print("///////////////")

interNewton(nodes)
print(r())
# interLagrange(nodes)