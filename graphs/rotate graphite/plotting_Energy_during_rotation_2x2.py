import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('Energy_during_rotation_2x2.csv')

rotation = df["rotation"]
energy = df["magnetic_potential_energy"]

#B = df["B"]
#B_error = df["B_error"]

#r=np.linspace(0,0.007,1000)
#m_=1737454.063
#cplus_=280.736708
#map_fit = (m_*r)+cplus_

#plt.errorbar(B,T,xerr = B_error,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)       
plt.plot(rotation,energy,'k',markersize=5)
#plt.plot(r,map_fit,'r--',label='Trendline',linewidth=2.5)  

plt.show
plt.xlabel('Angle of Rotation (°)',fontsize=12)          #labels x axis as 'r (μm)'
plt.ylabel('E$_m$ (x10$^{-6}$ J)',fontsize=12)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(-2.5,182.5)                 #x axis is from -25 to 25 μm
plt.ylim(6.45e-6,7.45e-6) 

plt.tick_params(bottom=True, top=True, left=True, right=True)
plt.tick_params(axis="x", direction="in", length=5, width=1)
plt.tick_params(axis="y", direction="in", length=5, width=1)

plt.xticks([0,45,90,135,180])#,['7.5', '10','12.5', '15', '17.5'])
plt.yticks([6.6e-6,6.8e-6,7e-6,7.2e-6,7.4e-6],['6.6','6.8', '7.0','7.2','7.4'])
#plt.set_xticklabels(['7.5', '10','12.5', '15', '17.5'])