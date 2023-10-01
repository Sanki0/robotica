import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función de la trayectoria r(t)
def r(t):
    x = t**2 - 3*t
    y = 2*t - 4
    z = t + 2
    return x, y, z

# Crear un rango de tiempo de 0 a 20 segundos
t = np.linspace(0, 20, 100)  # 100 puntos entre 0 y 20 segundos

# Calcular las posiciones en función del tiempo
x, y, z = r(t)

# Calcular la velocidad media en el intervalo de tiempo
Vm_x = (x[-1] - x[0]) / 20
Vm_y = (y[-1] - y[0]) / 20
Vm_z = (z[-1] - z[0]) / 20

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la trayectoria en 3D
ax.plot(x, y, z, label='Trayectoria r(t)')

# Configurar etiquetas de ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Mostrar la velocidad media en la figura
ax.text(x[-1], y[-1], z[-1], f'Vm = ({Vm_x:.2f}, {Vm_y:.2f}, {Vm_z:.2f})', fontsize=12, color='red')

# Mostrar la figura
plt.legend()
plt.show()
