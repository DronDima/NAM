import numpy as np
np.set_printoptions(precision = 4)

nodes = np.zeros(11)
h = np.pi/4/10

for i in range(11):
    nodes[i] = 0 + i*h

x1 = nodes[0] + h / 2.6
x2 = nodes[5] + h / 2.6
x3 = nodes[9] + h / 2.6

def f(x):
    return 1.8 * np.power(np.e, -x) - 0.8 * np.tan(x)

def mul(x, k):
    result = 1
    for i in range(k+1):
        result *= x-nodes[i]
    return result

def P(x, DD):
    result = 0
    for i in range(1, 12):
        result += DD[0, i] * mul(x, i-2)
    return result

def w(x):
    result = 1
    for i in range(11):
        result *= x-nodes[i]
    return result

def r(x):
    nodesWithX = np.insert(nodes, 0, x)
    DDWithX = np.zeros((12, 13))
    for i in range(12):
        DDWithX[i, 0] = nodesWithX[i]
        DDWithX[i, 1] = f(nodesWithX[i])

    col = 2
    for i in range(11, -1, -1):
        for j in range(i):
            DDWithX[j, col] = (DDWithX[j + 1, col - 1] - DDWithX[j, col - 1]) / (DDWithX[j + 12 - i, 0] - DDWithX[j, 0])
        col += 1

    return w(x)*DDWithX[0,12]


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
    print("|f-P| = ", res1)
    print("r(x) = ", r(x1))
    print("///////////////")
    print("x** = ", x2)
    print("f = ", f(x2))
    print("fi = ", P(x2, DD))
    print("|f-P| = ", res2)
    print("r(x) = ", r(x2))
    print("///////////////")
    print("x*** = ", x3)
    print("f = ", f(x3))
    print("fi = ", P(x3, DD))
    print("|f-P| = ", res3)
    print("r(x) = ", r(x3))
    print("max |f-P|= ", np.max(np.array([res1, res2, res3])))
    print("max r(x) = ", np.max(np.array([r(x1), r(x2), r(x3)])))
    print("///////////////")

interNewton(nodes)