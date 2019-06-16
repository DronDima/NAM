import numpy as np
np.set_printoptions(precision = 4)
nodes = np.zeros(11)
h = np.pi/4/10

for i in range(11):
    nodes[i] = 0 + i*h

x1 = nodes[0] + h / 2.6
x2 = nodes[5] + h / 2.6
x3 = nodes[9] + h / 2.6

def sum(i, j):
    result = 0
    for k in range(11):
        result += np.power(nodes[k], i)*np.power(nodes[k], j)
    return result

def sumF(i):
    result = 0
    for k in range(11):
        result += np.power(nodes[k], i) * (1.8*np.power(np.e, -nodes[k])-0.8*np.tan(nodes[k]))
    return result

def f(x):
    return 1.8*np.power(np.e, -x) - 0.8*np.tan(x)

def fi(x, c, n):
    result = 0
    for i in range(n):
        result += c[i]*np.power(x, i)
    return result

def minimalSquares(n):
    S = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            S[i, j] = sum(i, j)

    b = np.zeros(n)
    for i in range(n):
        b[i] = sumF(i)
    c = np.linalg.solve(S, b)
    print("///////////////")
    print("n = ", n)
    res1 = np.abs(f(x1) - fi(x1, c, n))
    res2 = np.abs(f(x2) - fi(x2, c, n))
    res3 = np.abs(f(x3) - fi(x3, c, n))
    print("x* = ", x1)
    print("f = ", f(x1))
    print("fi = ", fi(x1, c, n))
    print("|f-fi| = ", res1)
    print("///////////////")
    print("x** = ", x2)
    print("f = ", f(x2))
    print("fi = ", fi(x2, c, n))
    print("|f-fi| = ", res2)
    print("///////////////")
    print("x*** = ", x3)
    print("f = ", f(x3))
    print("fi = ", fi(x3, c, n))
    print("|f-fi| = ", res3)
    print("max = ", np.max(np.array([res1, res2, res3])))
    print("///////////////")
    return np.max(np.array([res1, res2, res3]))
minimalSquares(6)

# results = np.zeros(130)
# for i in range(2, 132, 1):
#     results[i-2] = minimalSquares(i)

# minIndex = results.argmin()
# print(minIndex+2)
# print(results[minIndex])
