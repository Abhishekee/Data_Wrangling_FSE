#!/usr/bin/env python
# coding: utf-8

# In[65]:


import os
import requests
from statistics import median
from datetime import datetime, timedelta
MY_API_KEY = "GiLsNT3yeyEPwCHaCz4V"


# In[66]:


FSE_AFX_base_url = 'https://data.nasdaq.com/api/v3/datasets/FSE/AFX_X'
params = {
    'start_date' : datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'),
    'end_date' : datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'),
    'api_key' : MY_API_KEY
}
response = requests.get(FSE_AFX_base_url, params = params)


# In[6]:


response.json()


# In[9]:


FSE_AFX_base_url = 'https://data.nasdaq.com/api/v3/datasets/FSE/AFX_X'
params = {
    'start_date' : '2019-01-02',
    'end_date' : '2019-12-30',
    'api_key' : MY_API_KEY
}
response = requests.get(FSE_AFX_base_url, params = params)


if response.status_code != 200:
    print("Error")
else:
    print("Working")


# In[15]:


data = response.json()

data.keys()

data['dataset'].keys()
data['dataset']['data'][3]


# In[25]:


dataset = data['dataset']


# In[23]:


data['dataset']['type']


# In[24]:


data['dataset']['column_names']


# In[30]:


FSE_data = dataset['data']
FSE_data[1]
FSE_data[1][1]


# In[62]:


largest_open_price = max(row[1] for row in FSE_data if row[1] is not None)
lowest_open_price = min(row[1] for row in FSE_data if row[1] is not None)
print("largest open price: ", max_open_price)
print("lowest open price: ", min_open_price)


# In[35]:


no_dates = [row for row in FSE_data if row[1] is None]
print(no_dates)


# In[37]:


print("high_price:", FSE_data[1][2], 'low_price:', FSE_data[1][3])


# In[63]:


maximum_diff = max(row[2]-row[3] for row in FSE_data if row[2] is not None and row[3] is not None)
print("max change in a day:", maximum_diff)


# In[39]:


FSE_data[1][4]


# In[64]:


maximum_change = 0
for i in range(1, len(FSE_data)):
    difference_closing_price = FSE_data[i][4] - FSE_data[i-1][4]
    if abs(difference_closing_price) > maximum_change:
        maximum_change = abs(difference_closing_price)
print("Max Change in any two days:", maximum_change)


# In[53]:


FSE_data[1][6]


# In[59]:


avg_daily_trading_volume = sum([row[6] for row in FSE_data if row[6] is not None])/ len(FSE_data)
print("Average daily Trading Volume for 2019:", avg_daily_trading_volume)


# In[61]:


data =[2,6,9,35,11]
print("Median Trading voume for 2019:", median([row[6] for row in FSE_data if row[1] is not None])) 

