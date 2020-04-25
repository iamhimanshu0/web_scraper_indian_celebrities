#!/usr/bin/env python
# coding: utf-8

# ### Web Scraper
# - Beautiful Soup
# - Request

# In[11]:


from bs4 import BeautifulSoup
import requests
import json


link = "https://www.imdb.com/list/ls068010962/"
source = requests.get(link).text 

soup = BeautifulSoup(source,'html.parser')

d = {
    "data": []
}
# print(soup.prettify())
f = soup.find_all('div',class_= 'lister-item mode-detail')

for list in f:
    # print(list.prettify())
    name = list.find('h3', class_='lister-item-header').text
    name = name.split('\n')
    name = name[2].strip()
    # print("----------------")
    about = list.find_all('p')
    about = about[1].text.strip()
    # print('---------------------')
    img = " ".join([img.get('src') for img in list.find_all('img')])
#     
    d['data'].append(
        {
        
        'name':name,
        'about':about,
        'img' :img
        }
        )
    

# json_data = json.dumps(d,sort_keys=False,indent=4)
# print(json_data)

print(d)


# ### After scraping we have
# - Name
# - About 
# - Image Link

# ###  Database Connection 
# - PyMongo
# 

# In[12]:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Make Database called Indina_photos 
mydb = myclient["indian_photos"]

mycol = mydb['data_']


# ### Insert data into Database 

# In[13]:


insert = mycol.insert_many(d['data'])


# ### Print inserted Data id

# In[14]:


print(insert.inserted_ids)


# ### Check for the values 

# In[15]:


for x in mycol.find():
    print(x)


# ### Get Perticular Person
# - In this case "Akshay Kumar"
# - About "Akshay Kumar"
# - Image link

# In[19]:


for x in mycol.find({ "name": 'Akshay Kumar' }):
    name = x['name']
    about =x['about']
    img = x['img']
    

print(name)
print(about)
print(img)


