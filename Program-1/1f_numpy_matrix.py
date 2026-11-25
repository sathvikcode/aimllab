import numpy as np

A = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Matrix A\n", A)
print("Matrix B\n", B)
print("Addition\n", A + B)
print("Subtraction\n", A - B)
print("Multiplication\n", A @ B)
print("Transpose\n", A.T)
print("Determinant\n", np.linalg.det(A))
