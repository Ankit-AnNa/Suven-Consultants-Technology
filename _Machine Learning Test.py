#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


a=pd.read_csv('users[1].csv')
b=pd.read_csv('views[1].csv')
c=pd.read_csv('posts[1].csv')


# In[3]:


a 


# In[4]:


a['gender']=a['gender'].str.capitalize()
a['academics']=a['academics'].str.capitalize()
a['name']=a['name'].str.capitalize()
a['name']=a['name'].str.title()
a.rename(columns = {'_id':'ID','name': 'NAME','gender':'GENDER','academics':'ACADEMICS'},inplace = True)
a


# In[5]:


b


# In[6]:


b.rename(columns = {'user_id': 'ID','post_id':'POST-ID','timestamp':'TIMESTAMP'},inplace = True)
b


# In[7]:


c 


# In[8]:


c['title']=c['title'].str.title()
c['category']=c['category'].str.title()
c[' post_type']=c[' post_type'].str.capitalize()
c.rename(columns = {'_id': 'POST-ID',' post_type':'POST-TYPE','title':'TITLE','category':'CATEGORY'},inplace = True)
c


# In[9]:


d=b.groupby(['ID'])
e=d.first().reset_index()
e.info()


# In[10]:


e['TIMESTAMP']= pd.to_datetime(e['TIMESTAMP'])
e.info()


# In[11]:


df_new = pd.merge(a, e, how='right',on='ID')


# In[12]:


df_new


# In[13]:


df_1 = pd.merge(c,df_new, how='right',on='POST-ID')
df_1


# In[14]:


df_1.info()


# In[15]:


df_2=df_1[['ID','POST-ID','NAME','GENDER','ACADEMICS','TITLE','CATEGORY','POST-TYPE','TIMESTAMP']]


# In[16]:


df_2


# In[17]:


p=df_2['GENDER'].value_counts().reset_index()
p


# In[18]:


m=df_2[['GENDER','NAME']]
m.groupby(['GENDER','NAME']).first()


# In[19]:


q=df_2['ACADEMICS'].value_counts().reset_index()
q


# In[20]:


n=df_2[['ACADEMICS','NAME']]
n.groupby(['ACADEMICS','NAME']).first()


# In[21]:


r=df_2['POST-TYPE'].value_counts().reset_index()
r


# In[22]:


l=df_2[['POST-TYPE','NAME']]
l.groupby(['POST-TYPE','NAME']).first()


# In[23]:


s=df_2['CATEGORY'].value_counts().reset_index()
s[:10]


# In[24]:


plt.figure(figsize=(12,7))
plt.pie(s['CATEGORY'][:10],labels=s['index'][:10],autopct='%0.2f%%',shadow=True,counterclock=True)
plt.title('PRECENTAGE RECORD OF CATEGORPY THROUG PIE CHART',fontsize=20)
plt.show()


# In[25]:


t=df_2['TITLE'].value_counts().reset_index()
t[:10]


# In[26]:


plt.figure(figsize=(12,7))
plt.pie(t['TITLE'][:10],labels=t['index'][:10],autopct='%0.2f%%',shadow=True,counterclock=True)
plt.title('PRECENTAGE RECORD OF TITLE THROUG PIE CHART',fontsize=20)
plt.show()


# In[27]:


df_2['YEAR'] = df_2['TIMESTAMP'].dt.year 
df_2['MONTH'] = df_2['TIMESTAMP'].dt.month 
df_2['DAY'] = df_2['TIMESTAMP'].dt.day 
df_2['HOUR'] = df_2['TIMESTAMP'].dt.hour 
df_2['MINUTE'] = df_2['TIMESTAMP'].dt.minute 


# In[28]:


df_2


# In[29]:


u=df_2[['YEAR','MONTH','DAY','NAME','ID','POST-ID']]
u.groupby(['YEAR','MONTH','DAY']).first()


# In[30]:


detail=df_2.groupby(['NAME'])
x=detail.first()


# ## Enter any Candidate name and see all details which present in dataset.

# In[31]:


name = x.loc[['Akhila Kota']]
name


# In[ ]:




