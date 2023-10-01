import sympy as sp

# Definir las variables simbólicas
a, b, x, y, z, r, theta, phi = sp.symbols('a b x y z r theta phi')

# Solicitar las coordenadas del punto en forma simbólica
x = sp.sympify(input("Ingrese la coordenada x en términos de 'a' y 'b': "))
y = sp.sympify(input("Ingrese la coordenada y en términos de 'a' y 'b': "))
z = sp.sympify(input("Ingrese la coordenada z en términos de 'a' y 'b': "))

# Calcular las coordenadas cilíndricas
r = sp.sqrt(x**2 + y**2)
theta = sp.atan2(y, x)

# Calcular las coordenadas esféricas
rho = sp.sqrt(x**2 + y**2 + z**2)
phi = sp.acos(z / rho)

# Imprimir coordenadas en coordenadas cilíndricas y esféricas
print(f"\nCoordenadas en coordenadas cilíndricas:")
print(f"r = {r}")
print(f"theta = {theta}")
print(f"\nCoordenadas en coordenadas esféricas:")
print(f"rho = {rho}")
print(f"phi = {phi}")

# Solicitar los valores de 'a' y 'b'
a_value = float(input("Ingrese el valor de 'a': "))
b_value = float(input("Ingrese el valor de 'b': "))

# Reemplazar 'a' y 'b' en las coordenadas y evaluar en forma numérica
x_numeric = x.subs({a: a_value, b: b_value}).evalf()
y_numeric = y.subs({a: a_value, b: b_value}).evalf()
z_numeric = z.subs({a: a_value, b: b_value}).evalf()

# Imprimir las coordenadas numéricas
print("\nCoordenadas en forma numérica (con 4 decimales):")
print(f"x = {x_numeric:.4f}")
print(f"y = {y_numeric:.4f}")
print(f"z = {z_numeric:.4f}")
