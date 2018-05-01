# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:43:32 2018

@author: Ben
"""

import pandas as pd


file = 'C:\\Users\\Ben\\PythonProjects\\football.analytics\\defense2017.csv'

df = pd.read_csv(file)

#sets the index to teams
#df = df.rank('index')
#df1 = df['Tm','G']

print(df.head())


df1 = df[['Tm', 'G', 'Tgt', 'Rec', 'Yds', 'TD', 'FDPt']]
df1['Rec_per_Tgt'] = (df1['Rec'] / df1['Tgt'])
df1 = df1.sort_values(by='Rec_per_Tgt', ascending = False)
df1['RecRate_Rank'] = df1['Rec_per_Tgt'].rank(ascending=False)
df1['FDPt_Rank'] = df1['FDPt'].rank(ascending=False)
df1['Rec_per_G'] = (df1['Rec'] / df1['G'])
df1['Rec_per_G_Rank'] = df1['Rec_per_G'].rank(ascending=False)
df1['Yds_per_G'] = (df1['Yds'] / df1['G'])
df1['Yds_per_G_Rank'] = df1['Yds_per_G'].rank(ascending=False)
print(df1)