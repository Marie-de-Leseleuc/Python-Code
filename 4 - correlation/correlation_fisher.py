import numpy as np
import matplotlib.pyplot  as plt

## Number of simulated data sets
nrep = 1000


X = np.random.normal(size=100)
Y = np.random.normal(size=100)
r = np.corrcoef(X, Y)[0,1]

plt.scatter(X,Y, color = ['r', 'g'] )
plt.xlabel('X')
plt.ylabel('Y') 
plt.show()


F = 0.5*np.log((1+r)/(1-r))

## Simulation study for the correlation coefficient

## Sample size
n = 20

## Correlation between X and Y
r = 0.3

## Generate matrices X and Y such that the i^th rows of X and Y are
## correlated with correlation coefficient 0.3.
X = np.random.normal(size=(nrep,n))
Y = r*X + np.sqrt(1-r**2)*np.random.normal(size=(nrep,n))

## Get all the correlation coefficients
R = [np.corrcoef(x,y)[0,1] for x,y in zip(X,Y)]
R = np.array(R)

## Fisher transform all the correlation coefficients
F = 0.5*np.log((1+R)/(1-R))

print ("The standard deviation of the Fisher transformed " + "correlation coefficients is %.3f" % F.std() )
print( "1/sqrt(n-3)=%.3f" % (1/np.sqrt(n-3)))

## 95% confidence intervals on the Fisher transform scale
LCL = F - 2/np.sqrt(n-3)
UCL = F + 2/np.sqrt(n-3)

## Convert the intervals back to the correlation scale
LCL = (np.exp(2*LCL)-1) / (np.exp(2*LCL)+1)
UCL = (np.exp(2*UCL)-1) / (np.exp(2*UCL)+1)

CP = np.mean((LCL < r) & (r < UCL))

print( "The coverage probability is %.3f" % CP)