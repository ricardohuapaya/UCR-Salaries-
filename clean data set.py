# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:00:37 2020

@author: Ricardo 
"""
#The main idea is to clean all the data
import pandas as pd 
df = pd.read_csv('planilla-2020-08.csv', sep =';')
print(df.columns)

#%% Funtions
def drop_this (DataFrame, list):
    try:
        DataFrame2 = DataFrame.drop(columns = list)
        print('Elements dropped')
        print(list)
        return DataFrame2
    except KeyError:
        print('This name is not in the DataFrame')
        
        
def change_columns(DataFrame, list): 
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
    
df = df.fillna('No aplica')



#%%% Subsets

df_count = df.position.value_counts()

df_worth = df_count[df_count['position'] < 10]

