#Exploratory Analysis
#git test

import pandas as pd

#create a data frame with the data from UCR salaries information

df = pd.read_csv('planilla_clean.csv', sep =',')
df_profe = pd.read_csv('planilla_profesores .csv', sep =',')

#%%% Basic Stats

df.agg({'salary_millions': ['min', 'max', 'mean', 'median', 'skew'],
        'years':['min', 'max', 'mean', 'median', 'skew']})


workers = df.groupby('position')['Salary_per_hour', 'years'].mean()

#%%% Teachers

df_profe.agg({'salary_millions': ['min', 'max', 'mean', 'median', 'skew'],
        'years':['min', 'max', 'mean', 'median', 'skew']})


teachers = df_profe.groupby('position')['salary_millions', 'years'].mean()

#%%% Visualization
import seaborn as sns
import matplotlib.pyplot as plt

#%% Quantity of people
plt.figure(figsize=(12,6))
plt.title('UCR: Quantity of employees by type of schedule')
g = sns.countplot(df.hours,
                  palette = 'BuPu_r',
                  order = df['hours'].value_counts().index)
plt.ylabel('Quantity of employees')
plt.xlabel('Type of schedule')

plt.show(g)

plt.figure(figsize=(12,6))
plt.title('UCR: Quantity of employees by amount of years worked')
f = sns.countplot(df.year_cut_in_10,
                  palette = 'BuPu_r',
                  order = df['year_cut_in_10'].value_counts().index)
plt.ylabel('Quantity of employees')
plt.xlabel('Years Worked')

#%% Salary in Millions and per hour in general staff General Staff

plt.figure(figsize=(12,6))
plt.title('UCR: Salary distribution by type of schedule')
h = sns.boxplot(x="hours",
                y="salary_millions", 
                width=0.7,
                showfliers= False,
                palette = 'BuPu_r',
                order = df['hours'].value_counts().index,
                data=df)
plt.ylabel('Salary in millons of colones')
plt.xlabel('Type of schedule')

plt.figure(figsize=(12,6))
plt.title('UCR: Salary per hour distribution by type of schedule')
h = sns.boxplot(x="hours",
                y="Salary_per_hour", 
                width=0.7,
                showfliers= False,
                palette = 'BuPu_r',
                order = df['hours'].value_counts().index,
                data=df)
plt.ylabel('Salary per hour')
plt.xlabel('Type of schedule')
 
#%% Teachers
df_profe.loc[df_profe['position'].str.contains('INTERINO'), 'position'] = 'INTERINO'

df_profe.loc[df_profe['position'].str.contains('CATEDRATICO'), 'position'] = 'CATEDRATICO'

df_profe.loc[df_profe['position'].str.contains('ASOCIADO'), 'position'] = 'ASOCIADO'

df_profe.loc[df_profe['position'].str.contains('ADJUNTO'), 'position'] = 'ADJUNTO'

df_profe.loc[df_profe['position'].str.contains('VISITANTE'), 'position'] = 'VISITANTE'

df_profe.loc[df_profe['position'].str.contains('EXBECARIO'), 'position'] = 'EXBECARIO'

df_profe.loc[df_profe['position'].str.contains('EDUCACION SUPERIOR'), 'position'] = 'EDUCACION SUPERIOR'

df_profe.loc[df_profe['position'].str.contains('INSTRUCTOR'), 'position'] = 'INSTRUCTOR'

df_profe.loc[df_profe['position'].str.contains('SEP'), 'position'] = 'SEP'


plt.figure(figsize=(15,6))
plt.title('UCR professors: Distribution of salaries')
ygu = sns.boxplot(x="position",
                y="salary_millions", 
                width=0.7,
                showfliers= False,
                order = df_profe['position'].value_counts().index,
                palette = 'BuPu_r',
                data=df_profe)
plt.ylabel('Salary in millions of Colones')
plt.xlabel('Job Title')


plt.figure(figsize=(15,6))
plt.title('UCR professors: Distribution of the value of an hour worked')
ygu = sns.boxplot(x="position",
                y="Salary_per_hour", 
                width=0.7,
                showfliers= False,
                order = df_profe['position'].value_counts().index,
                palette = 'BuPu_r',
                data=df_profe)
plt.ylabel('Salary per hour')
plt.xlabel('Job Title')
