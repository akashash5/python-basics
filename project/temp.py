import pandas as pd
xl=pd.ExcelFile('RAW FINAL CGPA Vs Package Report of 2018,2017,2016 (14-feb-18).xlsx')
sheet1=xl.parse(0)
placementPackage=sheet1['Max Package']
qp,cp=sheet1['Qualifying Marks'],sheet1['Current Course Percentage']
qp.replace('Not Available',0.0,inplace=True)
qp.fillna(0.0,inplace=True)
cp.fillna(0.0,inplace=True)
diff=cp-qp
placementPackage.fillna(0.0,inplace=True)
count=0
for i,j in zip(diff,placementPackage):
    if i>10 and (j<=6 and j>=4):
        count+=1
print(count)
        

