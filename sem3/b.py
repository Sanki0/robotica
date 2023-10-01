import sympy as sp

# Posición inicial
s0 = 3

# Definir la variable simbólica t
t, c = sp.symbols('t, c')

# Definir la velocidad
v = 5 * sp.sin(6 * sp.pi * t)

# Calcular la integral indefinida de la velocidad para obtener la posición
s = sp.integrate(v, t)
print("La integral es: ", s)


# Evaluar el factor de integración c
c_value = s0 - s.subs(t, 0)
print("El factor de integración es: ", c_value)

# Evaluar la posición en t = 2 segundos
t_value = 2
s_final = s.subs(t, t_value) + c_value  # Agregamos la posición inicial de s = 3

# Imprimir la posición en t = 2 segundos
print(f"a) La posición del objeto en t = 2 es {s_final} unidades.")

# ¿Y cuánto recorrió durante este tiempo? t2 -t0

# Distancia recorrida
d = s_final - s0

# Imprimir la distancia recorrida
print(f"b) La distancia recorrida es {d} unidades.")