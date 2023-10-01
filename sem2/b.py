# Dado el vector (2,-2) en el plano, rota el vector un ángulo de 60 grados en sentido antihorario alrededor del punto (-3,4). Imprime el vector resultante.


import numpy as np
import matplotlib.pyplot as plt


# Vector
v = np.array([2,-2])

# Matriz de rotación
theta = np.pi/180* 15
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
# Producto punto
v2 = R.dot(v)

# Imprime el vector resultante
print(v2)