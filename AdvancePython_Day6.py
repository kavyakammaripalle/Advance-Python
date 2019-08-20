#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numpy iterating
import numpy as np


# In[2]:


a=np.arange(11)**2
a


# In[4]:


a=np.arange(11)**2
for i in a:
    print(i**(1/2))


# In[33]:


students=np.array([['cathy','beth','rachel','ross','alice'],
                  [77,89,69,94,76],
                  [79,75,65,86,90]])

for i in students:
    print('i=',i)


# In[34]:


for e in students.flatten():
    print(e)


# In[38]:


#forton order flattern
for element in students.flatten(order='F'):
    print(element)


# In[40]:


#nditer
#row-wise
x=np.arange(12).reshape(3,4)
x
for i in np.nditer(x):
    print(i)


# In[50]:


#column-wise
x=np.arange(12).reshape(3,4)
for i in np.nditer(x,order='F'):
    print(i)


# In[ ]:




