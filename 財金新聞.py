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


for h in range(9):#0 3 4 5 7 8
    if h == 0 or h == 3 or h == 4 or h == 5 or h == 7 or h == 8:
        find_subtitle_text = []
        link_classification = driver.find_element_by_link_text(class_title_text[h])
        link_classification.click() #點進小標題裡面
        time.sleep(2)
        path = f'C:/Users/沈睿朋/Desktop/比賽/output{class_title_text[h]}.txt'
        f = open(path, 'w' , encoding  = 'UTF-8')
    
    
        for j in range(1,3): #找前十篇文章
            text_test=""
            time.sleep(2)
            link_subtitle =driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div[2]/a[{j}]')
            link_subtitle.click()
            time.sleep(2)
            
            
            # 爬內文
            inside_text = driver.find_elements_by_class_name("story")
            for words in inside_text:
                text_test+=words.text
            
            f.writelines(f'{j}')
            f.writelines(f'{link_subtitle.get_attribute("href")}\n')
            f.writelines(text_test)
            f.writelines("\n\n\n\n\n\n")
            driver.back()
        f.close()
    else:
        pass
        
        

#stop
time.sleep(5)
driver.quit()