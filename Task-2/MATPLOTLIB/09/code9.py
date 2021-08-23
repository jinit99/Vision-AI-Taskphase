import random  # to get random values
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('ggplot')

x_vals = []
y_vals = []

index = count()


def animate(i):  # changing/altering the x and y values
    data = pd.read_csv(
        'c:/Users/JINIT JAIN/OneDrive/Documents/GitHub/Vision-AI-Taskphase/Task-2/MATPLOTLIB/data9.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()  # cla implies clear axis to avoid changing colour due to new line on each operation

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


# calling the funcanimation function
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
""" code for basic chart with changing colour
import random  # to get random values
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('ggplot')

x_vals = []
y_vals = []

index = count()


def animate(i): 
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.plot(x_vals, y_vals)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
 """
