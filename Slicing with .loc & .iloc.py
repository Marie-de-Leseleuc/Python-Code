

import pandas as pd
import numpy as np
df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
                   'B': 'one one two three two two one three'.split(),
                   'C': np.arange(8), 'D': np.arange(8) * 2})
print(df)
#      A      B  C   D
# 0  foo    one  0   0
# 1  bar    one  1   2
# 2  foo    two  2   4
# 3  bar  three  3   6
# 4  foo    two  4   8
# 5  bar    two  5  10
# 6  foo    one  6  12
# 7  foo  three  7  14

print(df.loc[df['A'] == 'foo'].iloc[[2]])

print df["C"]*2


#DataFrame has a private function _slice() to slice the DataFrame, and it allows the parameter axis to determine which axis to slice. 
#The __getitem__() for DataFrame doesn't set the axis while invoking _slice(). So the _slice() slice it by default axis 0.
# You can take a simple experiment, that might help you:

print df._slice(slice(0, 2))
print df._slice(slice(0, 2), 0)
print df._slice(slice(0, 2), 1)



"""
def multiply_num(col):
    for i in col:
        return i*2
   
print df[df['A'] == 'foo'] """