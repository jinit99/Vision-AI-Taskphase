
from matplotlib import pyplot as plt

plt.style.use("ggplot")


time_in_min = [1, 2, 3, 4, 5, 6, 7, 8, 9]

developer1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
developer2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
developer3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['developer1', 'developer2', 'developer3']
colors = ['b', 'k', 'r']

plt.stackplot(time_in_min, developer1, developer2,
              developer3, labels=labels, colors=colors)

# the number indicates the percentage distance between the margin and its border
plt.legend(loc=(0.07, 0.05))

plt.title("My First Stack Plot")
plt.tight_layout()
plt.savefig('stackplot')
plt.show()
