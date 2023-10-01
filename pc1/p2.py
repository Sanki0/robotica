import sympy as sp
import numpy as np

# Velocidad inicial
v0 = 4

# Definir la variable t
t = sp.symbols('t')

# Definir la aceleracion
a = (2*t + 3)**(-3)

# Calcular la integral indefinida de la aceleracion para obtener la velocidad
v = sp.integrate(a, t)
print ("La integral es: ", v)

# Evaluar en la posicion inicial para obtener el factor de integracion c
c_value = v0 - v.subs(t, 0)
print ("La constante de integracion es: ", c_value)

# Calculamos la velocidad en t = 2
t_value = 2
v_final = v.subs(t, t_value) + c_value

# Imprimir la velocidad en t = 2 con 4 decimales
print(f"La velocidad en t = 2 es: {v_final.evalf():.4f} m/s")