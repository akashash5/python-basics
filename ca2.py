url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

import pandas as pd
df=pd.read_csv(url,header=None)
print(df.head(5))
df2=df.dropna()
print(df2.head(5))
df2=df.fillna(0)
print(df2.head(5))
