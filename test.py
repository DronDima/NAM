import math
eps = 0.0000000001

x = 2
X = x - (x**2-2)/(2*x)
count = 0
while(math.fabs(X-x) > eps):
    x = X
    X = x - (x ** 2 - 2) / (2 * x)
    count+=1
print(X)
print(count)