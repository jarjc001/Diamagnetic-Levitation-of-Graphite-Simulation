import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('plotting_lev_height_vs_side_legth.csv')

side = df["side_length"]
height = df["lev_height"]

#B = df["B"]
#B_error = df["B_error"]

#r=np.linspace(0,0.007,1000)
#m_=1737454.063
#cplus_=280.736708
#map_fit = (m_*r)+cplus_

#plt.errorbar(B,T,xerr = B_error,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)       
plt.plot(side,height,'ks',markersize=5)
#plt.plot(r,map_fit,'r--',label='Trendline',linewidth=2.5)  

plt.show
plt.xlabel('Side Length (mm)',fontsize=10)          #labels x axis as 'r (μm)'
plt.ylabel('Levitation Height (mm)',fontsize=10)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(0.006,0.0195)                 #x axis is from -25 to 25 μm
plt.ylim(0.00108,0.00135) 

plt.tick_params(bottom=True, top=True, left=True, right=True)
plt.tick_params(axis="x", direction="in", length=5, width=1)
plt.tick_params(axis="y", direction="in", length=5, width=1)

plt.xticks([0.0075,0.01,0.0125,0.015,0.0175],['7.5', '10','12.5', '15', '17.5'])
plt.yticks([0.0011,0.00115,0.0012,0.00125,0.0013],['1.1','1.15', '1.2','1.25','1.3'])# '1.4'])
#plt.set_xticklabels(['7.5', '10','12.5', '15', '17.5'])