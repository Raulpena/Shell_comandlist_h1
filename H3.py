
# coding: utf-8

# In[6]:

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt 
import pandas as pd
import sys
import matplotlib


# In[7]:

print('python version' + sys.version)
print('pandas ver' + pd.__version__)
print('matplotlib ver' + matplotlib.__version__)


# In[17]:

names = ['bib','lighting','fire','water','earth']
births=[90,55,82,23,45]
BabyDataSet=list(zip(names,births))
BabyDataSet


# In[22]:

df=pd.DataFrame(data=BabyDataSet,columns=['names','births'])
df


# In[33]:

#df.to_csv?
df.to_csv('birthsfile.csv',index=False,header=False)


# In[45]:

Location=r'/home/b107-08/birthsfile.csv'
df=pd.read_csv(Location)
df=pd.read_csv(Location,header = None)
df=pd.read_csv(Location,names=['names','births'])


# In[46]:

import os
os.remove(Location)


# In[51]:

Sorted = df.sort_values(['births'],ascending=False)
Sorted.head(1)
df['births'].max()


# In[55]:

df['births'].plot()
MaxValues=df['births'].max()
MaxName=df['names'][df['births']==df['births'].max()].values
Text=str(MaxValue)+"_"+MaxName


# In[69]:

plt.annotate(Text,xy=(1,MaxValue),xytext=(8,0),xycoords=('axes fraction','data'),textcoords='offset points')
print("The most popular name")
df[df['births']==df['births'].max()]

