
# coding: utf-8

# This file is for generating any graphs for my dissertation.

# In[14]:


import matplotlib.pyplot as plt
import numpy as np
import pylab
from matplotlib import pyplot
import seaborn
import math
from matplotlib.gridspec import GridSpec


# In[19]:


plt.rcParams.update({'font.size': 11})
#plt.rcParams['xtick.labelsize']=20
#plt.rcParams['ytick.labelsize']=8

x = np.linspace(-1, 16, 100)
y = 4*(x**3) - 120*(x**2) + 864*x
q = 12*(x**2) - 240*(x) + 864
z = x**2 - 20*x + 72

fig, ax = plt.subplots()
ax.plot(x, q, 'mediumblue', linewidth = 2)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
#ax.axvline(10-2*math.sqrt(7),linewidth=2, color='red')
ax.axvline(linewidth=2, color='black')
ax.annotate("$V'(x) = 12x^2 - 240x + 864$", xy=(130, 150), xycoords='figure points', color = 'mediumblue')
#ax.annotate('x = 10 - 2$\sqrt{7}$', xy=(75, 75), xycoords='figure points', color = 'red')
ax.set_xlim([-1,17])

pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("V '(x)", fontsize = 14)

fig.savefig('final_optimisation_differentiated.png', transparent=True)

pyplot.show()


# In[11]:


fig, ax = plt.subplots()
ax.plot(x, y, 'red')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')
#ax.axvline(10-2*math.sqrt(7), color='red', linewidth = 2)
#ax.annotate('$V(x) = 4x^3 - 120x^2 + 864x$', xy=(240, 200), xycoords='figure points', color = 'mediumblue')
#ax.annotate('x = 10 - 2$\sqrt{7}$', xy=(165, 60), xycoords='figure points', color = 'red')
ax.set_xlim([-1,30])
ax.set_ylim([-700,2500])

pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("V(x)", fontsize = 14)

plt.show()

fig.savefig('final_optimisation_normal.png', transparent=True)


# In[4]:


x = np.arange(0, 21,0.01)
y = 36 - 2*x
z = 24 - 2*x

fig, ax = plt.subplots()
ax.plot(x, y, 'mediumblue', linewidth = 2)
#pyplot.title("Length")
ax.annotate('$L(x) = 36-2x$', xy=(190, 185), xycoords='figure points', color = 'mediumblue')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2,color='black')
plt.axvline(linewidth=2,color='black')
ax.set_xlim([-2,20])
ax.set_ylim([-20,50])
ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])


pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("Length", fontsize = 14)

plt.show()

fig.savefig('optimisation_length.png', transparent=True)


# In[5]:


x = np.linspace(0, 21,100)
y = 36 - 2*x
z = 24 - 2*x

fig, ax = plt.subplots()
ax.plot(x, z, 'red', linewidth = 2)
#pyplot.title("Width")
ax.annotate('$W(x) = 24-2x$', xy=(180, 170), xycoords='figure points', color = 'red')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2,color='black')
plt.axvline(linewidth=2,color='black')
ax.set_ylim([-20,50])
ax.set_xlim([-2,20])


pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("Width", fontsize = 14)

plt.show()

fig.savefig('optimisation_width.png', transparent=True)


# In[6]:


a = np.linspace(0, 3.46, 100)
b = (16 - a**2)**(1/2)
fig, ax = plt.subplots()
ax.plot(b, a, 'mediumblue', linewidth = 2)
#pyplot.title("Ladder Distance")
ax.annotate('a = $\sqrt{16-b^2}$', xy=(170, 202), xycoords='figure points', color = 'mediumblue', fontsize = 12)


ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')

pyplot.xlabel("b", fontsize = 14)
pyplot.ylabel("a", fontsize = 14)
ax.set_ylim([-1,6])
ax.set_xlim([-1,5])

plt.show()

fig.savefig('final_ladderxy.png', transparent=True)


# In[7]:


dadb = (-2*b)/(16 - b**2)**(1/2)

fig, ax = plt.subplots()
ax.plot(b, dadb, 'crimson')
pyplot.title("$da/db$")
ax.annotate('$da/db = -2b /\sqrt{16-b^2}$', xy=(120, 145), xycoords='figure points', color = 'crimson', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("b", fontsize = 14)
pyplot.ylabel("da/db", fontsize = 14)
ax.set_ylim([-8,2])
ax.set_xlim([-1,5])

plt.show()

fig.savefig('final_ladderxy_differentiated.png', transparent=True)


# In[8]:


t = np.linspace(0, 7, 100)
a = 3.46 - 0.6*t

fig, ax = plt.subplots()
ax.plot(t, a, 'mediumblue')
pyplot.title("a over time")
ax.annotate('$a = 3.46 - 0.6t$', xy=(200, 190), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Time (seconds)", fontsize = 14)
pyplot.ylabel("a (meters)", fontsize = 14)
ax.set_ylim([-1,5])
ax.set_xlim([-1,7])

plt.show()

fig.savefig('ladder_y_over_time.png', transparent=True)


# In[9]:


#plot dx/dt
t = np.linspace(0, 5.766666, 100)
b = (16 - (3.46 - 0.6*t)**2)**(1/2) 

fig, ax = plt.subplots()
ax.plot(t, b, 'crimson')
pyplot.title("b over time")
ax.annotate('$b = 3.46 - 0.6t$', xy=(200, 170), xycoords='figure points', color = 'crimson', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Time (seconds)", fontsize = 14)
pyplot.ylabel("b (meters)", fontsize = 14)
ax.set_ylim([-1,5])
ax.set_xlim([-1,7])

plt.show()

fig.savefig('ladder_b_over_time.png', transparent=True)


# In[10]:


t = np.linspace(0, 12, 100)
Volume = 4*t

fig, ax = plt.subplots()
ax.plot(t, Volume, 'mediumblue')
pyplot.title("Volume over Time")
ax.annotate('$V(t) = 4(t)$', xy=(190, 110), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Time(minutes)", fontsize = 14)
pyplot.ylabel("Volume($m^3$)", fontsize = 14)
#ax.set_ylim([-8,2])
#ax.set_xlim([-1,6])

plt.show()

fig.savefig('volume_over_time.png', transparent=True)


# In[11]:


radius = np.linspace(0, 17, 100)
Volume2 = math.pi*(radius**2)*0.1

fig, ax = plt.subplots()
ax.plot(radius, Volume2, 'mediumblue')
pyplot.title("Volume against Radius")
ax.annotate("$V(r) = 0.1\u03C0r^2$", xy=(170, 140), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Radius(m)", fontsize = 14)
pyplot.ylabel("Volume($m^3$)", fontsize = 14)
#ax.set_ylim([-8,2])
#ax.set_xlim([-1,6])

plt.show()

fig.savefig('volume_against_radius.png', transparent=True)


# In[12]:


dvdr = 2*0.1*math.pi*radius

fig, ax = plt.subplots()
ax.plot(radius, dvdr, 'mediumblue')
pyplot.title("Rate of Change of Volume wrt Radius")
ax.annotate("$dV/dr = 0.2\u03C0r$", xy=(230, 140), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Radius(m)", fontsize = 14)
pyplot.ylabel("dV/dr", fontsize = 14)
#ax.set_ylim([-8,2])
#ax.set_xlim([-1,6])

plt.show()

fig.savefig('rate_volume_wrt_radius.png', transparent=True)


# In[13]:


t = np.linspace(0,12, 100)
drdt = 4/(0.2)*math.pi*radius

fig, ax = plt.subplots()
ax.plot(t, drdt, 'mediumblue')
pyplot.title("Rate of Change of Radius")
ax.annotate("$dr/dt = 4/0.2\u03C0r$", xy=(135, 180), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Time(minutes)", fontsize = 14)
pyplot.ylabel("dr/dt", fontsize = 14)
#ax.set_ylim([-8,2])
#ax.set_xlim([-1,6])

plt.show()

fig.savefig('rate_change_radius_time.png', transparent=True)


# In[14]:


dAdr = 2*math.pi*radius

fig, ax = plt.subplots()
ax.plot(radius, dAdr, 'mediumblue')
pyplot.title("Rate of Change of Area wrt Radius")
ax.annotate("$dA/dr = 2\u03C0r$", xy=(135, 180), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Radius(m)", fontsize = 14)
pyplot.ylabel("dA/dr", fontsize = 14)
#ax.set_ylim([-8,2])
#ax.set_xlim([-1,6])

plt.show()

fig.savefig('rate_change_area_radius.png', transparent=True)


# In[15]:


dAdt = 40*t

fig, ax = plt.subplots()
ax.plot(t, dAdt, 'mediumblue')
pyplot.title("Rate of Change of Area")
ax.annotate("$dA/dt = 40(t)$", xy=(135, 180), xycoords='figure points', color = 'mediumblue', fontsize = 12)

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=1, color='black')
plt.axvline(linewidth=1, color='black')

pyplot.xlabel("Time(minutes)", fontsize = 14)
pyplot.ylabel("dA/dt", fontsize = 14)
#ax.set_ylim([-8,2])
#ax.set_xlim([-1,6])

plt.show()

fig.savefig('rate_change_area_time.png', transparent=True)


# In[16]:


x = np.linspace(-5, 5, 100)
y = -4*x**3 + 3*x**2 + 25*x + 6
fig, ax = plt.subplots()
ax.plot(x, y, 'mediumblue')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')
#ax.axvline(-1.215, color='red', linewidth = 2)
#ax.axvline(1.715, color='red', linewidth = 2)
#ax.annotate('$y = 4x^3 + 3x^2 + 25x + 6$', xy=(240, 200), xycoords='figure points', color = 'mediumblue')
#ax.annotate('x = -1.215$', xy=(165, 60), xycoords='figure points', color = 'red')
ax.set_xlim([-4,4])
ax.set_ylim([-50,50])

pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("y", fontsize = 14)

plt.show()

fig.savefig('final_Theory_cubed.png', transparent=True)


# In[17]:


q = np.linspace(-5, 5, 100)
r = -12*q**2 + 6*q + 25
fig, ax = plt.subplots()
ax.plot(q, r, 'mediumblue')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')
#ax.axvline(-1.215, color='red', linewidth = 2)
#ax.axvline(1.715, color='red', linewidth = 2)
#ax.annotate('$y = 4x^3 + 3x^2 + 25x + 6$', xy=(240, 200), xycoords='figure points', color = 'mediumblue')
#ax.annotate('x = -1.215$', xy=(165, 60), xycoords='figure points', color = 'red')
ax.set_xlim([-4,4])
ax.set_ylim([-50,50])

pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("f '(x)", fontsize = 14)

plt.show()

fig.savefig('final_Theory_squared.png', transparent=True)


# In[18]:


s = np.linspace(-5, 5, 100)
t = -24*s + 6
fig, ax = plt.subplots()
ax.plot(s, t, 'mediumblue')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
plt.axvline(linewidth=2, color='black')
#ax.axvline(-1.215, color='red', linewidth = 2)
#ax.axvline(1.715, color='red', linewidth = 2)
#ax.annotate('$y = 4x^3 + 3x^2 + 25x + 6$', xy=(240, 200), xycoords='figure points', color = 'mediumblue')
#ax.annotate('x = -1.215$', xy=(165, 60), xycoords='figure points', color = 'red')
ax.set_xlim([-4,4])
ax.set_ylim([-50,50])

pyplot.xlabel("x", fontsize = 14)
pyplot.ylabel("f ''(x)", fontsize = 14)

plt.show()

fig.savefig('final_Theory_line.png', transparent=True)


# In[92]:


fig, ax = plt.subplots()
#ax.plot(s, t, 'mediumblue')
ax.plot(x, y, 'mediumblue')
ax.plot(q, r, 'crimson')

ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='black', labelsize='small', width=2)
plt.axhline(linewidth=2, color='black')
plt.axvline(-1.23, linewidth=2, color='teal', linestyle = '-', ymin = 0.3, ymax = 0.6)
plt.axvline(1.7, linewidth=2, color='teal', linestyle = '-', ymin = 0.4, ymax = 0.95)
#ax.axvline(-1.215, color='red', linewidth = 2)
#ax.axvline(1.715, color='red', linewidth = 2)
ax.annotate('f $(x) = 4x^3 + 3x^2 + 25x + 6$', xy=(125, 230), xycoords='figure points', color = 'mediumblue', fontsize = 12)
ax.annotate("f '$(x) = 12x^2 + 6x +25$", xy=(160, 50), xycoords='figure points', color = 'red', fontsize = 12)
ax.set_xlim([-4,4])
ax.set_ylim([-50,50])

#pyplot.xlabel("x", fontsize = 14)
#pyplot.ylabel("f ''(x)", fontsize = 14)

fig.savefig('TheoryExample.png')
plt.show()


# Below I generate the plots for showing user engagement data.

# In[20]:


FA1 = [3,4,5,3,4,3]
FA2 = [3,4,4,4,5,3]
FA3 = [2,3,3,5,4,4]
FA4 = [2,5,4,4,4,4]
FA5 = [3,4,4,3,4,4]
FA6 = [5,4,4,4,4,4]
FA7 = [3,4,4,4,3,3]
PU1 = [5,5,5,3,5,3]
PU2 = [5,4,5,2,5,3]
PU3 = [5,5,5,4,5,4]
PU4 = [5,5,5,4,5,5]
PU5 = [5,5,5,5,5,3]
PU6 = [3,5,5,4,4,5]
PU7 = [5,4,4,3,4,2]
PU8 = [5,4,3,3,4,3]
AE1 = [5,4,5,3,3,5]
AE2 = [5,4,3,4,5,4]
AE3 = [5,4,4,4,5,5]
AE4 = [5,4,4,5,4,5]
AE5 = [5,4,4,4,3,4]
RW1 = [5,4,4,4,5,4]
RW2 = [5,4,5,4,5,4]
RW3 = [5,5,5,4,5,3]
RW4 = [5,4,3,4,4,3]
RW5 = [5,4,5,4,5,4]
RW6 = [5,5,3,3,4,3] #no_1 emphasised curiosity element
RW7 = [5,5,5,4,5,4]
RW8 = [5,5,5,4,5,4]
RW9 = [5,5,5,4,4,5]
RW10 = [5,5,5,4,5,5]

engage_data = [FA1, FA2, FA3, FA4, FA5, FA6, FA7, PU1, PU2, PU3,
               PU4, PU5, PU6, PU7, PU8, AE1, AE2, AE3, AE4, AE5, RW1,
               RW2, RW3, RW4, RW5, RW6, RW7, RW8, RW9, RW10]

focused_attention = [FA1, FA2, FA3, FA4, FA5, FA6, FA7]

perceived_usability = [PU1, PU2, PU3, PU4, PU5, PU6, PU7, PU8]

aesthetic_appeal = [AE1, AE2, AE3, AE4, AE5]

reward_factor = [RW1, RW2, RW3, RW4, RW5, RW6, RW7, RW8, RW9, RW10]


# In[82]:


from __future__ import division


# In[75]:


FA1_average = np.mean(FA1)
print("FA1 Average = {0}".format(FA1_average))
FA2_average = np.mean(FA2)
print("FA2 Average = {0}".format(FA2_average))
FA3_average = np.mean(FA3)
print("FA3 Average = {0}".format(FA3_average))
FA4_average = np.mean(FA4)
print("FA4 Average = {0}".format(FA4_average))
FA5_average = np.mean(FA5)
print("FA5 Average = {0}".format(FA5_average))
FA6_average = np.mean(FA6)
print("FA6 Average = {0}".format(FA6_average))
FA7_average = np.mean(FA7)
print("FA7 Average = {0}".format(FA7_average)) 

FA_average = np.mean([FA1_average, FA2_average, FA3_average,
                     FA4_average, FA5_average, FA6_average,
                     FA7_average])
print("Focused Attention Overall Score: {0}".format(FA_average))

FA_std = np.std([FA1_average, FA2_average, FA3_average,
                     FA4_average, FA5_average, FA6_average,
                     FA7_average])
print("Focused Attention Standard Deviation: {0}".format(FA_std))


# In[76]:


PU1_average = np.mean(PU1)
print("PU1 Average = {0}".format(PU1_average))
PU2_average = np.mean(PU2)
print("PU2 Average = {0}".format(PU2_average))
PU3_average = np.mean(PU3)
print("PU3 Average = {0}".format(PU3_average))
PU4_average = np.mean(PU4)
print("PU4 Average = {0}".format(PU4_average))
PU5_average = np.mean(PU5)
print("PU5 Average = {0}".format(PU5_average))
PU6_average = np.mean(PU6)
print("PU6 Average = {0}".format(PU6_average))
PU7_average = np.mean(PU7)
print("PU7 Average = {0}".format(PU7_average))
PU8_average = np.mean(PU8)
print("PU8 Average = {0}".format(PU8_average))

PU_average = np.mean([PU1_average, PU2_average, PU3_average,
                     PU4_average, PU5_average, PU6_average,
                     PU7_average, PU8_average])
print("Perceived Usability Overall Score: {0}".format(PU_average))

PU_std = np.std([PU1_average, PU2_average, PU3_average,
                     PU4_average, PU5_average, PU6_average,
                     PU7_average, PU8_average])
print("Perceived Usability Standard Deviation: {0}".format(PU_std))


# In[77]:


AE1_average = np.mean(AE1)
print("AE1 Average = {0}".format(AE1_average))
AE2_average = np.mean(AE2)
print("AE2 Average = {0}".format(AE2_average))
AE3_average = np.mean(AE3)
print("AE3 Average = {0}".format(AE3_average))
AE4_average = np.mean(AE4)
print("AE4 Average = {0}".format(AE4_average))
AE5_average = np.mean(AE5)
print("AE5 Average = {0}".format(AE5_average))

AE_average = np.mean([AE1_average, AE2_average, AE3_average,
                     AE4_average, AE5_average])
print("Aesthetic Appeal Overall Score: {0}".format(AE_average))

AE_std = np.std([AE1_average, AE2_average, AE3_average,
                     AE4_average, AE5_average])
print("Aesthetic Appeal Standard Deviation: {0}".format(AE_std))


# In[74]:


RW1_average = np.mean(RW1)
print("RW1 Average = {0}".format(RW1_average))
RW2_average = np.mean(RW2)
print("RW2 Average = {0}".format(RW2_average))
RW3_average = np.mean(RW3)
print("RW3 Average = {0}".format(RW3_average))
RW4_average = np.mean(RW4)
print("RW4 Average = {0}".format(RW4_average))
RW5_average = np.mean(RW5)
print("RW5 Average = {0}".format(RW5_average))
RW6_average = np.mean(RW6)
print("RW6 Average = {0}".format(RW6_average))
RW7_average = np.mean(RW7)
print("RW7 Average = {0}".format(RW7_average))
RW8_average = np.mean(RW8)
print("RW8 Average = {0}".format(RW8_average))
RW9_average = np.mean(RW9)
print("RW9 Average = {0}".format(RW9_average))
RW10_average = np.mean(RW10)
print("RW10 Average = {0}".format(RW10_average))

RW_average = np.mean([RW1_average, RW2_average, RW3_average,
                     RW4_average, RW5_average, RW6_average, RW7_average, RW8_average, RW9_average, RW10_average])
RW_std = np.std([RW1_average, RW2_average, RW3_average,
                     RW4_average, RW5_average, RW6_average, RW7_average, RW8_average, RW9_average, RW10_average])
print("Reward Factor Overall Score: {0}".format(RW_average))
print("Reward Factor Standard Deviation: {0}".format(RW_std))


# In[81]:


fig = plt.figure(figsize = (16, 10))

FA_means = (FA1_average, FA2_average, FA3_average, FA4_average, FA5_average, FA6_average, FA7_average)
PU_means = (PU1_average, PU2_average, PU3_average, PU4_average, PU5_average, PU6_average, PU7_average, PU8_average)
AE_means = (AE1_average, AE2_average, AE3_average, AE4_average, AE5_average)
RW_means = (RW1_average, RW2_average, RW3_average, RW4_average, RW5_average,
            RW6_average, RW7_average, RW8_average, RW9_average,RW10_average)

width = 0.7  #the width of the bars
ind_FA = np.arange(len(FA_means))  #the x locations for the groups
ind_PU = np.arange(len(PU_means))
ind_AE = np.arange(len(AE_means))
ind_RW = np.arange(len(RW_means))

ax1 = fig.add_subplot(221)
ax1.set_ylabel('Scores', fontsize = '16')
ax1.set_title('Focused Attention Scores by Item', fontsize = '16')
ax1.set_xticks(ind_FA)
ax1.set_xticklabels(('FA1', 'FA2', 'FA3', 'FA4', 'FA5', 'FA6', 'FA7'))
ax1.set_ylim(0, 6)
ax1.legend()

ax2 = fig.add_subplot(222)
ax2.set_ylabel('Scores', fontsize = '16')
ax2.set_title('Perceived Usability Scores by Item', fontsize = '16')
ax2.set_xticks(ind_PU)
ax2.set_xticklabels(('PU1', 'PU2', 'PU3', 'PU4', 'PU5', 'PU6', 'PU7', 'PU8'))
ax2.set_ylim(0, 6)
ax2.legend()

ax3 = fig.add_subplot(223)
ax3.set_ylabel('Scores', fontsize = '16')
ax3.set_title('Aesthetic Appeal Scores by Item', fontsize = '16')
ax3.set_xticks(ind_AE)
ax3.set_xticklabels(('AE1', 'AE2', 'AE3', 'AE4', 'AE5'))
ax3.set_ylim(0, 6)
ax3.legend()

ax4 = fig.add_subplot(224)
ax4.set_ylabel('Scores', fontsize = '16')
ax4.set_title('Focused Attention Scores by Item', fontsize = 16)
ax4.set_xticks(ind_RW)
ax4.set_xticklabels(('RW1', 'RW2', 'RW3', 'RW4', 'RW5', 'RW6', 'RW7', 'RW8', 'RW9', 'RW10'))
ax4.set_ylim(0, 6)
ax4.legend()

rects1 = ax1.bar(ind_FA, FA_means, width,
                color='teal')
rects2 = ax2.bar(ind_PU, PU_means, width,
                color='firebrick')
rects3 = ax3.bar(ind_AE, AE_means, width,
                color='goldenrod')
rects4 = ax4.bar(ind_RW, RW_means, width,
                color='darkgreen')

fig.savefig('UE_Bar_Graphs')
plt.show()


# In[80]:


plt.figure(figsize = (8, 5))

subset_means, subset_std = (FA_average, PU_average, AE_average, RW_average), (FA_std, PU_std, AE_std, RW_std)
width = 0.7  #the width of the bars
ind_average = np.arange(len(subset_means))  #the x locations for the groups

plt.ylabel('Scores', fontsize = '16')
plt.title('Focused Attention Scores by Item', fontsize = '16')
plt.xticks(ind_average, ('FA', 'PU', 'AE', 'RW'))
plt.ylim(0, 6)
plt.legend()

rects_average = plt.bar(ind_average, subset_means, width, yerr=subset_std,
                color=['teal', 'firebrick', 'goldenrod', 'darkgreen'])
plt.savefig('UE_averages_chart')
plt.show()

