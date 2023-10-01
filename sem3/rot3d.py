# Rotar el vector [2, 3, 4] alrededor de los ejes x, y y z en ese orden, con ángulos de 37, 53 y -90 grados sexagesimales respectivamente.

import math

# Vector original
vector_original = [2, 3, 4]

# Ángulos de rotación en radianes
angulo_rotacion_x_radianes = math.radians(37)
angulo_rotacion_y_radianes = math.radians(53)
angulo_rotacion_z_radianes = math.radians(-90)

# Matrices de rotación
matriz_rotacion_x = [
    [1, 0, 0],
    [0, math.cos(angulo_rotacion_x_radianes), -math.sin(angulo_rotacion_x_radianes)],
    [0, math.sin(angulo_rotacion_x_radianes), math.cos(angulo_rotacion_x_radianes)]
]

matriz_rotacion_y = [
    [math.cos(angulo_rotacion_y_radianes), 0, math.sin(angulo_rotacion_y_radianes)],
    [0, 1, 0],
    [-math.sin(angulo_rotacion_y_radianes), 0, math.cos(angulo_rotacion_y_radianes)]
]

matriz_rotacion_z = [
    [math.cos(angulo_rotacion_z_radianes), -math.sin(angulo_rotacion_z_radianes), 0],
    [math.sin(angulo_rotacion_z_radianes), math.cos(angulo_rotacion_z_radianes), 0],
    [0, 0, 1]
]

# Aplicar la rotación al vector original

# Rotación en x

vector_rotado_x = [
    matriz_rotacion_x[0][0] * vector_original[0] + matriz_rotacion_x[0][1] * vector_original[1] + matriz_rotacion_x[0][2] * vector_original[2],
    matriz_rotacion_x[1][0] * vector_original[0] + matriz_rotacion_x[1][1] * vector_original[1] + matriz_rotacion_x[1][2] * vector_original[2],
    matriz_rotacion_x[2][0] * vector_original[0] + matriz_rotacion_x[2][1] * vector_original[1] + matriz_rotacion_x[2][2] * vector_original[2]
]

# Rotación en y

vector_rotado_y = [
    matriz_rotacion_y[0][0] * vector_rotado_x[0] + matriz_rotacion_y[0][1] * vector_rotado_x[1] + matriz_rotacion_y[0][2] * vector_rotado_x[2],
    matriz_rotacion_y[1][0] * vector_rotado_x[0] + matriz_rotacion_y[1][1] * vector_rotado_x[1] + matriz_rotacion_y[1][2] * vector_rotado_x[2],
    matriz_rotacion_y[2][0] * vector_rotado_x[0] + matriz_rotacion_y[2][1] * vector_rotado_x[1] + matriz_rotacion_y[2][2] * vector_rotado_x[2]
]

# Rotación en z

vector_rotado_z = [
    matriz_rotacion_z[0][0] * vector_rotado_y[0] + matriz_rotacion_z[0][1] * vector_rotado_y[1] + matriz_rotacion_z[0][2] * vector_rotado_y[2],
    matriz_rotacion_z[1][0] * vector_rotado_y[0] + matriz_rotacion_z[1][1] * vector_rotado_y[1] + matriz_rotacion_z[1][2] * vector_rotado_y[2],
    matriz_rotacion_z[2][0] * vector_rotado_y[0] + matriz_rotacion_z[2][1] * vector_rotado_y[1] + matriz_rotacion_z[2][2] * vector_rotado_y[2]
]

print("Vector original:", vector_original)
print("Vector rotado:", vector_rotado_z)