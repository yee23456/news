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
class_title = driver.find_elements_by_class_name("nav_1")
class_title_text = class_title[0].text.split("\n")


for h in class_title_text[:6]:
    find_subtitle_text = []
    link_classification = driver.find_element_by_link_text(h)
    link_classification.click() #點進小標題裡面
    time.sleep(5)
    
    find_subtitle = driver.find_elements_by_css_selector(".piece.clearfix [title]")
    find_subtitle_text = [i.get_attribute('title') for i in find_subtitle]
    
    print(find_subtitle_text)
    
    # for j in find_subtitle_text[:2]: #找前十篇文章
    #     text_test=""
    #     link_subtitle =driver.find_element_by_link_text(j)
    #     link_subtitle.click()
    #     time.sleep(3)
    #     # WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    #     #     (By.CLASS_NAME, "story")))
        
        
    #     inside_text = driver.find_elements_by_class_name("story")
    #     for words in inside_text:
    #         text_test+=words.text
    #     print(text_test)
            
    #     driver.back()
    #     time.sleep(3)
        
        
        
        
        
    # title = driver.find_element_by_class_name("post-title")
    # find_title = title.text
  
    




























#stop
time.sleep(5)
driver.quit()