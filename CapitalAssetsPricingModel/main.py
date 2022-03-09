from scipy import stats
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2016, 1, 1)

# if you don't have csv
df_spy = web.DataReader('SPY', 'yahoo', start, end)
# if you have,put it under the current repo
# df_spy = pd.read_csv("SPY.csv",index_col=0,parse_dates=True)

# if you don't have csv
df_fb = web.DataReader('FB', 'yahoo', start, end)
# if you have , put it under the current repo
# df_fb = pd.read_csv("FB.csv",index_col=0,parse_dates=True)

df_spy.head()

df_fb.head()

df_fb['Close'].plot(label='Facebook', figsize=(10, 8))
df_spy['Close'].plot(label='SPY')
plt.legend()

df_fb['Cumu'] = df_fb['Close'] / df_fb['Close'].iloc[0]
df_spy['Cumu'] = df_spy['Close'] / df_spy['Close'].iloc[0]
df_fb['Cumu'].plot(label='Facebook', figsize=(10, 8))
df_spy['Cumu'].plot(label='SPY')
plt.legend()

df_fb['daily_ret'] = df_fb['Close'].pct_change(1)
df_spy['daily_ret'] = df_spy['Close'].pct_change(1)
plt.scatter(df_fb['daily_ret'], df_spy['daily_ret'])

LR = stats.linregress(df_fb['daily_ret'].iloc[1:], df_spy['daily_ret'].iloc[1:])

LR

beta, alpha, r_val, p_val, std_err = LR

beta  # high if the stock behaves just like the market.

alpha  # as the CAPM said that alpha is close to zero
