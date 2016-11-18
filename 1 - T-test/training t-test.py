# Tools  :
# from scipy import stats
# stats.ttest_ind(groupe1, groupe2, equal_var=True or False)
# stats.ttest_1samp(data, target_value)
# --> will output t-statistics & p-value

# import matplotlib.pyplot as plt
# plt.scatter() / plt.show()
from scipy import stats
import numpy as np


# Question 1 
# Is the average number of hours spent in game greater than the game average 175.3
# one_sample_data = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]
# r = stats.ttest_1samp(one_sample_data, 175.3)
# print(np.mean(one_sample_data))
# print(r)


# Question 2
# Are female player playing more PvP (in hours) than male ?
# female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
# male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]
# r = stats.ttest_ind(female, male, equal_var=True)
# print('female:',np.mean(female),'male:',np.mean(male))
# print(r)

# Question 3
# Is the average number of hours of this group of PvP players has increased after free currency ?
baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]
r = stats.ttest_rel(baseline, follow_up)

print('baseline:',np.mean(baseline),'follow_up:',np.mean(follow_up))
print(r)


# Bonus question: plot a scatterplot of the data ;)
