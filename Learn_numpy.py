import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)

# create numpy array
x = np.linspace(0, 2 * np.math.pi, 100)
y = np.sin(x)

# matrix production
A = np.array([[1, 0], [0, 1]])
B = np.array([[3, 0], [4, 1]])
A * B  # elementwise production
A.dot(B)  # matrix production
np.dot(A, B)  # another matrix production
A.T  # return a matrix transposed
