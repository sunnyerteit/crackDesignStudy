#!/usr/bin/python
# -*- coding: utf-8 -*-

# Reads the .dat-files produced from jBatch.py
# Uses the data to establish a surface plot of height, width and registered J-integral
# Author : Sunny Islam, 2017

from itertools import islice
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# some constant, smallest size fxf of half-plane

f = 60.0

# parameters b = width, w = height (don't ask), n = increments
# these parameters should be equivalent with those in jBatch.py

b = 100.0
w = 100.0
n = 10

i = np.linspace(f, b, num=n)
j = np.linspace(f, w, num=n)
x = np.array([])
y = x
z = x
for x_1 in range(n):
    for y_1 in range(n):

        # open .dat-files

        with open('data/' + str(x_1) + str(y_1) + '.dat') as p:
            for line in p:

                # find string in proximity to desired values

                if '-3-' in line:
                    # save next line and split the values into an array

                    temp = ''.join(islice(p, 1))
                    temp = temp.split()

                    # highest value of J should always be employed

                    d = max(temp)
                    d = np.array([d])
                    x = np.append(i[x_1], x)
                    y = np.append(j[y_1], y)
                    z = np.append(d, z)

                    # we need to break due to there being more occurences of our desired string in the .dat-file

                    break

# convert J-integral values to floats

z = z.astype(np.float)

# make data readable for surface plot interpolation

(X, Y) = np.meshgrid(i, j)
Z = griddata(
    x,
    y,
    z,
    i,
    j,
    interp='linear',
)

# establish figure

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('Normalized width, w/w_0')
ax.set_ylabel('Normalized height, h/h_0')
ax.set_zlabel('Normalized J-integral, J/J_0')
surf = ax.plot_surface(
    X / min(x),
    Y / min(y),
    Z / min(z),
    rstride=1,
    cstride=1,
    cmap=cm.jet,
    linewidth=1,
    antialiased=True,
)
ax.set_zlim3d(np.min(Z) / min(z), np.max(Z) / min(z))
fig.colorbar(surf)

plt.show()

# the reason for why increased width has a higher effect than height is due to the load being applied as a constant
# displacement. Thuas less width -> higher avg. strain dL/L -> higher stress


