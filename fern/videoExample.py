import numpy as np
from matplotlib import pyplot
from random import randrange as rrng

position = np.array([0, 0, 1])

arr1 = np.array([[0.85, 0.04, 0], [-0.04, 0.85, 1.6], [0, 0, 1]])
arr2 = np.array([[0.2, -0.26, 0], [0.23, 0.24, 1.6], [0, 0, 1]])
arr3 = np.array([[-0.15, 0.28, 0], [0.26, 0.24, 0.44], [0, 0, 1]])
arr4 = np.array([[0, 0, 0], [0, 0.16, 0], [0, 0, 1]])

r_0 = position
r_1 = position
for i in range(2000):
    r_1 = np.dot(arr1, r_1)
r_2 = np.dot(arr3, r_1)


l_0 = np.dot(arr2, r_0)
l_1 = np.dot(arr2, r_1)
l_2 = np.dot(arr2, r_2)

steps, now_pos = 50000, position
points = np.zeros((steps, 2))
for i in range(steps):
    dice = rrng(100)
    if dice < 83:
        now_pos = np.dot(arr1, now_pos)
    elif dice < 91:
        now_pos = np.dot(arr2, now_pos)
    elif dice < 99:
        now_pos = np.dot(arr3, now_pos)
    else:
        now_pos = np.dot(arr4, now_pos)
    points[i] = now_pos[0:2]

pyplot.title("Two Triangle")
pyplot.gca().set_aspect("equal", adjustable="box")
pyplot.xlim(-3, 3)
pyplot.ylim(-1, 12)
pyplot.plot(
    [r_0[0], r_1[0], r_2[0], r_0[0]],
    [r_0[1], r_1[1], r_2[1], r_0[1]],
    color="red",
)
pyplot.plot(
    [l_0[0], l_1[0], l_2[0], l_0[0]],
    [l_0[1], l_1[1], l_2[1], l_0[1]],
    color="blue",
)
pyplot.scatter(points[:, 0], points[:, 1], s=0.1, color="green")
pyplot.show()
