import numpy as np

a = np.array([1, 2, 3, 4])
b = a
print(b)

b[0] = 100
print(a)
print(b)