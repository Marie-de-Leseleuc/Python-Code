import pandas as pd
from pandas import DataFrame

df = pd.read_csv('sp500_ohlc.csv', index_col = 'Date', parse_dates=True)
df['H-L'] = df.High - df.Low

# data
print(df.head(3).to_string())

#stats
print(df.describe())

# corelation (pearson)
print(df.corr())

#covariance (non normalized like correlation)
print(df.cov())

#specific columns
print( df[['Volume','H-L']].corr())