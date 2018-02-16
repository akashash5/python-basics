import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' }) 

print(df2)
print(df2.dtypes)
print(df2.head())
print(df2.tail())
print(df2.index)
print(df2.columns)
print(df.describe())
print(df2.t)
print(df.sort_index(axis=1, ascending=False))
print(df['A'])
print(df[0:3])
print(df.loc[dates[0]])
print(df.loc['20130102':'20130104',['A','B']])
print(df.iloc[[1,2,4],[0,2]])
print(df[df.A > 0])
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print(s1)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print(df1)
df1.dropna(how='any')
df1.fillna(value=5)
pd.isna(df1)
print(df.mean())
print(df.mean(1))
print(df.apply(np.cumsum))
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())
print()