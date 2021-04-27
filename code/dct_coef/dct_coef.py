import numpy as np
import math
pi = math.pi
sqrt = math.sqrt
cos = math.cos
n = 8

coef = np.array([[1]*n])
for i in range(1, n):
    row = sqrt(2) *np.array([cos((2*j + 1)*pi*i/(2*n)) for j in range(n)])
    coef = np.vstack((coef, row))
coef = coef / sqrt(n)
print(coef)
c = np.matmul(coef, coef.T)
c[np.abs(c) < 1e-10] = 0
print(c)

