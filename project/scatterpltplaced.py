import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
xl=pd.ExcelFile('CGPA VS Package 2018 batch Report CLEAN.xlsx')
sheet1=xl.parse(0)
x=sheet1['Qualifying Marks']
y=sheet1['Current Course Percentage']
p=sheet1['No of Placement Offers']
chg=sheet1['Change']
p.fillna(0.0,inplace=True)
color=[]
for i,j in zip(chg,p):
    if i<0 and j<=0.0:
        color.append([1.0,0.0,0.0])
    elif i<0 and j>0.0:
        color.append([1.0,0.549,0.0])
    elif i>0 and j>0:
        color.append([0.0,0.0,1.0])
    elif i>0 and j<=0.0:
        color.append([0.0,1.0,1.0])
    elif i==0.0 and j==0.0:
        color.append([1.0,1.0,0.0])
    else:
        print(i,j,'errorsome value')
plt.scatter(x,y,c=color,s=2.0,alpha=0.5)
plt.xlabel('Qualifying percentage')
plt.ylabel('Present Percentage')
plt.title('Scatter plot 2018')
plt.xlim(0.0,100.0)
plt.ylim(0.0,100.0)
plt.show()
