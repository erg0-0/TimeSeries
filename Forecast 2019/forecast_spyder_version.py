#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:56:55 2019
@author: Liliana Gmerek
"""

#Imports
import pandas as pd
import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import statsmodels.api as sm
from pylab import rcParams
import matplotlib.pyplot as plt
import matplotlib
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns

#%matplotlib inline
sns.set_context('notebook')
#%config InlineBackend.figure_format = 'retina'

matplotlib.rcParams['axes.labelsize'] = 25
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 17
matplotlib.rcParams['text.color'] = 'k'

#Import the data
#train_df = pd.read_csv("train.csv",encoding='utf-8' ) 

df = pd.read_csv("./Forecast 2019/Forecast3.csv", dayfirst=True, encoding='utf-8')
df.set_index('Posting period', inplace=True)