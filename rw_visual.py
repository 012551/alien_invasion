import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_number = list(range(rw.num_point))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    kepp_running = input("Make another walk? (y/n):")
    if kepp_running == "n":
        break
