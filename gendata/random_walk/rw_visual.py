import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandWalk的实例
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values,  rw.y_values,  s = 15)
plt.show()