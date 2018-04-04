import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
xl=pd.ExcelFile('CGPA VS Package 2018 batch Report CLEAN.xlsx')
sheet1=xl.parse(0)
chg=sheet1['Change']
datax=[-1,0,1]
labels=['Negative change','No change','Positive change']
data=list([0]*3)
for i in chg:
    if i<0:
        data[0]-=1
    elif i==0.0:
        data[1]+=1
    elif i>0:
        data[2]+=1
    else:
        print('errorsome value')
colors=['r','g','g']
print(data)
datap=[]
for i in data:
    datap.append(abs(i)*100/len(chg))
print(datap)
plt.bar(datax, data, width=1, color=colors)
plt.xticks(datax,labels)
plt.title('percent change graph 2018')
plt.show()
