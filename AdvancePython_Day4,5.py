#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[19]:


salaries=np.genfromtxt(r'C:\\Users\\ADMIN\\Desktop\\Advance_Python\\realtimedatasets\\salary.csv',delimiter=',')
salaries


# In[16]:


import sys
np.set_printoptions(threshold=sys.maxsize)
salaries=np.genfromtxt(r'C:\\Users\ADMIN\Desktop\Advance_Python\realtimedatasets\salary.csv',delimiter=',')
salaries


# In[20]:


#operations
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
a+b
a-b
a*b
a/b
a%b
a**3


# In[21]:


#dot function/method
a=np.array(([2,3],[5,9]))
b=np.array(([1,0],[0,1]))
print('a:\n',a)
print('b:\n',b)
a*b #element wise multiplication
a.dot(b) #Matrix multiplication


# In[23]:


#Modifying an existing array rather than creating a new one
a=np.array([[2,3],[5,9]])
b=np.array([[1,0],[0,1]])
a+=3
a


# In[24]:


a=np.array([[2,3],[5,9]])
b=np.array([[1,0],[0,1]])
b+=a
b


# In[25]:


#unary operations
ages=np.array([5,10,18,21,35,49,55,60,78,82])
ages.sum()
ages.min()
ages.max()


# In[26]:


numbers=np.arange(60).reshape(10,6)
numbers
numbers.sum()


# In[27]:


#axis 0 represnts column and axis 1 represents rows
a=np.arange(24).reshape(6,4)
a.sum(axis=1)
a.sum(axis=0)


# In[28]:


#universal functions:Trigonometry,arithmetic,complex and statistical functions
#trigonometric functions
#sin
angles=np.array([0,30,45,60,90])
#angles must be converted to radians by multiplying by pi/180
angles_radians=angles*np.pi/180
angles_radians
print('sine of angles in the array:')
print(np.sin(angles_radians))


# In[29]:


#cos
angles=np.array([0,30,45,60,90])
angles_radians=angles*np.pi/180
angles_radians
print('cos of angles in the array:')
print(np.cos(angles_radians))


# In[30]:


#Tan
angles=np.array([0,45,60,60,90])
angles_radians=angles*np.pi/180
angles_radians
print('tan of angles in the array:')
print(np.tan(angles_radians))


# In[31]:


#statistical functions
test_scores=np.array([32.45,45.78,67.90,34.56])
print('mean of the scores:')
print(np.mean(test_scores))
print('median of scores:')
print(np.median(test_scores))


# In[36]:


#Numpy indexing and slicing
a=np.arange(12)**2
a


# In[43]:


a[-2]
a[2]
a[2:7]
a[:7]
a[3:]
a[2:-3]
a[1:11:3]


# In[45]:


#How to print array of numbers in  reverse order by using negative index
a[::-1]


# In[ ]:




