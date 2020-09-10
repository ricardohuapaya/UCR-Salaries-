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

l= ['MES COMPLETO']
df = drop_this(df, l)

l=['position',
   'salary',
   'hours',
   'years',
   'respon']
df = change_columns(df, l)
df = df.fillna('No aplica')

df['salary/1000'] = df.salary/1000 #salary in thousands of colones
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
df['sal_qcut'] = pd.qcut(df.salary, 10) # salary in deciles

#years 
year_bins = [-np.inf,10, 20, 30, 40 ,50, np.inf]
df['years_cut'] = pd.cut(df['years'], year_bins)

#drop missing values
df = df.dropna()
#%%% add

df['time'] = '2020-08-01'

#%% import

df.to_csv('planilla_clean.csv', index = False)

#%% understand the new data 

#FIX the position data!

df.loc[df['position'].str.contains('VISITANTE'), 'position'] = 'PROFESOR VISITANTE'
df.loc[df['position'].str.contains('INVITADO|INV.'), 'position'] = 'PROFESOR VISITANTE'
df.loc[df['position'].str.contains('EXBECARIO | POSDOCTORADO'), 'position'] = 'PROFESOR EXBECARIO'
df.loc[df['position'].str.contains('EDUCACION SUPERIOR'), 'position'] = 'PROFESOR EDUCACION SUPERIOR'
df.loc[df['position'].str.contains('EDUCACION SUPERIOR'), 'position'] = 'PROFESOR EDUCACION SUPERIOR'
df.loc[df['position'].str.contains('CATEDRATICO'), 'position'] = 'PROFESOR CATEDRATICO'
df.loc[df['position'].str.contains('CATEDRATICO'), 'position'] = 'PROFESOR CATEDRATICO'

#%% import new positions

planilla_profesores = df.loc[df['position'].str.contains('PROFESOR')]
planilla_profesores = planilla_profesores.reset_index(drop = True)
planilla_profesores.to_csv('planilla_profesores .csv', index = False)

#%%% slip respon
glue = df
glue.loc[~glue['respon'].str.contains('PUESTO NO'), 'respon'] = 'ADMINISTRATIVO'

#%% import dichotomy

glue.to_csv('dichotomy_planilla.csv', index = False)

