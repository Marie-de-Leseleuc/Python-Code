from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12345678)


verbose ="yes"
# Generates value for t-test
rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs2 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs3 = stats.norm.rvs(loc=5, scale=20, size=500)
rvs4 = stats.norm.rvs(loc=5, scale=20, size=100)
rvs5 = stats.norm.rvs(loc=8, scale=20, size=100)


def ttest_(s1,s2):
	var_eq = stats.ttest_ind(s1,s2)
	var_uneq = stats.ttest_ind(rvs1,rvs2, equal_var = False)
	return var_eq, var_uneq


def showplot(s1,s2):
	if verbose =="yes":
		fig, ax = plt.subplots(1, 1)
		ax.hist(s1, normed=True, histtype='stepfilled', alpha=0.2)
		ax.hist(s2, normed=True, histtype='stepfilled', alpha=0.2)

		ax.legend(loc='best', frameon=False)
		plt.show()

def brksp(x=1):
	for i in range(x):
		print("")


# Test with sample with identical means:
print("Test with sample with identical means:")
r1, r2 = ttest_(rvs1,rvs2)
print("Result with equal var assumed:",r1 )
print("Result with unequal var assumed:",r2 )
brksp(1)
showplot(rvs1,rvs2)



# ttest_ind underestimates p for unequal variances:
print("ttest_ind underestimates p for unequal variances:")
r1, r2 = ttest_(rvs1, rvs3)
print("Result with equal var assumed:",r1 )
print("Result with unequal var assumed:",r2 )
brksp(1)
showplot(rvs1,rvs3)


# When n1 != n2, the equal variance t-statistic is no 
# longer equal to the unequal variance t-statistic:
print("n1 != n2")
r1, r2 = ttest_(rvs1, rvs4)
print("Result with equal var assumed:",r1 )
print("Result with unequal var assumed:",r2 )
brksp(1)
showplot(rvs1,rvs4)


# T-test with different means, variance, and n:
print("T-test with different means, variance, and n:")
r1, r2 = ttest_(rvs1, rvs5)
print("Result with equal var assumed:",r1 )
print("Result with unequal var assumed:",r2 )
brksp(1)
showplot(rvs1,rvs5)
