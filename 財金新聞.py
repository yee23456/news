# -*- coding: utf-8 -*-
#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#%%
PATH = "C:/Users/沈睿朋/Desktop/chromedriver_win32/chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.get("https://finance.ettoday.net/")


#爬小標
class_title_text = []
class_title = driver.find_elements_by_class_name("nav_1")
for i in class_title:
    link_classification = driver.find_element_by_link_text(i.text)
    link_classification.click() #點進小標題裡面
    
    for j in range(10): #找前十篇文章
        find_subtitle = driver.find_element_by_class_name("piece")
        link_subtitle = driver.find_element_by_link_text(find_subtitle.text)
        link_subtitle.click()
        
        
        
        
        
        
        
    # title = driver.find_element_by_class_name("post-title")
    # find_title = title.text
    
    




























#stop
time.sleep(5)
driver.quit()