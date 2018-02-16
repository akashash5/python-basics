import pandas as pd
import seaborn as sbn
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('studentData.csv',index_col=0,header=0)
print(df)
dfm=df[['QualifyingP','PresentP']]
print(dfm)
sbn.heatmap(dfm,cmap="RdYlGn")
plt.show()
