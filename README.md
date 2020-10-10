# Universidad de Costa Rica Salaries: an Exploratory Analysis.
## General Information
The main objective of this program is to properly understand how the Universidad de Costa Rica, a public and State-funded college, distributes its salaries to each worker.  Also, we focus on determining the relationship between the salaries, the number of years worked and the type of job and position held at the University. 
## Data
All the data it's collected from the official [webpage](https://transparencia.ucr.ac.cr/), the dataset was downloaded as a CSV file that contains the payroll for each month. For this project, we are going to be working with the payroll for August 2020.

## Data Cleaning
We take the information given by the university and we procede to understand the first distributions of salaries. 

## Data Summary

**Summary:** Salary in Millons of colones and Years of Service; for _all employees_.
|          | Salary in Millions of colones | Years of service |
|----------|-------------------------------|------------------|
| Min      | 0.006712                      | 0                |
| Max      | 9.891736                      | 56               |
| Mean     | 1.057374                      | 12.55            |
| Median   | 1.720855                      | 11               |
| Skewness | 1.30                          | 0.78             |


**Summary:** Salary in Millons of colones and Years of Service; for _all professors_.

|          | Salary in Millions of colones | Years of service |
|----------|-------------------------------|------------------|
| Min      | 0.006712                      | 0                |
| Max      | 9.891736                      | 56               |
| Mean     | 1.144469                       | 10.38            |
| Median   | 0.623217                     | 8               |
| Skewness |  1.78                           | 1.13             |

Mean of tier of employees

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

**Tier 3**

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

![Graph1](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Images/graph1.png)

![Graph2](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Images/graph2.png)

Graphs 3 and 4 show an interesting relation between the salary, value of an hour of work, and type of schedule, in the case of the variable salary in millions of colones the majority of the salaries are under 2 million colones. And if we focus only on full-time workers, the concentration of data is also under two million.

![Graph3](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Images/Figure%202020-10-08%20204128%20(2).png)

On the other hand, graph 4 shows that for most employees the value of an hour of work is under 10 thousand colones.

![Graph4](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Images/Figure%202020-10-08%20204128%20(3).png)

If we now focus only on the professors from Universidad de Costa Rica we can now see, in graph 5, that the concentration of salaries is under 3 million colones. Nonetheless, the type of professor called "CATEDRADICO", which can be interpreted as a professor that can hold the chair of a course, has a fairly symmetrical distribution with 50% of the salaries in between 3-5 million colones.

![Graph5](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Images/Figure%202020-10-08%20204128%20(6).png)

Similarly, the value of hours of work holds the concentration of data under a relatively low number of 20 thousand colones, but again the professor type "CATEDRATICO" maintains a symmetrical distribution with 50% of the data between 20 and 30 thousand colones.

![Graph6](https://github.com/ricardohuapaya/UCR-Salaries-/blob/master/Images/Figure%202020-10-08%20204128%20(7).png)
## Final Remarks
