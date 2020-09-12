import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('planilla_clean.csv')
df_profe = pd.read_csv('planilla_profesores .csv')
df_split = pd.read_csv('dictom_planilla.csv')


sns.set_style("darkgrid")

# Basic Ploting
#%% Countplots
"""
The idea of the count plot are to understand where is each piece of data located. Since we
are working with salaries we first want to see how the basic distribution of data according to 
their basic ranks such as 'years employed' and how many hours they are working.
"""

plt.figure(figsize=(12,6))
plt.title('UCR: Quantity of employees by type of schedule')
hours_plot = sns.countplot(df.hours,
                  palette = 'BuPu_r',
                  order = df['hours'].value_counts().index)
plt.ylabel('Quantity of employees')
plt.xlabel('Type of schedule')

plt.show(hours_plot)

