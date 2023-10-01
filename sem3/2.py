# halla las coordenadas cartesianas del punto A que tiene coordenadas cilindricas (r, theta, phi) = (2, 2pi, -4)

import math

r = 2
theta = 2*math.pi/3
phi = -4

x = r*math.cos(theta)
y = r*math.sin(theta)
z = phi

print("x = ", x)
print("y = ", y)
print("z = ", z)

