# halle las coordenadas cartesianas del punto A que tiene coordenadas esfericas (r, theta, phi) = (4, 2pi/3, pi/6)

import math

r = 4
theta = 2*math.pi/3
phi = math.pi/6

x = r*math.sin(theta)*math.cos(phi)
y = r*math.sin(theta)*math.sin(phi)
z = r*math.cos(theta)

print("x = ", x)
print("y = ", y)
print("z = ", z)

