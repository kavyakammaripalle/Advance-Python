#!/usr/bin/env python
# coding: utf-8

# In[1]:


#matplotlib (data visualization libarary in python)
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[ ]:





# In[17]:


x=[2,9,6,8]
y=[1,10,5,7]
plt.plot(x,y) #function to plot(comparison of x and y)
plt.title('sales data')
plt.xlabel('quantity')
plt.ylabel('price')
plt.legend(['x,y plot'])


# In[34]:


x=[2,9,6,8]
y=[1,10,5,7]
plt.bar(x,y)
plt.title('bar graph')
plt.show()


# In[32]:


x=[2,9,6,11]
y=[1,10,5,3]
plt.hist(x)
plt.hist(y)
plt.title('histogram')


# In[29]:


x=[2,9,6,11]
y=[1,10,5,3]
plt.scatter(x,y)
plt.title('scatter plot')
plt.show()


# In[38]:


a=pd.read_csv('sample_data.csv')
a


# In[39]:


type(a)


# In[42]:


plt.plot(a.column_a,a.column_b)
plt.plot(a.column_c,a.column_b)
plt.show()


# In[44]:


data=pd.read_csv('countries.csv')
data


# In[56]:


#to select particular rows from data we use .loc
data.loc[0:11]


# In[58]:





# In[ ]:




