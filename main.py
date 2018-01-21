import pandas as pd
import plotly as py
from plotly import tools
import plotly.graph_objs as go

# Step 1 Loading and Cleaning the Data
df = pd.read_csv('Data/EURUSDHOURS.csv')
df.columns = [['date','open','high','low','close','volume']]
df.date = pd.to_datetime(df.date, format='%d.%m.%Y %H:%M:%S.%f')
df = df.set_index(df.date)
# Renaming Column names
df = df[['open','high','low','close','volume']]
# Removing Duplicates
df = df.drop_duplicates(keep=False)

ma = df.close.rolling(center=False,window=30).mean()
print(df.head())

trace0 = go.Ohlc(x=df.index,open=df.open,high=df.high,low=df.low,close=df.close, name='Candle EURUSD1Hour')
trace1 = go.Scatter(x=df.index,y=ma, name='Moving Average 30 MA')
trace2 = go.Bar(x=df.index,y=df.volume, name='Volume')

data = [trace0, trace1, trace2]

fig = tools.make_subplots(rows=2,cols=1,shared_xaxes=True)
fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,1)
fig.append_trace(trace2,2,1)

py.offline.plot(fig,filename='Candle_Stick.html')
#py.offline.plot(data,filename='tutorial.html')
