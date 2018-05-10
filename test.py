# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:43:32 2018

@author: Ben
"""

import pandas as pd
import matplotlib.pyplot as plt


file = 'calcTest.csv'
x = []
y = []

df = pd.read_csv(file)
#df = df.set_index('Tm')
df = df[['Tm', 'Rec']]
print(df)


#need to figure this one out
df.plot(x = 'Tm', y = 'Rec', kind='scatter')


'''
df = df.set_index('Tm')

forecast_col = 'Rec'

#empty data treated as an outlier
df.fillna(-99999, inplace = True)

#predict 10% out of the data frame
forecast_out = int(math.ceil(0.1 * len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
print(df.tail())
'''