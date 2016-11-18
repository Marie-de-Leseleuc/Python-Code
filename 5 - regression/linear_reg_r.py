from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(100)
y = np.random.random(100)


slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

print("slope: ", slope )
print("intercept: ", intercept )
print("r_value: ", r_value )
print("p_value: ", p_value )
print("std_err: ", std_err )

# To get coefficient of determination (r_squared)

print("r-squared:", r_value**2)
