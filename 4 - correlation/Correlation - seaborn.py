import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from io import BytesIO
from pandas import read_csv

sns.set(style="white")

kw = dict(na_values='NaN', sep=',', encoding='utf-8',
          skipinitialspace=True, index_col=False)

df = read_csv("fish.csv", **kw)

df.head()

# Compute the correlation matrix
corr = df.corr()

corr

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)


# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
            square=True, xticklabels=5, yticklabels=5,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)


plt.show()

