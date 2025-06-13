import matplotlib.pyplot as plt
import numpy as np

'''Make a scatter plot and line plot'''
def graph(x, y1, y2):
    axes = plt.axes()
    ys = np.array([y1, y2])
    ys.reshape(-1)
    axes.plot(x, ys)
    plt.show()


x = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 1, 4, 9, 16, 25])
y2 = np.array([0, 1, 2, 1, 0, -1])

print(graph(x, y1, y2))