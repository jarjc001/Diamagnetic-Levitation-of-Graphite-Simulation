import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('data_mag_sus.csv')

height= df["height"]*1e3
mass = df["mass_diff"]
mag_sus = df["mag_sus"]*1e6



#B = df["B"]
#B_error = df["B_error"]

#r=np.linspace(0,0.007,1000)
#m_=1737454.063
#cplus_=280.736708
#map_fit = (m_*r)+cplus_

#plt.errorbar(B,T,xerr = B_error,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)   
fig, ax = plt.subplots()    
plt.plot(height,mag_sus,'ks',markersize=6)
#ax.plot(x,zy,'k',markersize=7,label='y=x')

#plt.plot(r,map_fit,'r--',label='Trendline',linewidth=2.5)  

plt.show
plt.xlabel('z (mm)')          #labels x axis as 'r (μm)'
plt.ylabel('χ$_{v}$ (x10$^{-6}$)')    #labels y axis as 'Intensity (Wm^-2)'

plt.xlim(1.93,2.4)                 #x axis is from -25 to 25 μm
#ax.set_ylim(1.21,1.33) 

#plt.yticks([1.22,1.24,1.26,1.28,1.30,1.32])

#ax2 = plt.twinx()
#ax2.set_ylabel('E$_m$ (x10$^{-6}$ J)')
#ax2.set_ylim(1.21,1.33)

plt.xticks([2,2.1,2.2,2.3,2.4])
#plt.yticks([1.22,1.24,1.26,1.28,1.30,1.32],['3.9','4.7', '5.5', '6.3','7.1','7.9'])# '1.4'])
#plt.set_xticklabels(['7.5', '10','12.5', '15', '17.5'])

plt.axline((2, -450), (2.2, -450),color='r',linestyle="-.",linewidth=2,label="Referenced") 
plt.axline((2, -463), (2.2, -463),color='k',linestyle="-",linewidth=2,label="Mean ")
plt.axline((2, -491), (2.2, -491),color='b',linestyle="--",linewidth=2,label="Error boundaries") 
plt.axline((2, -435), (2.2, -435),color='blue',linestyle="--",linewidth=2) 

plt.tick_params(bottom=True, top=True, left=True, right=True)
plt.tick_params(axis="x", direction="in", length=5, width=1)
plt.tick_params(axis="y", direction="in", length=5, width=1)

plt.tick_params(axis='both', which='major', labelsize=12)

plt.legend()