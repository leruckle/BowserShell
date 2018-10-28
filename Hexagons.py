import numpy as np
from numpy import tile
from numpy import linspace
from numpy import reshape
from numpy import diff
import math
import matplotlib.pyplot as plt


def hexagon(nx, ny):
    X = tile(linspace(0, 1, nx), (ny, 1))
    Y = linspace(0, 1, 2 * ny)

    Y = reshape(Y, (ny, 2))

    if nx % 2 == 0:  # nx is even
        Y = tile(Y, (1, int(nx / 2)))
    else:
        Y = tile(Y, (1, int((nx - 1) / 2 + 1)))

    rx = diff(X[0, 0:2]) * (2 / 3)
    ry = diff(Y[0:2, 0]) / math.sqrt(3)

    thetas = np.array([0, 60, 120, 180, 240, 300]) * math.pi / 180

    to_return = []
    for xf, yf in zip(X.flat, Y.flat):
        xhex = rx * np.cos(thetas) + xf
        yhex = ry * np.sin(thetas) + yf
        to_return.append((xhex, yhex))
    return to_return


def plot_hexagons():
    gridsize = 4
    ny = gridsize
    nx = gridsize

    X = tile(linspace(0, 1, nx), (ny, 1))
    Y = linspace(0, 1, 2 * ny)

    Y = reshape(Y, (gridsize, 2))

    if nx % 2 == 0:  # nx is even
        Y = tile(Y, (1, int(nx / 2)))
    else:
        Y = tile(Y, (1, int((nx - 1) / 2 + 1)))

    rx = diff(X[0, 0:2]) * (2 / 3)
    ry = diff(Y[0:2, 0]) / math.sqrt(3)

    X = reshape(X, (X.size, 1))
    Y = reshape(Y, (Y.size, 1))

    thetas = np.array([0, 60, 120, 180, 240, 300]) * math.pi / 180

    for xf, yf in zip(X.flat, Y.flat):
        xhex = rx * np.cos(thetas) + xf
        yhex = ry * np.sin(thetas) + yf

        plt.plot(xf, yf, 'o')
        plt.plot(xhex, yhex)

    plt.show()


if __name__ == '__main__':
    hexagons = hexagon(4, 4)
    print(hexagons)




