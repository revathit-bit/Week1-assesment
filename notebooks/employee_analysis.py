#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import os

print("Current location:", os.getcwd())

file_path = "../data/employees.csv"

print("File exists:", os.path.exists(file_path))

df = pd.read_csv(file_path)

print(df)


# In[7]:


print(df["city"].value_counts())
get_ipython().run_line_magic('timeit', 'df["salary"].mean()')



# In[8]:


df.groupby("city")["salary"].mean().plot(kind="bar")

plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.show()


# In[9]:


import matplotlib.pyplot as plt


# In[10]:


df.groupby("city")["salary"].mean().plot(kind="bar")

plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.show()


# In[ ]:




