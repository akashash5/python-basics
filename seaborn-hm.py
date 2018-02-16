import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
n=1000
x= np.random.uniform(low=50.0, high=100.0, size=(n,2))

sns.heatmap(x,cmap='RdYlGn')
plt.show()
