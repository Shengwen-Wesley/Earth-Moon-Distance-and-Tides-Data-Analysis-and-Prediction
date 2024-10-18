import pandas as pd
import numpy as np
import requests

#preparation
endpoint=f'https://api.xmltime.com/astrodata'
Date=np.array(['2013-01','2013-02','2013-03','2013-04','2013-05','2013-06','2013-07','2013-08','2013-09','2013-10','2013-11','2013-12',])

time = []
days31 = {1,3,5,7,8,10,12}
days30 = {4,6,9,11}
def incre(i,daynum):
    if i <10:
        for j in range(1,daynum):
            if j<10:
                a=('2022-0{0}-0{1}'.format(i,j))
                time.append(a)
            else:
                a=('2022-0{0}-{1}'.format(i,j))
                time.append(a)
    else:
        for j in range(1,daynum):
            if j<10:
                a=('2022-{0}-0{1}'.format(i,j))
                time.append(a)
            else:
                a=('2022-{0}-{1}'.format(i,j))
                time.append(a)

for mon in range(1,13):
    if mon in days31:
        incre(mon,32)
    elif mon in days30:
        incre(mon,31)
    else:
        incre(2,29)

#achieve the data
x=0
Data_distance={}
for i in(Date):
        distance=[]
        for j in (time[x:(x+1)]):
            for g in(j):
                params={
                    'object':'moon',
                    'accesskey':'API-KEY',
                    'secretkey':'API-KEY',
                    'placeid':'usa/new-york',
                    'version':'3',
                    }
                params['interval']=g
                responds=requests.get(endpoint,params=params).json()
                distance_data=responds["locations"][0]["astronomy"]["objects"][0]["results"][0]["distance"]
                distance.append(distance_data)
            x+=1
        Data_distance[i]=distance

#save the data to distance
df_Data_distance=pd.DataFrame(Data_distance)
df_Data_distance.to_csv('Earth-Moon Distance in 20xx.csv',index=False,encoding='utf-8')

