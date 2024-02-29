#!/usr/bin/env python
# coding: utf-8

# In[130]:


import pandas as pd


# In[ ]:


pd.


# In[131]:


df = pd.read_csv('telco_churn.csv')


# In[134]:


tempdict = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}


# In[135]:


dictdf = pd.DataFrame.from_dict(tempdict)


# In[133]:


df.head(10)


# In[136]:


dictdf.head()


# In[138]:


df.tail(15)


# In[139]:


df.columns


# In[140]:


df.dtypes


# In[141]:


df.describe()


# In[142]:


df.describe(include='object')


# In[143]:


df.State


# In[145]:


df['International plan']


# In[146]:


df[['State', 'International plan']]


# In[148]:


df.Churn.unique()


# In[149]:


df.head()


# In[150]:


df[df['International plan']=='No']


# In[152]:


df[(df['International plan']=='No') & (df['Churn']==True)]


# In[153]:


df.iloc[14]


# In[155]:


df.iloc[14,-1]


# In[156]:


df.iloc[22:33]


# In[157]:


state = df.copy()
state.set_index('State', inplace=True)


# In[158]:


state.head()


# In[159]:


state.loc['OH']


# In[160]:


df.isnull().sum()


# In[161]:


df.dropna(inplace=True)


# In[162]:


df.isnull().sum()


# In[163]:


df.drop('Area code', axis=1)


# In[164]:


df['New Column'] = df['Total night minutes'] + df['Total intl minutes']


# In[165]:


df.head()


# In[166]:


df['New Column'] = 100


# In[167]:


df.head()


# In[168]:


df.iloc[0,-1] = 10


# In[169]:


df.head()


# In[170]:


df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)


# In[ ]:





# In[172]:


df[df['Churn']==True].head()


# In[173]:


df.to_csv('output.csv')


# In[174]:


df.to_json()


# In[175]:


df.to_html()


# In[176]:


del df


# In[ ]:





# In[ ]:




