import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c = 'red', edgecolor = 'none', s = 10)
# plt.scatter(x_values, y_values, c = (0, 0, 0.8), edgecolor = 'none', s = 10)
#颜色映射colormap
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 10)

plt.title("Square Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
#设置每个坐标轴的范围
plt.axis([0, 1100, 0, 1100000])
#设置刻度标记大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
#自动保存图表:其中bbox_inches将空余白边裁剪掉
plt.savefig('squares_plot.png', bbox_inches = 'tight')