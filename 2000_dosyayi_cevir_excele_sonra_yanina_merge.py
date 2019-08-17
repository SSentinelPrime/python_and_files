#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import os as os


# In[17]:


directory = input("Path to directory: ")


# In[18]:


os.getcwd()


# In[22]:


os.chdir('C:\\Users\\Ahmets Project\\Desktop\\txt')


# In[23]:


os.getcwd()


# In[25]:


files_dir =  os.listdir(directory)


# In[26]:


newlist = []


# In[27]:


for names in files_dir:
    if names.endswith(".txt"):
        newlist.append(names)


# In[28]:


print(newlist)


# In[33]:


for i in newlist :
    x = i
    df2 = pd.read_excel('2_notalar_ve_freq_comma.xlsx')
    try:
        df1 = pd.read_table(x)
    except FileNotFoundError:
        continue
    results = df1.merge(df2, on='Koma53')
    sort_by_time = results.sort_values('Sira')
    y = ("5_" +"%s" %x + ".xlsx")
    pd.DataFrame(sort_by_time).to_excel(y)


# In[ ]:





# In[ ]:




