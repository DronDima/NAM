import numpy as np
np.set_printoptions(precision = 4)
nodes = np.zeros(4)
h = 2
for i in range(4):
    nodes[i] = 3 + i*h
# x3 = nodes[9] + h / 2.6
def f(x):
    return 1.8 * np.power(np.e, -x) - 0.8 * np.tan(x)
def f2Shtr(x):
    return 1.8 * np.power(np.e, -x) - 1.6 * np.tan(x) / np.cos(x)**2
def h(nodes, i):
    return nodes[i] - nodes[i-1]
def ThomasMethod(A, d, n):
    x = np.zeros(n)
    alpha = np.zeros(n)
    beta = np.zeros(n)
    a = np.append(0, np.diag(A, -1))
    b = np.diag(A, 0)
    c = np.diag(A, 1)
    det = b[0]
    alpha[n-1] = -a[n-1]/b[n-1]
    beta[n-1] = d[n-1]/b[n-1]
    for i in range(n-2, 0, -1):
        alpha[i] = -a[i]/(b[i] + c[i]*alpha[i+1])
        beta[i] = (d[i] - c[i]*beta[i+1])/(b[i] + c[i]*alpha[i+1])
    x[0] = beta[0] = (d[0] - c[0]*beta[1])/(b[0] + c[0]*alpha[1])
    for i in range(1, n):
        x[i] = alpha[i]*x[i-1] + beta[i]
    return x
def S3(x, nodes, m, i):
    slag1 = m[i - 1] * (nodes[i] - x) ** 3 / (6 * h(nodes, i))
    slag2 = m[i] * (x - nodes[i - 1]) ** 3 / (6 * h(nodes, i))
    slag3 = (x - nodes[i - 1]) / h(nodes, i) * (f(nodes[i]) - m[i] * h(nodes, i) ** 2 / 6)
    slag4 = (nodes[i] - x) / h(nodes, i) * (f(nodes[i - 1]) - m[i - 1] * h(nodes, i) ** 2 / 6)
    return slag1 + slag2 + slag3 + slag4
def r(x, nodes):
    h = nodes[1] - nodes[0]
    return h**4*1.8
def spline(nodes):
    n = nodes.shape[0]
    A = np.zeros((n, n))
    A[0, 0] = 1
    A[n-1, n-1] = 1
    for i in range(1, n-1):
        A[i, i - 1] = h(nodes, i)/6
        A[i, i] = (h(nodes, i) + h(nodes, i + 1)) / 3
        A[i, i + 1] = h(nodes, i + 1) / 6

    b = np.zeros(n)
    b[0] = 2
    b[1] = 0
    b[2] = 0
    b[n-1] = -2
    # for i in range(1, n-1):
    #     b[i] = (f(nodes[i+1])-f(nodes[i])) / h(nodes, i+1) - (f(nodes[i])-f(nodes[i-1])) / h(nodes, i)
    m = ThomasMethod(A, b, n)
    # print("f(x) = ", f(x3))
    print("S(x) = ", S3(8, nodes, m, n - 1))
    # print("|f - S| = ", np.abs(f(x3) - S3(x3, nodes, m, n - 1)))
    # print("r(x) = ", r(x3, nodes))
spline(nodes)

