#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Pandas Functionality
#Create a series with 100 random number
import pandas as pd
import numpy as np
s=pd.Series(np.random.randn(100))
print(s)


# In[4]:


#Axes
s=pd.Series(np.random.randn(5))
print("The axes are:")
print(s.axes)


# In[5]:


#Empty
s=pd.Series(np.random.randn(20))
print("is the object empty?")
print(s.empty)


# In[6]:


#To check how many dimensions does series have
s=pd.Series(np.random.randn(4))
print(s)
print("Dimensions of the object:")
print(s.ndim)


# In[8]:


#To check size of the data
s=pd.Series(np.random.randn(7))
print(s)
print(s.size)


# In[10]:


#Values
s=pd.Series(np.random.randn(12))
print(s)
print("The actual data series:")
print(s.values)


# In[13]:


#Head and Tail
s=pd.Series(np.random.rand(20))
print(s)
print("first 3 rows of data series:")
print(s.head(3))
print("last 3 rows of data series:")
print(s.tail(3))


# In[ ]:




