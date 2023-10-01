import numpy as np
from math import radians, cos, sin

# Definir las matrices de transformación
Rx_minus90 = np.array([[1, 0, 0, 0],
                       [0, 0, -1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]])

T_5_5_10 = np.array([[1, 0, 0, 5],
                     [0, 1, 0, 5],
                     [0, 0, 1, 10],
                     [0, 0, 0, 1]])

Rz_90 = np.array([[0, -1, 0, 0],
                  [1, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

T_minus4_6_7 = np.array([[1, 0, 0, -4],
                        [0, 1, 0, 6],
                        [0, 0, 1, 7],
                        [0, 0, 0, 1]])

theta = radians(45)
cos_theta = cos(theta)
sin_theta = sin(theta)
Ry_45 = np.array([[cos_theta, 0, sin_theta, 0],
                  [0, 1, 0, 0],
                  [-sin_theta, 0, cos_theta, 0],
                  [0, 0, 0, 1]])

# Calcular la matriz de transformación total
transformacion_total = Rx_minus90.dot(T_5_5_10).dot(Rz_90).dot(T_minus4_6_7).dot(Ry_45)

# Imprimir la matriz de transformación total
print("Matriz de transformación total:")
print(transformacion_total)
