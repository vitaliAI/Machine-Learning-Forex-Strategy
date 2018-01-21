#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:56:39 2018

@author: vmueller
"""

import pandas as pd
import plotly as py
from plotly import tools
import plotly.graph_objs as go
from ffeatures import *

# Step 1 Loading and Cleaning the Data

df = pd.read_csv('Data/EURUSDHOURS.csv')
df.columns = [['date','open','high','low','close','volume']]
df.date = pd.to_datetime(df.date, format='%d.%m.%Y %H:%M:%S.%f')
df = df.set_index(df.date)
df = df[['open','high','low','close','volume']]
df = df.drop_duplicates(keep=False)
df = df.iloc[:50]

# Moving Average 30 MA
ma = df.close.rolling(center=False,window=30).mean()


# Get Heiken Ashi Method from ForexFeutures 
# Heiken Ashi

ff = ForexFeatures(df)
HA = ff.heikenashi()

trace0 = go.Ohlc(x=df.index,open=df.open,high=df.high,low=df.low,close=df.close, name='OHLC EURUSD 1HOUR CHART')
trace1 = go.Ohlc(x=HA.index, open=HA.open, high=HA.high, low=HA.low,close=HA.close, name='Heiken Ashi 1HOUR CHART')


data = [trace0, trace1, trace2]
fig = tools.make_subplots(rows=2,cols=1,shared_xaxes=True)
fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,1)
fig.append_trace(trace2,2,1)

py.offline.plot(fig,filename='Heiken_Ashi.html')

