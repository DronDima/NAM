import numpy as np
import pandas as pd
import numpy.linalg as alg

n = 3
np.set_printoptions(precision = 4)
eps = 0.001
stack = []
A = pd.read_csv('matrix.txt', sep=' ', header = None, nrows = n)
b = pd.read_csv('matrix.txt', sep=' ', header = None, skiprows = n, nrows = 1)

def jacobi(A, b):
    B = np.zeros((n,n))
    g = np.zeros(n)
    x = np.zeros(n)
    for i in range(n):
        B[i,:] = -A[i,:]/A[i,i]
        B[i,i] = 0
        g[i] = b[i]/A[i,i]
    X = np.dot(B,x) + g
    iterations = 0
    while(np.linalg.norm(X-x, np.inf) > eps):
        iterations += 1
        x = X
        X = np.dot(B,x) + g
    print("Количество итераций: ", iterations)
    print("Решение: ", X)

jacobi(np.copy(A), np.copy(b).ravel())