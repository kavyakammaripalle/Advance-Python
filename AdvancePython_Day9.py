#!/usr/bin/env python
# coding: utf-8

# In[4]:


#syntax for dataframe
# pandas.DataFrame(data,index,columns,dtype,copy)
#creating and empty datafarame
import pandas as pd
a=pd.DataFrame()
print(a)


# In[5]:


#creating dataframes with a list
data=[1,2,3,4,5,6,7]
d=pd.DataFrame(data)
print(d)


# In[17]:


x=[['kavya',80],['rahul',75],['karthik',100],['keerthi',78]]
y=pd.DataFrame(x,columns=['Student Name','Scores'],dtype=float)
print(y)


# In[16]:


#creating a dataframe from a dictionary of nd arrays/list
data={'Name':['kavya','karthi','keerthi','dhanush'],'Age':[23,24,23,19]}
df=pd.DataFrame(data,index=['1','2','3','4'])
print(df)


# In[19]:


data=[{'a':1,'b':3},{'b':0,'c':4}]
x=pd.DataFrame(data)
print(x)


# In[ ]:




