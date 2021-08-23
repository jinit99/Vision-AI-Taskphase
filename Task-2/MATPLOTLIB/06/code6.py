import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv(
    'c:/Users/JINIT JAIN/OneDrive/Documents/GitHub/Vision-AI-Taskphase/Task-2/MATPLOTLIB/06/content6.csv')
ids = data['Responder_id']
ages = data['Age']

# makes slots of 10 each ranging from 10 to 100
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# here log is used to make data which is too small visible
plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = 'r'

# makes a vertical line at the median age
plt.axvline(median_age, color=color, label='Age Median', linewidth=3)

plt.legend()

plt.title('Respondents Ages Group')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.savefig('Histograms')
plt.tight_layout()

plt.show()
