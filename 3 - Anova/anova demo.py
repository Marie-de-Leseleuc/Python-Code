import numpy as np
import pandas
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.graphics.api import interaction_plot, abline_plot
from statsmodels.stats.anova import anova_lm
import sys

def brk():
	sys.exit()


try:
     salary_table = pandas.read_csv('./salary.table')
except:
     print("fetching from website")
     url = 'http://stats191.stanford.edu/data/salary.table'
     #the next line is not necessary with recent version of pandas
     url = urlopen(url)
     salary_table = pandas.read_table(url)
     salary_table.to_csv('salary.table', index=False)


Salary = salary_table.S
Experience = salary_table.X
Education = salary_table.E
Management = salary_table.M


salary_table = salary_table.rename(columns={"S":"Salary",
								    "X":"Experience",
								    "E":"Education",
								    "M":"Management"})


print(salary_table)

# plt.figure(figsize=(6, 6))
# symbols = ['D', '^']
# colors = ['r', 'g', 'blue']
# factor_groups = salary_table.groupby(['Education', 'Management'])
# for values, group in factor_groups:
#      i, j = values
#      plt.scatter(group['Experience'], group['Salary'], marker=symbols[j], color=colors[i - 1],
#                  s=144)

# plt.xlabel('Experience');
# plt.ylabel('Salary');
# plt.show()

formula = 'Salary ~ C(Education) + C(Management) + Experience'
lm = ols(formula, salary_table).fit()
print(lm.summary())

