import numpy as np
from random import choice as choose
from matplotlib import pyplot

vertices = np.array([[0, 0], [10, 0], [10, 10], [0, 10]])
x, y, steps = 0, 0, 20000
points = np.zeros((steps, 2))

for i in range(steps):
    vertex = choose(vertices)
    x = (x + 2*vertex[0]) / 3
    y = (y + 2*vertex[1]) / 3
    points[i] = [x, y]

pyplot.title("Square")
pyplot.gca().set_aspect("equal", adjustable = "box")
pyplot.xlim(0, 10)
pyplot.ylim(0, 10)
pyplot.scatter(points[:, 0], points[:, 1], s = 0.1, color = "black")
pyplot.show()
