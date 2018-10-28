from Ellipsoid import ellipsoid
from Hexagons import hexagon
from matplotlib import pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

a = 25 / 2.0
b = 19 / 2.0
c = 10
coeffs = (a, b, c)


hexagons = hexagon(4, 4)
x_values = []
y_values = []
z_values = []
for hex in hexagons:
    yhex, xhex = hex
    yhex = yhex * 19 - 9.5 +3
    xhex = xhex * 25 - 12.5 -1.75
    zhex = ellipsoid(xhex, yhex, coeffs)
    x_values.append(xhex)
    y_values.append(yhex)
    z_values.append(zhex)

np.set_printoptions(precision=3, linewidth=75)

for q in x_values:
    print(q)
print("")
for q in y_values:
    print(q)
print("")
for q in z_values:
    print(q)
print("")

fig = plt.figure()
ax = fig.gca(projection='3d')

rx, ry, rz = coeffs

# Set of all spherical angles:
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi / 2, 100)

# Cartesian coordinates that correspond to the spherical angles:
# (this is the equation of an ellipsoid):
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

# Plot:
ax.plot_wireframe(x, y, z, rstride=4, cstride=4, color='gray', linewidth=0.5)

# plt.axis('equal')
# Adjustment of the axes, so that they all have the same span:
# max_radius = max(rx, ry, rz)
# for axis in 'xy':
#     getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))
# ax.set_zlim(0, max_radius)

for i in range(len(z_values)):
    ax.plot(x_values[i], y_values[i], z_values[i], 'o-', linewidth=2)

ax.set_xlim(-13, 13)
ax.set_ylim(-10, 10)
ax.set_zlim(0, 10)
plt.axis('equal')
ax.set_zlim(0, 30)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')



#XX = 3.607
#YY = -4.3888
#ZZ = 8.386

XX = 4.04
YY = -3.76
ZZ = 8.22


for yyyyy in range(100):
    minResidual = 100000

    for i in range(2):
        for j in range(2):
            for k in range(2):

                xx = XX-0.02+0.04*i
                yy = YY-0.02+0.04*j
                zz = ZZ - 0.02 + 0.04 * k

                det1 = [[x_values[4][2], x_values[5][2], x_values[8][2], xx], [y_values[4][2], y_values[5][2], y_values[8][2], yy], [z_values[4][2], z_values[5][2], z_values[8][2], zz], [1, 1, 1, 1]]
                det2 = [[x_values[5][1], x_values[5][2], x_values[9][2], xx], [y_values[5][1], y_values[5][2], y_values[9][2], yy], [z_values[5][1], z_values[5][2], z_values[9][2], zz], [1, 1, 1, 1]]

                residual = np.linalg.det(det1)**2 + np.linalg.det(det2)**2
                if(residual < minResidual):
                    minResidual = residual
                    bestx = xx
                    besty = yy
                    bestz = zz

    XX = bestx
    YY = besty
    ZZ = bestz

    print(minResidual, bestx, besty, bestz)


plt.plot([4.400000000000013], [-3.3599999999999994], [8.539999999999994], 'or')

plt.show()