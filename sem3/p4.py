#  Se quiere obtener la matriz de transformación que representa al sistema O'UVW obtenido a partir del sistema OXYZ mediante un giro de ángulo -90° alrededor del eje OX, una traslación de vector pxyz (5, 5, 10), un giro de 90° sobre el eje OZ, una traslación de vector pxyz (-4, 6, 7) y finalmente un giro de 45° alrededor del eje OY.

import numpy as np
from math import radians, cos, sin

# Matriz de rotación en el eje X de -90

Rx_minus90 = np.array([[1, 0, 0, 0],
                       [0, 0, -1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]])

# Matriz de traslación a (5, 5, 10)
T_5_5_10 = np.array([[1, 0, 0, 5],
                     [0, 1, 0, 5],
                     [0, 0, 1, 10],
                     [0, 0, 0, 1]])

# Matriz de rotación en el eje Z de 90
sen2 = sin(radians(90))
cos2 = cos(radians(90))
Rz_90 = np.array([[0, -1, 0, 0],
                  [1, 0, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

# Matriz de traslación a (-4, 6, 7)
T_minus4_6_7 = np.array([[1, 0, 0, -4],
                         [0, 1, 0, 6],
                         [0, 0, 1, 7],
                         [0, 0, 0, 1]])

# Matriz de rotación en el eje Y de 45
cos_theta = cos(radians(45))
sin_theta = sin(radians(45))

Ry_45 = np.array([[cos_theta, 0, sin_theta, 0],
                  [0, 1, 0, 0],
                  [-sin_theta, 0, cos_theta, 0],
                  [0, 0, 0, 1]])

# Calcular la matriz de transformación total
transformacion_total = Rx_minus90.dot(T_5_5_10).dot(Rz_90).dot(T_minus4_6_7).dot(Ry_45)

# Imprimir la matriz de transformación total
print("Matriz de transformación total:")
print(transformacion_total)