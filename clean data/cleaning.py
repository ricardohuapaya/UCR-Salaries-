# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:00:37 2020

@author: Ricardo 
"""
#The main idea is to clean all the data
import pandas as pd 
import numpy as np
df = pd.read_csv('planilla-2020-08.csv', sep =';')
print(df.columns)

#%%% Functions
def drop_this (DataFrame, list): #this function drops columns you don't need
    try:
        DataFrame2 = DataFrame.drop(columns = list)
        print('Elements dropped')
        print(list)
        return DataFrame2
    except KeyError:
        print('This name is not in the DataFrame')
                
def change_columns(DataFrame, list): #this function renames the columns
    try: 
        DataFrame.columns = list
        return DataFrame
    except Exception as e:
        print(e)
        
#%%% Let's clean what we don't need

print('How many elements do you want out?')
n = int(input())
l = []

for i in range(n):
    print('Type the name of element #', (i+1))
    h = str(input())
    l.append(h)
    
df = drop_this(df, l)


print('Change Column names')
j = df.columns
n = len(j)
l = []
for i in range(n):
    print('Type the new names #', i+1)
    h = str(input())
    l.append(h)

df = change_columns(df, l)
df = df.fillna('No aplica')

#%%% Let's fix what we need

#Hours_range

hours_bins = [0, 0.125, 0.25,0.375, 0.50, 0.625, 0.75, 0.875, 1.]
hours_label = ['1/8 de tiempo', 
               '1/4 de tiempo',
               '3/8 de tiempo', 
               '1/2 tiempo',
               '5/8 de tiempo', 
               '3/4 de tiempo',
               '7/8 de tiempo',
               'Tiempo Completo']

df.hours = pd.cut(df['hours'], hours_bins, labels = hours_label)

#Salary_percentile
df['sal_qcut'] = pd.qcut(df.salary, 10) 

#years 
year_bins = [-np.inf,10, 20, 30, 40 ,50, np.inf]
df['years_cut'] = pd.cut(df['years'], year_bins)

#drop missing values
df = df.dropna()
#%%% add

df['time'] = '2020-08-01'

#%% import

df.to_csv('planilla_clean.csv', index = False)
