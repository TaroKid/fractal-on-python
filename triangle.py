import matplotlib.pyplot as plt
import random
import math
import numpy as np

vertices = [[-10, 0], [10, 0], [0, 20 * math.sin(math.radians(60))]]
x, y , repeat= 0, 0, 60000
points = []

for i in range(repeat):
    vertex = random.choice(vertices)
    x = (x + vertex[0]) / 2
    y = (y + vertex[1]) / 2
    points.append([x, y])
points = np.array(points)
vertices = np.array(vertices)

plt.ion()
plt.title('Sierpinski triangle')
plt.axis('equal')
plt.plot(vertices[:, 0], vertices[:, 1], 'mv')
text = plt.text(-10, 13, '', fontsize=12, color='red')

for i in range(0, repeat, 500):
    plt.plot(points[i: i + 500, 0], points[i: i + 500, 1], '.k')
    text.set_text(f'Points: {i + 500}')
    plt.pause(1e-6)
plt.ioff()
print("繪圖完成！\n")
plt.show()
