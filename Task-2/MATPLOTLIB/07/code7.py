import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')
# reading data from csv file
data = pd.read_csv(
    'c:/Users/JINIT JAIN/OneDrive/Documents/GitHub/Vision-AI-Taskphase/Task-2/MATPLOTLIB/07/data7.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
# this function is used to give a scatter plot of the data
plt.scatter(view_count, likes, c=ratio, cmap='summer',
            edgecolor='black', linewidth=1, alpha=0.75)

cbar = plt.colorbar()
# this helps us in getting a chart near the plot which says how much is the ration depending on the colour of the plots
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending Videos On YouTube')
plt.xlabel('Count of views')
plt.ylabel('Total likes on the video')
plt.savefig('Youtube')
plt.tight_layout()

plt.show()
