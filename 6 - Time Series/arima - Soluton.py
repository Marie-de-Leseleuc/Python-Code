import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt


# create an Excel file object
excel = pd.ExcelFile( 'PET_PRI_SPT_S1_M.xls' )
 
# parse the first sheet
df = excel.parse( excel.sheet_names[1] )
 
# rename the columns
df = df.rename( columns=dict( zip( df.columns, ['Date','Brent'] ) ) )
 
# cut off the first 18 rows because these rows
# contain NaN values for the Brent prices
df = df[18:]


# index the data set by date
df.index = df['Date']

# remove the date column after re-indexing
df = df[['Brent']]
print(df)

df.plot()
plt.show()

#############################################################################

## SOLUTION

print(df)

endog = np.asarray(df["Brent"])
endog_dates = np.asarray(df.index)

ar_model = sm.tsa.AR(endog, dates=endog_dates, freq='M')
pandas_ar_res = ar_model.fit()

pred = pandas_ar_res.predict(start='2015-10-15', end='2017-01-18')
pred = pd.TimeSeries(pred, index=pandas_ar_res.data.predict_dates)

print(pred)

df.plot()
pred.plot()

plt.show()