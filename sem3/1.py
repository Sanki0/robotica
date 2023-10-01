# halla las coordenadas cilindricas de un punto en el espacio (-1, -1, 3)

import math

x = -1
y = -1
z = 3

r = math.sqrt(x**2 + y**2)
theta = math.atan(y/x)
phi = z

print("r = ", r)
print("theta = ", theta)
print("phi = ", phi)

