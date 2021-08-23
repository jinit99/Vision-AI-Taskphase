import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('ggplot')

data = pd.read_csv(
    'c:/Users/JINIT JAIN/OneDrive/Documents/GitHub/Vision-AI-Taskphase/Task-2/MATPLOTLIB/08/data8.csv')

data['Date'] = pd.to_datetime(data['Date'])
# inplace is used to replace the thing at that time only after doing the editing of the file content
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices On Various Dates')
plt.xlabel('Dates')
plt.ylabel('Closing Prices')

plt.tight_layout()
plt.savefig('Bitcoin')
plt.show()
