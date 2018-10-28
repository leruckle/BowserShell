from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


def ellipsoid(x, y, coeffs):
    a, b, c = coeffs
    z = np.sqrt(c**2 * (1 - (x**2 / a**2 + y**2 / b**2)))
    return z


def plot_ellipsoid(coeffs):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.linspace(-12.5, 12.5, 100)
    Y = np.linspace(-9.5, 9.5, 100)

    X, Y = np.meshgrid(X, Y)
    Z = ellipsoid(X, Y, coeffs)

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlim(-13, 13)
    ax.set_ylim(-10, 10)
    ax.set_zlim(0, 10)
    plt.axis('equal')
    plt.show()


def plot_ellipsoid_polar(coeffs):
    fig = plt.figure()  # Square figure
    ax = fig.add_subplot(111, projection='3d')

    # Radii corresponding to the coefficients:
    # rx, ry, rz = 1 / np.sqrt(coeffs)

    rx, ry, rz = coeffs

    # Set of all spherical angles:
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi / 2, 100)

    # Cartesian coordinates that correspond to the spherical angles:
    # (this is the equation of an ellipsoid):
    x = rx * np.outer(np.cos(u), np.sin(v))
    y = ry * np.outer(np.sin(u), np.sin(v))
    z = rz * np.outer(np.ones_like(u), np.cos(v))

    # Plot:
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='firebrick')

    # plt.axis('equal')
    # Adjustment of the axes, so that they all have the same span:
    max_radius = max(rx, ry, rz)
    for axis in 'xy':
        getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))
    ax.set_zlim(0, max_radius)


    plt.show()




if __name__ == "__main__":
    a = 25 / 2.0
    b = 19 / 2.0
    c = 10
    coeffs = (a, b, c)
    plot_ellipsoid_polar(coeffs)

