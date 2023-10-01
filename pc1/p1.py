import sympy as sp

# Posicion inicial
s0 = 3

# Definir la variable t
t = sp.symbols('t')

# Definir la velocidad
v = 5 * sp.sin(6 * sp.pi * t)

# Calcular la integral indefinida de la velocidad para obtener la posicion
s = sp.integrate(v, t)
print("La integral es: ", s)

# Evaluar en la posicion inicial para obtener el factor de integracion c
c_value = s0 - s.subs(t, 0)
print("El factor de integracion c es: ", c_value)

# Evaluar la posicion en t = 2 segundos
t_value = 2
s_final = s.subs(t, t_value) + c_value 

print(f"a) La posicion del objeto en t = 2 es {s_final}")

# Distancia recorrida como integral definida
d = sp.integrate(v, (t, 0, t_value))
print(f"b) La distancia recorrida es {d}")
