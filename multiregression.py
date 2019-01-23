#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
import random
x=np.random.randint(1,1000,100)
#y=np.random.randint(1,1000,100)


# In[2]:


x


# In[15]:


x=x.reshape(20,5)
x[:,0]=1
x


# In[4]:



y=np.array(20)
y=x[:,0]
y


# In[88]:


x[:,0]=1


# In[13]:


x


# In[8]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#plt.scatter(x,y)


# In[ ]:





# In[11]:


list1=np.random.rand(5)
B=np.array(list1)
print(B)
y1=np.dot(x,B)
#print(y1)
mse=np.sum(np.square(y-y1))
for i in range(5):
    y1=np.dot(x,B)
    cost_b=np.dot(np.dot(2,y1),x)
    B=B-0.1*cost_b
print(B)


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')

#plt.scatter(x)


# In[ ]:




