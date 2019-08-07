#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
array1=np.ones((4,5))
array1


# In[5]:


#dtype function to specify datatype
array2=np.ones((4,5),dtype=np.int16)
array2


# In[14]:


#creating an empty array
array3=np.empty((2,4))
array3


# In[15]:


#identity matrix-np.eye()
array4=np.eye(4)
array4


# In[16]:


#arange in numpy
array_odd=np.arange(1,20,2)
array_odd


# In[18]:


#It also accepts float numbers
array_float=np.arange(1,10,0.5)
array_float


# In[24]:


#introduction to two-dimensional arrays
array2d=np.array([(2,4,6),(5,7,9)])
array2d


# In[23]:


#To verify if its 2D
array2d.shape


# In[29]:


#To create n-demnsional array
arraynd=np.arange(100).reshape(10,10)
arraynd


# In[ ]:




