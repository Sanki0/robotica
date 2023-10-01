import numpy as np

A=[1, 0 , 4]
B=[1, 3, 1]
C= [-4,2, 6]

#find the volume of the parallelepiped
A = np.array(A)
B = np.array(B)
C = np.array(C)
print(A)
print(B)
print(C)
print(np.cross(A,B))
print(np.dot(np.cross(A,B),C))
print(np.abs(np.dot(np.cross(A,B),C)))
