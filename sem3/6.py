#Dado el vector (2,-2) en el plano, rota el vector un ángulo de 60 grados en sentido antihorario alrededor del punto (-3,4)

import math

# Vector original
vector_original = [2, -2]

# Punto de rotación
punto_rotacion = [-3, 4]

# Trasladar el vector al punto de rotación
vector_trasladado = [vector_original[0] - punto_rotacion[0], vector_original[1] - punto_rotacion[1]]

# Ángulo de rotación en radianes
angulo_rotacion_radianes = math.radians(60)

# Matriz de rotación
matriz_rotacion = [
    [math.cos(angulo_rotacion_radianes), -math.sin(angulo_rotacion_radianes)],
    [math.sin(angulo_rotacion_radianes), math.cos(angulo_rotacion_radianes)]
]

# Aplicar la rotación al vector trasladado
vector_rotado = [
    matriz_rotacion[0][0] * vector_trasladado[0] + matriz_rotacion[0][1] * vector_trasladado[1],
    matriz_rotacion[1][0] * vector_trasladado[0] + matriz_rotacion[1][1] * vector_trasladado[1]
]

# Sumar las coordenadas del punto de rotación nuevamente
vector_resultado = [vector_rotado[0] + punto_rotacion[0], vector_rotado[1] + punto_rotacion[1]]

print("Vector original:", vector_original)
print("Vector rotado:", vector_resultado)
