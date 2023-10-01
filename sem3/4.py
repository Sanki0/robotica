import math

# Coordenadas cartesianas del punto A
x = -1/2
y = math.sqrt(3)/2
z = math.sqrt(3)

# Calcular la distancia desde el origen (r)
r = math.sqrt(x**2 + y**2 + z**2)

# Calcular el ángulo polar (theta)
theta = math.acos(z / r)

# Calcular el ángulo azimutal (phi)
phi = math.atan2(y, x)

# Convertir los ángulos de radianes a grados si es necesario
theta_degrees = math.degrees(theta)
phi_degrees = math.degrees(phi)

# Mostrar las coordenadas esféricas
print("Coordenadas esféricas:")
print(f"r = {r}")
print(f"θ (theta) = {theta} radianes o {theta_degrees} grados")
print(f"ϕ (phi) = {phi} radianes o {phi_degrees} grados")
