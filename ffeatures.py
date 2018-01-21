#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:31:47 2018

@author: vmueller
"""

import pandas as pd
import numpy as np
from scipy import stats
import scipy.optimize
from scipy.optimize import OptimizeWarning
import warnings
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.finance import _candlestick
from matplotlib.dates import date2num
from datetime import datetime


class ForexFeatures:
    
    def __init__(self, df):
        self.dataframe = df
    
            
    def heikenashi(self):
        HAclose = self.dataframe[['open','high','close','low']].sum(axis=1)/4    
        HAopen = HAclose.copy()    
        HAopen.iloc[0] = HAclose.iloc[0]    
        HAhigh = HAclose.copy()    
        HAlow = HAclose.copy()    
        for i in range(1, len(self.dataframe)):
            HAopen.iloc[i] = (HAopen.iloc[i-1] + HAclose[i-1])/2    
            HAhigh.iloc[i] = np.array([self.dataframe.high.iloc[i], HAopen.iloc[i], HAclose.iloc[i]]).max()    
            HAlow.iloc[i] = np.array([self.dataframe.low.iloc[i], HAopen.iloc[i], HAclose.iloc[i]]).min()    
        df = pd.concat((HAopen,HAhigh,HAlow,HAclose), axis=1)
        df.columns = [['open','high','close','low']]    
        return df

