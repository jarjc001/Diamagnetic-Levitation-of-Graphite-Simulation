import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('Energy_during_rotation_3x3.csv')

rotation = df["rotation"]
energy = df["magnetic_potential_energy"]

#B = df["B"]
#B_error = df["B_error"]

#r=np.linspace(0,0.007,1000)
#m_=1737454.063
#cplus_=280.736708
#map_fit = (m_*r)+cplus_

#plt.errorbar(B,T,xerr = B_error,fmt ='ks',capsize=4, elinewidth=1.5,markersize=6,label='Points')#,label='1$^{st}$ Cluster',markersize=5)       
plt.plot(rotation,energy,'k.',markersize=5)
#plt.plot(r,map_fit,'r--',label='Trendline',linewidth=2.5)  

plt.show
plt.xlabel('Angle of Rotation (°)',fontsize=12)          #labels x axis as 'r (μm)'
plt.ylabel('Potential Energy (x10$^{-5}$ J)',fontsize=12)    #labels y axis as 'Intensity (Wm^-2)'
plt.xlim(-2.5,182.5)                 #x axis is from -25 to 25 μm
plt.ylim(1.39e-5,1.67e-5) 

plt.tick_params(bottom=True, top=True, left=True, right=True)
plt.tick_params(axis="x", direction="in", length=5, width=1)
plt.tick_params(axis="y", direction="in", length=5, width=1)

plt.xticks([0,45,90,135,180])#,['7.5', '10','12.5', '15', '17.5'])
plt.yticks([1.4e-5,1.45e-5,1.5e-5,1.55e-5,1.6e-5,1.65e-5],['1.4','1.45','1.5', '1.55','1.6','1.65'])
#plt.set_xticklabels(['7.5', '10','12.5', '15', '17.5'])