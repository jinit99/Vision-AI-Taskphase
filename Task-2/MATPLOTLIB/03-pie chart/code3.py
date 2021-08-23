from matplotlib import pyplot as plt

plt.style.use("ggplot")

# taking just 5 datas as shown in video as much data makes the graph look congested
slices = [59219, 55466, 47544, 36443, 35917]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# this is used to enhance or highlight a part of the pie chart
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})  # wedgeprops is used to get the outline of the pie chart which differentiates from the others


plt.title("My First Pie Chart")
plt.tight_layout()
plt.savefig('piechart')
plt.show()
