from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = []
y = []
z = []
for phi in u:
    x.append([])
    y.append([])
    z.append([])
    for theta in v:
        x[-1].append(np.sin(theta)*np.cos(phi))
        y[-1].append(np.sin(theta)*np.sin(phi))
        z[-1].append(np.cos(theta))




ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')

plt.show()
