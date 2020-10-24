# Universidad de Costa Rica Salaries: an Exploratory Analysis.

**Go back to the [main :leftwards_arrow_with_hook: ](https://github.com/ricardohuapaya/Portafolio/blob/main/README.md)** 

**Check the code:**

- [:arrow_forward: DataClean.py ](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/DataClean.py)
- [:arrow_forward: Exploratory.py](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Exploratory.py)
## General Information
The main objective of this project is to properly understand how the Universidad de Costa Rica, a public and State-funded college, distributes its salaries to each worker. The inspiration for this program comes from the day to day comments on how the University should spend its budget; as it has been most commonly criticized by the congress people that the University's employees (and specifically professors) earn _to much_ money. Also, we focus on determining the relationship between the salaries, the number of years worked and the type of job and position held at the University. 
## Data
All the data it's collected from the official University's [webpage](https://transparencia.ucr.ac.cr/), the dataset was downloaded as a CSV file and contains the payroll for each month. For this project, we are going to be working with the payroll for August 2020.

## Data Cleaning
In this segment, we take the information given by the university and we proceed to understand the first distributions of salaries. 

We are going to be focusing on four variables: ```position```, which gives us the position held at the university for each employee; ```salary```, which tells us the salary before taxes in colones for each employee; ```hours```, which details us the type of schedule, and ```years``` that sums the total years worked in the university.

To better understand the ```salary```  variable, we extract the ```salary_per_hour``` of work, in this case, we assume that each month has 4.34524 weeks, then we divide the salary in the number of weeks and the number of hours worked each week depending on the worker's schedule.

``` python
df['Salary_per_hour'] = df.salary/4.34524
df.loc[df['hours']=='Full time', 'Salary_per_hour'] = df.Salary_per_hour/40 
df.loc[df['hours']=='7/8 of time', 'Salary_per_hour'] = df.Salary_per_hour/(40*7/8) 
df.loc[df['hours']=='3/4 of time', 'Salary_per_hour'] = df.Salary_per_hour/(40*6/8)
df.loc[df['hours']=='5/8 of time', 'Salary_per_hour'] = df.Salary_per_hour/(40*5/8) 
df.loc[df['hours']=='Part Time', 'Salary_per_hour'] = df.Salary_per_hour/(40*4/8)
df.loc[df['hours']=='3/8 of time', 'Salary_per_hour'] = df.Salary_per_hour/(40*3/8)
df.loc[df['hours']=='1/4 of  time', 'Salary_per_hour'] = df.Salary_per_hour/(40*2/8)
df.loc[df['hours']=='1/8  of time', 'Salary_per_hour'] = df.Salary_per_hour/(40*1/8)
```

## Data Summary

**Summary:** Salary in Millons of colones and Years of Service; for _all employees_.
|          | Salary in Millions of colones | Years of service |
|----------|-------------------------------|------------------|
| Min      | 0.006712                      | 0                |
| Max      | 9.891736                      | 56               |
| Mean     | 1.306981                      | 12.55            |
| Median   | 1.057817                      | 11               |
| Skewness | 1.71                          | 0.78             |


**Summary:** Salary in Millons of colones and Years of Service; for _all professors_.

|          | Salary in Millions of colones | Years of service |
|----------|-------------------------------|------------------|
| Min      | 0.006712                      | 0                |
| Max      | 9.891736                      | 56               |
| Mean     | 1.144469                      | 10.38            |
| Median   | 0.623217                      | 8                |
| Skewness |  1.78                         | 1.13             |

For the next segment of the summary we are going to see the mean for the salary per hour and the mean of years of services f rom each group of workers. 
Adding a column that sums up the total number of employees.

**Tier One**

| Position              | Mean Salary per Hour | Mean Years of service | Quantity of employees |
|-----------------------|-----------------|------------------|-----------------------|
| RECTOR                | 37 750.82       | 24.00            | 1                     |
| VICERRECTOR           | 33 111.41       | 24.20            | 5                     |
| CONSEJO UNIVERSITARIO | 34 028.51       | 25.33            | 9                     |
| DECANO                | 30 304.97       | 28.69            | 13                    |
| DIRECTOR              | 24 109.13       | 20.56            | 46                    |
| DIRECTOR DE ESCUELA   | 25 693.57       | 25.22            | 45                    |
| CONTRALOR             | 31 503.20       | 31.00            | 1                     |
| SUBCONTRALOR          | 23 048.19       | 16.00            | 1                     |

**Tier Two**

| Position                | Salary per Hour | Years of service | Quantity of employees |
|-------------------------|-----------------|------------------|-----------------------|
| JEFE A                  | 19 943.41       | 26.16            | 48                    |
| JEFE B                  | 22 222.46       | 26.54            | 33                    |
| PROFESIONAL A           | 10 565.64       | 16.26            | 419                   |
| PROFESIONAL B           | 12 177.31       | 15.17            | 347                   |
| PROFESIONAL C           | 14 607.70        | 17.35            | 251                   |
| PROFESIONAL D           | 17 937.24        | 21.71            | 32                    |
| TECNICO ASISTENCIAL A   | 5 318.93         | 12.19            | 478                   |
| TECNICO ASISTENCIAL B   | 6 204.86         | 14.22            | 452                   |
| TECNICO ESPECIALIZADO A | 6 582.37         | 14.72            | 84                    |
| TECNICO ESPECIALIZADO B | 6 914.99         | 14.84            | 422                   |
| TECNICO ESPECIALIZADO C | 7 639.56         | 15.13            | 93                    |
| TECNICO ESPECIALIZADO D | 8 556.81         | 16.81            | 428                   |
| TRABAJADOR OPERATIVO A  | 4 630.86         | 11.00            | 95                    |
| TRABAJADOR OPERATIVO B  | 5 047.77         | 13.08            | 368                   |
| TRABAJADOR OPERATIVO C  | 6 745.08         | 13.82            | 418                   |

**Tier Three**

| Position                          | Salary per Hour | Years of service | Quantity of employees |
|-----------------------------------|-----------------|------------------|-----------------------|
| PROFESOR ADJUNTO                  | 12 662.14       | 17.43            | 167                   |
| PROFESOR ASOCIADO                 | 16 159.07       | 19.78            | 365                   |
| PROFESOR CATEDRATICO              | 23 865.03       | 25.06            | 399                   |
| PROFESOR EDUCACION SUPERIOR       | 8 584.62        | 11.02            | 49                    |
| PROFESOR EXBECARIO                | 13 440.51       | 10.69            | 94                    |
| PROFESOR INSTRUCTOR               | 10 150.55       | 15.48            | 787                   |
| PROFESOR INTERINO                 | 8 514.06        | 11.55            | 478                   |
| PROFESOR INTERINO BACHILLER       | 3 284.72        | 1.35             | 87                    |
| PROFESOR INTERINO LICENCIADO      | 5 164.01        | 5.53             | 2783                  |
| PROFESOR INTERINO SIN TITULO      | 3 511.35        | 6.71             | 7                     |
| PROFESOR PROFESOR SEP CONTRACTUAL | 2 245.58        | 1.00             | 14                    |
| PROFESOR VISITANTE                | 10 812.62       | 7.90             | 83                    |

## Data Visualization 
### Data Comprehension
From the first and second plots, we can understand how the employees are distributed by type of work schedule and the number of years worked for the institution. As is shown, the majority of the population works full time for the University; also, we can comprehend that even tho most of the employees from UCR have a tenure of years, there are large parts of the workers' population that surpass the 20 and 30-year mark.

![Graph1](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Figure%202020-10-09%20215917.png)

![Graph2](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Figure%202020-10-09%20215917%20(1).png)

Graphs 3 and 4 show an interesting relation between the salary, value of an hour of work, and type of schedule, in the case of the variable salary in millions of colones the majority of the salaries are under 2 million colones. And if we focus only on full-time workers, the concentration of data is also under two million.

![Graph3](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Figure%202020-10-09%20215917%20(2).png)

On the other hand, graph 4 shows that for most employees the value of an hour of work is under 10 thousand colones.

![Graph4](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Figure%202020-10-09%20215917%20(3).png)

If we now focus only on the professors from Universidad de Costa Rica we can now see, in graph 5, that the concentration of salaries is under 3 million colones. Nonetheless, the type of professor called ```CATEDRATICO```, which can be interpreted as a professor that can hold the chair of a course, has a fairly symmetrical distribution with 50% of the salaries in between 3-5 million colones.

![Graph5](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Figure%202020-10-09%20215917%20(4).png)

Similarly, the value of hours of work holds the concentration of data under a relatively low number of 20 thousand colones, but again the professor type ```CATEDRATICO``` maintains a symmetrical distribution with 50% of the data between 20 and 30 thousand colones.

![Graph6](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Figure%202020-10-09%20215917%20(5).png)

As we saw in last two graph theres is an interesting relation between the position held and the years worked for the institution. We can take more advantage of this insight and show in the an scatter plot, for this particular case we will be using the first four categories for professors ```CATEDRATICO, INTERINO, ASOCIADO, INSTRUCTOR ```, the main reason is that this four categories hold the largest amount of data as is shown in the next table.

|             | Number of Observations |
|-------------|------------------------|
| INTERINO    | 2964                   |
| INSTRUCTOR  | 787                    |
| CATEDRATICO | 399                    |
| ASOCIADO    | 365                    |

And thus the scatter plot that compares the salary per hour earned and the years worked for the institution shows a fairly positive relations. 

![Scatter](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/Salary_per_hour_scatter.png)

As we want to understand the relation better we proceded to do a linear regression model using this data and the ```sklearn``` package. We also want to test our model and see how it fits out data, for this we do supervised training of the data and split into two. 

![testdata](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/test_and_train_data.png)

## Final Remarks
After the code is ran we end up with fair results, the linear regression model shows an  

$$
R^{2} =0.71
$$ 

Which gives us the nex plot

![linearregression](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/images/linear_regression.png)

This helps us conclude with two important remarks, the first one being that most salaries are pre-determined by the category of position held lets say for example the category of position as ```INTERINO``` vs ```CATEDRATICO``` shows that on side the first type of professors are related with professors that entered the job market or are hired per semester thus we conclude are only dedicated to teaching and not primarily doing research or gaining much academic experience, on the other hand, the second type shows a professors that probably has a PhD. or post-graduate degree, and probably dedicates large amount of time in doing or developing research. In a sense one has more market value than the other, and we see be presented in the boxplots charts. 

The second remark is that there exists a fair positive relation between the amount of years worked for the institution and the salary earned. As we remember the first bar charts, there are large parts of the workers population that surpass the 20 30 and year marks. So this mainly the reason of why we see really high salaries been paid by the University.
