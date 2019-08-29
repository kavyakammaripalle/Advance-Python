#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[ ]:


#syntax: pandas.series(data,index,dtype,copy)


# In[8]:


s=pd.Series()
s


# In[10]:


#creating series from an ndarray
import numpy as np
import pandas as pd
a=np.array(['a','b','c','d','e'])
s=pd.Series(a)
s


# In[14]:


#creating index position manually
data=np.array(['monica','rachel','joey'])
s=pd.Series(data,index=[0,1,2])
s


# In[19]:


#creating a series from list
l=['a','b','c','d','e']
s=pd.Series(l)
s


# In[25]:


#creating a series from dictionary
data={'a':123,'b':456,'c':789}
s=pd.Series(data)
s


# In[28]:


data={'d':12,'a':15,'b':25,'e':10}
s=pd.Series(data,index=['a','b','c','d','e'])
print(s)


# In[33]:


#creating a series from a scalar value
s=pd.Series(5,index=[100,101,102,103,104])
print(s)


# In[50]:


#how to access the data
a=pd.Series([1,2,3,4,5,6,7,8,9,10],index=['a','b','c','d','e','f','g','h','i','j'])
print(a)
a[7]
a[::-1]
a[-7]
a[:-5]
a[1:5]


# In[ ]:




