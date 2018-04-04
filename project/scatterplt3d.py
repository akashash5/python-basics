import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
xl=pd.ExcelFile('CGPA VS Package 2018 batch Report CLEAN.xlsx')
sheet1=xl.parse(0)
x=sheet1['Qualifying Marks']
y=sheet1['Current Course Percentage']
z=sheet1['Max Package']
size=sheet1['Max Package']**2
color=sheet1['Color']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z,c=color,s=size)
ax.set_xlabel('Qualifying percentage')
ax.set_ylabel('Present Percentage')
ax.set_zlabel('Package')
plt.title('3d Scatter plot 2018')
plt.xlim(0.0,100.0)
plt.ylim(0.0,100.0)
plt.show()
