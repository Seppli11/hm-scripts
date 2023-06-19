import matplotlib.pyplot as plt
import numpy as np

#######################
# Definitionen        #
#######################

a = 0
b = 6
n = 30

y0 = 0
def f(x, y): return 0.1*y+np.sin(2*x)

#######################
# Euler Verfahren     #
#######################


step_size = (b - a) / n

x = np.linspace(a, b, n + 1)
y = np.zeros(n + 1)
y[0] = y0

for i in range(n):
    y[i + 1] = y[i] + step_size * f(x[i], y[i])

print(y)


x_min = a
x_max = b
y_min = -1
y_max = 3

count = 30

plt.plot(x, y, label="euler")

mesh_x, mesh_y = np.meshgrid(
    np.linspace(x_min, x_max, count),
    np.linspace(y_min, y_max, count)
)

plt.quiver(mesh_x, mesh_y, 1, f(mesh_x, mesh_y))

plt.legend()
plt.show()
