import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')
data = pd.read_csv(
    'c:/Users/JINIT JAIN/OneDrive/Documents/GitHub/Vision-AI-Taskphase/Task-2/MATPLOTLIB/05/data5.csv')
ages = data['Age']
developer_salaries = data['All_Devs']
python_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, developer_salaries, color='r',
         linestyle='--', label='All developers')

plt.plot(ages, python_salaries, label='Python')
plt.plot(ages, js_salaries, label='Java Script')

overall_median = 57287  # median of the whole salary

plt.fill_between(ages, python_salaries, developer_salaries,
                 where=(python_salaries > developer_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, python_salaries, developer_salaries,
                 where=(python_salaries <= developer_salaries),
                 interpolate=True, color='k', alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary in (USD) by Age')
plt.xlabel('developer Ages')
plt.ylabel('Median Salary In (USD)')

plt.tight_layout()
plt.savefig('filling area')

plt.show()
