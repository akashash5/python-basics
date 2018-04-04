import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
xl=pd.ExcelFile('CGPA VS Package 2018 batch Report CLEAN.xlsx')
sheet1=xl.parse(0)
x=sheet1['Qualifying Marks']
y=sheet1['Current Course Percentage']
color=sheet1['Color']
plt.scatter(x,y,c=color,s=0.8)
plt.xlabel('Qualifying percentage')
plt.ylabel('Present Percentage')
plt.title('Scatter plot 2018')
plt.xlim(0.0,100.0)
plt.ylim(0.0,100.0)
plt.show()
