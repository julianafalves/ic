#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


csv = pd.read_csv('./adni_gwas_v2/adni_gwas_v2_set1/002_S_0295.csv', engine='python', encoding = "utf-8-sig",usecols=["SNP Name","Allele1 - Top"]) #deu certo essa parte
xlsx=pd.read_excel('dados.xlsx')


# In[5]:


xlsx.head()


# In[6]:


csv.head()



# In[57]:


df1 = pd.DataFrame(csv)
df1 = df1.transpose()
df1 = df1.drop(['SNP Name'],axis=0) #tirando a primeira linha


# In[58]:


df1


# In[62]:


df2 = pd.DataFrame(xlsx['Name'])
df2 = df2.transpose()


# In[63]:


df2


# In[68]:


df = pd.concat([df1,df2],axis=0)
df.columns = df.iloc[0] #estou transformando a linha 'Name' em cabeçalho
#df = df.drop(['Name'],axis=0) #tirando a linha name pra deixar só como cabeçalho


# In[69]:


print(df)

