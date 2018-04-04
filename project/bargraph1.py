import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
xl=pd.ExcelFile('CGPA VS Package 2018 batch Report CLEAN.xlsx')
sheet1=xl.parse(0)
chg=sheet1['Change']
datax=[-25,-20,-15,-10,-5,0,5,10,15,20]
labels=['less than -20','-20 to -15','-15 to -10','-10 to -5','-5 to 0','0 to 5','5 to 10','10 to 15','15 to 20','more than 20']
data=list([0]*10)
for i in chg:
    if i<-20:
        data[0]-=1
    elif i<-15 and i>=-20:
        data[1]-=1
    elif i<-10 and i>=-15:
        data[2]-=1
    elif i<-5 and i>=-10:
        data[3]-=1
    elif i<0 and i>=-5:
        data[4]-=1
    elif i<5 and i>=0:
        data[5]+=1
    elif i<10 and i>=5:
        data[6]+=1
    elif i<15 and i>=10:
        data[7]+=1
    elif i<=20 and i>=15:
        data[8]+=1
    elif i>20:
        data[9]+=1
    else:
        print('errorsome value')
colors=['r','r','r','r','r','g','g','g','g','g']
print(data)
datap=[]
for i in data:
    datap.append(abs(i)*100/len(chg))
print(datap)
plt.bar(datax, data, width=1, color=colors)
plt.xticks(datax,labels)
plt.title('percent change graph 2018')
plt.show()
