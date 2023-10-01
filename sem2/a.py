# Dado el vector (-3,2) en el plano, rota el vector un ángulo de 180 grados en sentido antihorario alrededor del origen del plano. print(v2)

import numpy as np
import matplotlib.pyplot as plt

# Vector
v = np.array([-3,2])

# Matriz de rotación
theta = np.pi
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
# Producto punto
v2 = R.dot(v)

# Gráfica
plt.plot([0,v[0]],[0,v[1]],label='v')
plt.plot([0,v2[0]],[0,v2[1]],label='v2')
plt.legend()
plt.grid()
plt.axis('square')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.show()

# Resultado
print(v2)