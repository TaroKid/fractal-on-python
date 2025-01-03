import matplotlib.pyplot as plt
import random
import math
import numpy as np

vertices = [[-10, 0], [10, 0], [0, 20 * math.sin(math.radians(60))]]
x = int(input("Input initial point x: "))
y = int(input("Input initial point y: "))
position= [x, y]
steps = int(input("Input iteration steps: "))
while True:
    speed = int(input("Input drawing speed (1 ~ 30): "))
    if speed >= 1 and speed <= 30:
        speed *= 100
        break
    else:
        print("Please input the valid speed value.")
points = []

for i in range(steps):
    vertex = random.choice(vertices)
    x = (x + vertex[0]) / 2
    y = (y + vertex[1]) / 2
    points.append([x, y])
points = np.array(points)
vertices = np.array(vertices)

plt.ion()
plt.title('Sierpinski Triangle')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-11, 11)
plt.ylim(-1, 18)
plt.plot(vertices[:, 0], vertices[:, 1], 'mv')
scatter = plt.scatter([], [], s = 0.1, color = 'black')
text = plt.text(-10, 13, '', fontsize=12, color='red')

for i in range(0, steps, speed):
    scatter.set_offsets(points[0 : i + speed])
    text.set_text(f'Points: {i + speed}')
    plt.pause(1e-6)
text.set_text(f'Points: {steps}\nComplete!')
plt.ioff()
plt.show()
