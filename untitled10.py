# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:08:58 2018

@author: prerna.prakash
"""


# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')




points = np.arange(-5,5,0.1)


# In[ ]:


dx,dy = np.meshgrid(points,points)


# In[ ]:


z = (np.sin(dx))+ (np.cos(dy))


# In[ ]:


print(z)

