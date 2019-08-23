#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Array shape manipulation
import numpy as np


# In[17]:


a=np.array([('germany','france','hungary','austria'),('berlin','paris','budapest','vienna')])
a


# In[18]:


a.shape


# In[19]:


a.ravel()


# In[20]:


#Transpose
a.T


# In[22]:


a.T.ravel()


# In[3]:


x=np.arange(9)
x


# In[8]:


print("split the array:")
np.split(x,3)


# In[9]:


print("split the array:")
np.split(x,5)


# In[ ]:




