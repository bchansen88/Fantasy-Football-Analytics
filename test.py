# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:43:32 2018

@author: Ben
"""

import pandas as pd


file = 'calcTest.csv'

df = pd.read_csv(file)
df = df.set_index('Tm')

print(df.head())
