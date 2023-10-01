import sympy as sp

# Definir el símbolo t para el tiempo
t = sp.symbols('t')

# Definir la aceleración
acceleration = -1/4 * t

# Calcular la velocidad como función del tiempo
velocity = sp.integrate(acceleration, t)

# Calcular la posición como función del tiempo
position = sp.integrate(velocity, t)

# Mostrar las soluciones
print("Velocidad como función del tiempo:")
sp.pprint(velocity, use_unicode=True)

print("\nPosición como función del tiempo:")
sp.pprint(position, use_unicode=True)