# create an Excel file object
'PET_PRI_SPT_S1_M.xls' 
 
# parse the first sheet
 
# rename the columns as 'Date','Brent'
 
# cut off the first 18 rows because these rows
# contain NaN values for the Brent prices


# index the data set by date

# remove the date column after re-indexing

#print df

#plot df


#############################################################################


# Create endogeneous (endog) variable from df by transforming it as an np.array
# np.asarray()

# Same for the date (endog_dates)


# build arima model
# sm.tsa.AR(endog, dates=endog_dates, freq='D or M or Y or Q')

# fit the model
# model.fit()


# Make a prediction that starts='2015-10-15' & ends='2017-01-18'
# .predict(start='date', end='date')

# transform the prediction in a pandas time series
# pd.TimeSeries()

#print prediction

#plot