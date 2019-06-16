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

def mul(t, k):
    result = 1
    for i in range(k+1):
        result *= t+i
    return result

def P(x,FD):
    result = 0
    t = (x-nodes[10])/h
    j = 0
    for i in range(10,4, -1):
        a = FD[i, j]
        result += FD[i, j]*mul(t, j-1)/np.math.factorial(j)
        j += 1
    return result

# n9 = nodes[9]
# n10 = nodes[10]
# h = (nodes[10] - nodes[9])/10
# for i in range(11):
#     nodes[i] = n9 + i*h
FD = np.zeros((11, 11))
for i in range(11):
    FD[i, 0] = f(nodes[i])

col = 1
for i in range(10, -1, -1):
    for j in range(i):
        FD[j, col] = FD[j + 1, col - 1] - FD[j, col - 1]
    col += 1

def f4shtr(x):
    return 0.119366*np.e**(-0.587787*x) - 12.8*(1/np.cos(x))**4*np.tan(x) - 6.4*(1/np.cos(x))**2*np.tan(x)**3

def r(x):
    t = (x - nodes[10]) / h
    print((nodes[10] + nodes[9])/2)
    ksi = (nodes[10] + nodes[9])/2
    return np.power(h, 4)*mul(t, 3)/np.math.factorial(4)*f4shtr(ksi)


print("///////////////")
res1 = np.abs(f(x1) - P(x1, FD))
res2 = np.abs(f(x2) - P(x2, FD))
res3 = np.abs(f(x3) - P(x3, FD))
print("x* = ", x1)
print("f = ", f(x1))
print("fi = ", P(x1, FD))
print("|f-P| = ", res1)
print("///////////////")
print("x** = ", x2)
print("f = ", f(x2))
print("fi = ", P(x2, FD))
print("|f-P| = ", res2)
print("///////////////")
print("x*** = ", x3)
print("f = ", f(x3))
print("fi = ", P(x3, FD))
print("|f-P| = ", res3)
print("max = ", np.max(np.array([res1, res2, res3])))
print("///////////////")
print("r(x) = ", r(x3))

