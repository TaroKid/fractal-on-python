import matplotlib.pyplot as plt
import numpy as np
import random

position = np.array([0, 0])
repeat = int(input("巴恩斯利蕨，請輸入迭代步數："))
while True:
    speed = int(input("請輸入繪製速度（1～10）："))
    if (speed >= 1) and (speed <= 10):
        steprange = 100 * speed
        break
    else:
        print("數值不匹配，請重新輸入")
points = []
twig, long_offset = np.array([[0.86, 0.03], [-0.03, 0.86]]), np.array([0, 1.5])
branch_one, uno_offset = np.array([[0.2, -0.25], [0.21, 0.23]]), np.array([0, 1.5])
branch_two, dos_offset = np.array([[-0.15, 0.27], [0.25, 0.26]]), np.array([0, 0.45])
root, zero_offset = np.array([[0, 0], [0, 0.17]]), np.array([0, 0])

for i in range(repeat):
    dice = random.randrange(0, 100)
    if dice < 83:
        position = np.dot(twig, position) + long_offset
    elif dice < 91:
        position = np.dot(branch_one, position) + uno_offset
    elif dice < 99:
        position = np.dot(branch_two, position) + dos_offset
    else:
        position = np.dot(root, position) + zero_offset
    points.append(position.tolist())
points = np.array(points)

plt.ion()
plt.title('Barnsley Fern')
plt.gca().set_aspect('equal', adjustable='box')
scatter = plt.scatter([], [], s=0.1, color='green')
text = plt.text(-2, 11, '', fontsize=12, color='red')

plt.xlim(-3, 3)
plt.ylim(-1, 12)  

for i in range(0, repeat, steprange):
    scatter.set_offsets(points[0 : i + steprange])
    text.set_text(f'Points: {i + steprange}')
    plt.pause(1e-6)
plt.ioff()
print("繪圖完成！")
plt.show()

