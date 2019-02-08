#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[69]:


data=pd.read_csv('titanic_data.csv')


# In[3]:


data


# In[4]:


data.info


# In[5]:


data.columns


# In[11]:


import cufflinks as cf


# In[70]:


sns.heatmap(data.isnull(),yticklabels=False,cbar=False)


# In[71]:


sns.boxplot(x='Survived',y='Age',data=data,hue='Survived')


# In[76]:


def add_data(cols):
    if pd.isnull(cols[0]):
        if cols[1]==1:
            return 30
        else:
            return 40
        print(cols[0])
    else:  
        return cols[0]    
        


# In[77]:


data['Age']=data[['Age','Survived']].apply(add_data,axis=1)
#datas.add(data['Survived'])
#datas1=data['Survived']


# In[78]:


sns.heatmap(data.isnull(),yticklabels=False)


# In[82]:


sns.boxplot(x='Pclass',y='Cabin',data=data,hue='Pclass')


# In[85]:


data.drop('Cabin',axis=1)


# In[108]:


data=data.join(pd.get_dummies(data['Sex']))


# In[92]:


#data.drop('male',axis=1)
data.columns


# In[109]:


import numpy as np
data.select_dtypes(include=[np.number])


# In[110]:


data.drop('male',axis=1)


# In[114]:


data=data.select_dtypes(include=np.number)


# In[115]:


data


# In[118]:


data=data.drop('male',axis=1)


# In[119]:


data


# In[120]:


data


# In[125]:


from sklearn.model_selection import train_test_split


# In[130]:


x=data[['Age','female','Pclass','Fare','SibSp','Parch']]
y=data['Survived']


# In[131]:


X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.33, random_state=42)


# In[126]:


from sklearn import linear_model


# In[142]:


fits=linear_model.SGDClassifier()


# In[143]:


fits.fit(X_train,y_train)


# In[148]:


predict_y=fits.predict(X_test)


# In[145]:


from sklearn.metrics import accuracy_score


# In[146]:


accuracy_score(y_test,predict_y)


# In[140]:


y_test


# In[147]:


predict_y


# In[ ]:




