import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('lev_height_2x2_0degrees.csv')

x = df["x"]
zy = df["z"]*1e3
z0 = df["zy0"]


#B = df["B"]
#B_error = df["B_error"]

#r=np.linspace(0,0.007,1000)
#m_=1737454.063
#cplus_=280.736708
#map_fit = (m_*r)+cplus_

#plt.errorbar(B,T,xerr = B_error,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)   
fig, ax = plt.subplots()    
plt.plot(x,z0,'r',markersize=7,label='y=0')
ax.plot(x,zy,'k',markersize=7,label='y=x')

#plt.plot(r,map_fit,'r--',label='Trendline',linewidth=2.5)  

plt.show
plt.xlabel('x (mm)')          #labels x axis as 'r (μm)'
plt.ylabel('Levitation Height (mm)')    #labels y axis as 'Intensity (Wm^-2)'
plt.legend() 
plt.xlim(-5.5,5.5)                 #x axis is from -25 to 25 μm
ax.set_ylim(1.21,1.33) 

plt.yticks([1.22,1.24,1.26,1.28,1.30,1.32])

ax2 = plt.twinx()
ax2.set_ylabel('E$_m$ (x10$^{-6}$ J)')
ax2.set_ylim(1.21,1.33)

#plt.xticks([-4,-2,0,2],['7.5', '10','12.5', '15'])
plt.yticks([1.22,1.24,1.26,1.28,1.30,1.32],['3.9','4.7', '5.5', '6.3','7.1','7.9'])# '1.4'])
#plt.set_xticklabels(['7.5', '10','12.5', '15', '17.5'])

plt.tick_params(bottom=True, top=True, left=True, right=True)
plt.tick_params(axis="x", direction="in", length=5, width=1)
plt.tick_params(axis="y", direction="in", length=5, width=1)

plt.tick_params(axis='both', which='major', labelsize=12)