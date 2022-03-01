# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 18:20:41 2022

@author: 沈睿朋
"""
#%%
import requests
news_URL = 'https://finance.ettoday.net/focus/775'
news_res = requests.get(news_URL)
print(news_res)
#%%
from bs4 import BeautifulSoup as bs

soup = bs(news_res.text,"html.parser") #以HTML結構解析

#程式碼全部靠左對齊
print(soup.prettify())
#%%
print(soup.title)
#%%
for i in soup.find_all(class_='clearfix'):
    print(i.find('a').get('href'))
    
  # print(i.find('a').text)
  # print(i.find('a').get('href'))