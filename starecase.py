#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import numpy as np
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


# In[ ]:





# In[ ]:





# In[3]:


#k=int(input())
#type(k)
prl=[]

for i in range(1,100):
    pos=0
    for i in range(100):
        di=np.random.randint(1,7)
        if (di<4 and pos!=0):
            pos-=1
        if (di<6) and (di>=4):
            pos+=1
        if(di==6):
            d=np.random.randint(1,7)
            pos+=d
    prl.append(pos)
print(prl)    


# In[4]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(prl)


# In[12]:


prls=np.array(prl)
prls.mean()


# In[13]:


dices=[1,2,3,4,5,6]
biased_dice=np.random.choice(dices,p=[1/4,1/4,1/4,1/12,1/12,1/12])


# In[6]:


stare_step=[]
for i in range(100):
    pos=0
    for i in range(100):
        biased_dice=np.random.choice(dices,p=[1/4,1/4,1/4,1/12,1/12,1/12])
        if (biased_dice<4):
            if pos!=0:
                pos-=1
        elif (biased_dice<6) and (biased_dice>4):
            pos+=1
        elif(biased_dice==6):
            biased_dice=np.random.choice(dices,p=[1/4,1/4,1/4,1/12,1/12,1/12])
            pos+=biased_dice
    stare_step.append(pos)
print(stare_step)    


# In[7]:


plt.hist(stare_step)


# In[11]:


stare_steps=np.array(stare_step)
stare_steps.mean()


# In[ ]:




