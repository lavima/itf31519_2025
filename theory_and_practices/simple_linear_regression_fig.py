import matplotlib.pyplot as plt


xs = [1, 2, 3, 4]
ys = [2, 2, 4, 6]

fig, ax = plt.subplots(1,1)
ax.scatter(xs, ys)
ax.plot([0,4], [0,28.0/5.0], color='red')
plt.show()

