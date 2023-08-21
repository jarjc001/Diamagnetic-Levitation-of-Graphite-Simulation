import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('res_torque2.csv')

rotation = df["rotation"]
tx = df["torque_x"]
ty = df["torque_y"]
tz = df["torque_z"]

#B = df["B"]
#B_error = df["B_error"]

#r=np.linspace(0,0.007,1000)
#m_=1737454.063
#cplus_=280.736708
#map_fit = (m_*r)+cplus_

#plt.errorbar(B,T,xerr = B_error,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)       
plt.plot(rotation,tx,'r-.',markersize=12,label='τ$^{x}$')
plt.plot(rotation,ty,'b:',markersize=12,label='τ$^{y}$')
plt.plot(rotation,tz,'k',markersize=12,label='τ$^{z}$')
#plt.plot(r,map_fit,'r--',label='Trendline',linewidth=2.5)  

plt.show
plt.legend(fontsize=10) 
plt.xlabel('Angle of Rotation (°)',fontsize=11)          #labels x axis as 'r (μm)'
plt.ylabel('τ (x10$^{-7}$ Nm)',fontsize=11)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(0,90)                 #x axis is from -25 to 25 μm
#plt.ylim(6.45e-6,7.45e-6) 

plt.tick_params(bottom=True, top=True, left=True, right=True)
plt.tick_params(axis="x", direction="in", length=5, width=1)
plt.tick_params(axis="y", direction="in", length=5, width=1)

plt.xticks([15,30,45,60,75,90])#,['7.5', '10','12.5', '15', '17.5'])
plt.yticks([-9e-7,-6e-7,-3e-7,0e-7,3e-7,6e-7,9e-7],['-9','-6', '-3','0','3','6','9'])
#plt.set_xticklabels(['7.5', '10','12.5', '15', '17.5'])