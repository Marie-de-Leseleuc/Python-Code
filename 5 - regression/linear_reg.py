from sklearn import datasets
from sklearn.cross_validation import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

lr = linear_model.LinearRegression()
boston = datasets.load_boston()
X = boston.data
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validated:
lr.fit(X, y)
predicted = cross_val_predict(lr, X, y, cv=10)

# # The coefficients
print('Coefficients: \n', lr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((lr.predict(X) - y) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % lr.score(X, y))


fig, ax = plt.subplots()
ax.scatter(y, predicted)

ax.plot([y.min(), y.max()], [y.min(), y.max()])

plt.show()

