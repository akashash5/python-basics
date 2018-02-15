import numpy as np
 
n=1000
x= np.random.uniform(low=50.0, high=100.0, size=(n,))
y= np.random.uniform(low=50.0, high=100.0, size=(n,))
import plotly
plotly.tools.set_credentials_file(username='akash.ash5', api_key='I1SgtDUZ6FDPQPEZ9Z12')
import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Heatmap(z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]])
data=[trace]
py.plot(data, filename='basic-heatmap')
