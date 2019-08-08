#!/usr/bin/env python
# coding: utf-8

# In[1]:


#print statement
#1D array-printed as rows
#2D array-printed as matrices
#3D array-printed as a list of matrices


# In[4]:


#1D array
import numpy as np
array1=np.arange(12)
print(array1)


# In[5]:


#2D array
array2=np.arange(10).reshape(5,2)
print(array2)


# In[6]:


#3D array
array3=np.arange(20).reshape(2,5,2)
print(array3)


# In[7]:


print(np.arange(1000))


# In[15]:


#np.set_printoptions(threshold=np.nan)


# In[17]:


#Operations
a=np.array([5,6,9])
b=np.array([3,6,12])
a+b


# In[ ]:




