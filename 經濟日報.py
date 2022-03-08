# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 08:07:34 2022

@author: 沈睿朋
#金融 :外匯市場 保險 銀行 Fintech
https://money.udn.com/money/cate/12017?from=edn_navibar

#期貨 :
https://money.udn.com/money/cate/11111?from=edn_navibar

#理財 :
https://money.udn.com/money/cate/5592?from=edn_navibar

#房市 :
https://money.udn.com/money/cate/5593?from=edn_navibar

#證券 :
https://money.udn.com/money/cate/5590?from=edn_navibar

#產業 : 科技產業
https://money.udn.com/money/cate/5591?from=edn_navibar
"""
#%%
print("123456879"[:3])

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import datetime
times = datetime.datetime.now()
# os.mkdir(f"C:/Users/user/Desktop/吐了/{times.year}_{times.month}_{times.day}")
#%%
PATH = "C:/Users/沈睿朋/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://money.udn.com/money/cate/12017?from=edn_navibar")

for i in range(2):
    link_classification =driver.find_element_by_xpath(f'//*[@id="wrapper"]/div/div/main/section[{i+3}]/div[2]/div[2]/a')
    link_classification.click()
    for j in range(3):
        text_test = ''
        time_find = driver.find_element_by_xpath('//*[@id="story"]/div/div[2]/div/section/div/article/section/time')
        
        if time_find.text[:10] == f'{times.year}/0{times.month}/0{times.day}':
            inside_text = driver.find_elements_by_class_name("article-body__editor")
            for words in inside_text:
                text_test+=words.text
            print(text_test)
        
            next_article = driver.find_element_by_xpath('//*[@id="story"]/div/div[2]/div/section/div/section[5]/div[2]/a')
            next_article.click()
        else:
            print('1234')
            break
    link_subtitle = driver.find_element_by_xpath('//*[@id="swiperHeader"]/nav/a[10]')
    link_subtitle.click()
        
time.sleep(5)
driver.quit()
#%%
from datetime import datetime

s = '2022-03-05'
day = datetime.strptime(s, '%Y-%m-%d')
print(type(day))
print((times-day).days <=7)

























