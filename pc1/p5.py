import math
import scipy.integrate as integrate

# Definimos la función de velocidad v(t)
def velocidad(t):
    return 5 * math.sin(6 * math.pi * t)

# Posición inicial
s_0 = 3

# Instante t=2 
t = 2

# Calculamos la posición en t=2 segundos usando la fórmula de posición
s_t = s_0 + integrate.quad(velocidad, 0, t)[0]

# Imprimimos la posición en t=2 segundos
print(f"a. La posición en t=2 segundos es s({t}) = {s_t} unidades.")

# b. Calculamos la distancia recorrida durante ese tiempo usando la velocidad promedio
# La velocidad promedio se calcula como la integral de velocidad dividida por el intervalo de tiempo
velocidad_promedio = integrate.quad(velocidad, 0, t)[0] / t
distancia_recorrida = velocidad_promedio * t

# Imprimimos la distancia recorrida
print(f"b. La distancia recorrida durante t=2 segundos es {distancia_recorrida} unidades.")