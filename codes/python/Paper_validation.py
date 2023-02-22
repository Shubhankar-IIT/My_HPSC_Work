#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

y1=[-0.342,-0.345,-0.338] #back wall
y2=[-0.402,-0.366,-0.340] #left wall
y3=[-0.331,-0.334,-0.362] #right wall
x =['Chanakya et al','DO model','MC model']
# In[30]:


plt.plot(x,y1,label='Back wall',linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=10)
plt.plot(x,y2,label='Left wall',linewidth = 3,
         marker='s', markerfacecolor='red', markersize=10)
plt.plot(x,y3,label='Right wall', linewidth = 3,
         marker='v', markerfacecolor='green', markersize=10)
plt.ylim(-0.60,-0.10)
plt.ylabel("Area average Nusselt number on different walls")
plt.legend()
plt.show()


# In[40]:


y5=[1.058,1.125,1.114] #bottom wall
x1 =['Chanakya et al','DO model','MC model']
plt.plot(x1,y5,label='Bottom wall',linewidth = 3,
         marker='v', markerfacecolor='blue', markersize=10)
plt.ylim(0.5,1.5)
plt.ylabel("Area average Nusselt number on different walls")
plt.legend()


# In[ ]:




