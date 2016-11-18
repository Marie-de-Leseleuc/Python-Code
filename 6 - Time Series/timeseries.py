import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

import numpy as np

df = pd.read_csv('NZAlcoholConsumption.csv')
to_forecast = df.TotalBeer.values
dates = df.DATE.values


def organize_data(to_forecast, window, horizon):
    """
     Input:
      to_forecast, univariate time series organized as numpy array
      window, number of items to use in the forecast window
      horizon, horizon of the forecast
     Output:
      X, a matrix where each row contains a forecast window
      y, the target values for each row of X
    """
    shape = to_forecast.shape[:-1] + (to_forecast.shape[-1] - window + 1, window)
    strides = to_forecast.strides + (to_forecast.strides[-1],)
    X = np.lib.stride_tricks.as_strided(to_forecast, 
                                        shape=shape, 
                                        strides=strides)
    y = np.array([X[i+horizon][-1] for i in range(len(X)-horizon)])
    return X[:-horizon], y

k = 4   # number of previous observations to use
h = 1   # forecast horizon
X,y = organize_data(to_forecast, k, h)


 
m = 10 # number of samples to take in account
regressor = LinearRegression(normalize=True)
# regressor = LogisticRegression(penalty='l1')
regressor.fit(X[:m], y[:m])


def mape(ypred, ytrue):
    """ returns the mean absolute percentage error """
    idx = ytrue != 0.0
    return 100*np.mean(np.abs(ypred[idx]-ytrue[idx])/ytrue[idx])

print('The error is {} %'.format(np.round(mape(regressor.predict(X[m:]),y[m:]),2)))


plt.figure(figsize=(8,6))
plt.plot(y, label='True demand', color='#377EB8', linewidth=2)
plt.plot(regressor.predict(X), '--', color='#EB3737', linewidth=3, label='Prediction')
plt.plot(y[:m], label='Train data', color='#3700B8', linewidth=2)
plt.xticks(np.arange(len(dates))[1::4],dates[1::4], rotation=45)
plt.legend(loc='upper right')
plt.show()

