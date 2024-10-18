#Data Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from natsort import natsorted 

#import the data
Raw_data_distance=pd.read_csv("F:\\Final Project\\Datasets\\Earth-Moon Distance From 2012 to 2022\\Earth-Moon Distance in 2022.csv",encoding='utf-8')
Row_data_tides_file=os.listdir("F:\\Final Project\\Datasets\\2022TIdesData")
Row_data_tides_file=natsorted(Row_data_tides_file)

#Preparation
All_data_tides_time=[]
All_data_tides_level=[]
x=0
for i in(Row_data_tides_file):
    read_csv=pd.read_csv("F:\\Final Project\\Datasets\\2022TIdesData\\"+Row_data_tides_file[x])
    read_csv_1=read_csv['Date'].copy()
    read_csv_1.to_string()
    read_csv_2=read_csv['Time (GMT)'].copy()
    read_csv_3=(read_csv_1+' '+read_csv_2).astype('datetime64')
    All_data_tides_time.append(read_csv_3)
    All_data_tides_level.append(read_csv['Verified (ft)'])
    x+=1
All_data_tides_time=pd.concat(All_data_tides_time)
All_data_tides_level=pd.concat(All_data_tides_level)

time=[]
for i in range(1,13):
    if i<10:
        for j in range(1,32):
            if j<10:
                a=('2022-0{0}-0{1}'.format(i,j))
                time.append(a)
            else:
                a=('2022-0{0}-{1}'.format(i,j))
                time.append(a)
    else:
        for j in range(1,32):
            if j<10:
                a=('2022-{0}-0{1}'.format(i,j))
                time.append(a)
            else:
                a=('2022-{0}-{1}'.format(i,j))
                time.append(a)

All_data_distance_pre=[]
for i in (Raw_data_distance.values):
    All_data_distance_pre.extend(i)

All_data_distance=[]
for a in(All_data_distance_pre):
    value=a/100000
    All_data_distance.append(value)


#Visualization
fig,ax1=plt.subplots()
fig.set_figwidth(20)
fig.set_figheight(8)
ax1.plot(time,All_data_distance,c='r',label='Earth-Moon Distance')
plt.legend(loc= 2,fontsize=10)
plt.ylabel('Distance x100000(Km) | Height OF Tides(m)',fontsize=20)
plt.xlabel('Date',fontsize=20)
plt.xticks(range(0,367,31))
ax2=ax1.twiny()
ax2.plot(All_data_tides_time,All_data_tides_level,linewidth=0.5,label='Height of Tides')
plt.legend(loc= 1,fontsize=10)
ax2.xaxis.set_visible(False)
plt.title('Earth-Moon Distance And Height of Tides in 2022',fontsize=20)
plt.show()




















