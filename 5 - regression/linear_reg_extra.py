# load numpy and pandas for data manipulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load statsmodels as alias ``sm``
import statsmodels.api as sm

# load the longley dataset into a pandas data frame - first column (year) used as row labels
df = pd.read_csv('longley.csv', index_col=0)
print(df.head())

y = df.Employed  # response
X = df.GNP  # predictor
X = sm.add_constant(X)  # Adds a constant term to the predictor
print(X.head())

est = sm.OLS(y, X)

est = est.fit()
print(est.summary())


# We pick 100 hundred points equally spaced from the min to the max
X_prime = np.linspace(X.GNP.min(), X.GNP.max(), 100)[:, np.newaxis]
X_prime = sm.add_constant(X_prime)  # add constant as we did before

# Now we calculate the predicted values
y_hat = est.predict(X_prime)



# Plot the raw data
plt.scatter(X.GNP, y, alpha=0.3)  
plt.xlabel("Gross National Product")
plt.ylabel("Total Employment")
plt.plot(X_prime[:, 1], y_hat, 'r', alpha=0.9)  # Add the regression line, colored in red
plt.show()


# import formula api as alias smf
import statsmodels.formula.api as smf

# formula: response ~ predictors
est = smf.ols(formula='Employed ~ GNP', data=df).fit()
est.summary()

print(est.summary())



# Fit the no-intercept model
est_no_int = smf.ols(formula='Employed ~ GNP - 1', data=df).fit()

# We pick 100 hundred points equally spaced from the min to the max
X_prime_1 = pd.DataFrame({'GNP': np.linspace(X.GNP.min(), X.GNP.max(), 100)})
X_prime_1 = sm.add_constant(X_prime_1)  # add constant as we did before

y_hat_int = est.predict(X_prime_1)
y_hat_no_int = est_no_int.predict(X_prime_1)

fig = plt.figure(figsize=(8,4))
splt = plt.subplot(121)

splt.scatter(X.GNP, y, alpha=0.3)  # Plot the raw data
plt.ylim(30, 100)  # Set the y-axis to be the same
plt.xlabel("Gross National Product")
plt.ylabel("Total Employment")
plt.title("With intercept")
splt.plot(X_prime[:, 1], y_hat_int, 'r', alpha=0.9)  # Add the regression line, colored in red

splt = plt.subplot(122)
splt.scatter(X.GNP, y, alpha=0.3)  # Plot the raw data
plt.xlabel("Gross National Product")
plt.title("Without intercept")
splt.plot(X_prime[:, 1], y_hat_no_int, 'r', alpha=0.9)  # Add the regression line, colored in red
plt.show()






'''

This summary provides quite a lot of information about the fit. The parts of the table we think are the most important are bolded in the description below.

The left part of the first table provides basic information about the model fit:

Element	Description
Dep. Variable	Which variable is the response in the model
Model	What model you are using in the fit
Method	How the parameters of the model were calculated
No. Observations	The number of observations (examples)
DF Residuals	Degrees of freedom of the residuals. Number of observations – number of parameters
DF Model	Number of parameters in the model (not including the constant term if present)
The right part of the first table shows the goodness of fit

Element	Description
R-squared	The coefficient of determination. A statistical measure of how well the regression line approximates the real data points
Adj. R-squared	The above value adjusted based on the number of observations and the degrees-of-freedom of the residuals
F-statistic	A measure how significant the fit is. The mean squared error of the model divided by the mean squared error of the residuals
Prob (F-statistic)	The probability that you would get the above statistic, given the null hypothesis that they are unrelated
Log-likelihood	The log of the likelihood function.
AIC	The Akaike Information Criterion. Adjusts the log-likelihood based on the number of observations and the complexity of the model.
BIC	The Bayesian Information Criterion. Similar to the AIC, but has a higher penalty for models with more parameters.
The second table reports for each of the coefficients

Description
The name of the term in the model
coef	The estimated value of the coefficient
std err	The basic standard error of the estimate of the coefficient. More sophisticated errors are also available.
t	The t-statistic value. This is a measure of how statistically significant the coefficient is.
P > |t|	P-value that the null-hypothesis that the coefficient = 0 is true. If it is less than the confidence level, often 0.05, it indicates that there is a statistically significant relationship between the term and the response.
[95.0% Conf. Interval]	The lower and upper values of the 95% confidence interval
Finally, there are several statistical tests to assess the distribution of the residuals

Element	Description
Skewness	A measure of the symmetry of the data about the mean. Normally-distributed errors should be symmetrically distributed about the mean (equal amounts above and below the line).
Kurtosis	A measure of the shape of the distribution. Compares the amount of data close to the mean with those far away from the mean (in the tails).
Omnibus	D’Angostino’s test. It provides a combined statistical test for the presence of skewness and kurtosis.
Prob(Omnibus)	The above statistic turned into a probability
Jarque-Bera	A different test of the skewness and kurtosis
Prob (JB)	The above statistic turned into a probability
Durbin-Watson	A test for the presence of autocorrelation (that the errors are not independent.) Often important in time-series analysis
Cond. No	A test for multicollinearity (if in a fit with multiple parameters, the parameters are related with each other).
As a final note, if you don’t want to include a constant term in your model, you can exclude it using the minus operator.


'''