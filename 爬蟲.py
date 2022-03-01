# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:46:54 2022

@author: 沈睿朋
"""
#%%

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#%%
import jieba
text_test=""
train = []
PATH = "C:/Users/沈睿朋/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://finance.ettoday.net/focus/775")


#搜尋
# search = driver.find_element_by_name("query")
# search.send_keys("比特幣")
# search.send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.CLASS_NAME, "block_title")))

#找標題
# title = driver.find_element_by_class_name("post-title")
# find_title = title.text



#找網址
elems  = driver.find_element_by_css_selector(".piece.clearfix [href]")
links = [elem.get_attribute('href') for elem in elems]
print(links)

# class_title = driver.find_elements_by_class_name("nav_1")
# for i in class_title:
#     print(i.text)

#文章點按進去
# link = driver.find_element_by_link_text("SWIFT被踢還有西聯匯款！　俄羅斯留學生、異鄉人免驚")
# link.click()


#爬文
# inside_text = driver.find_elements_by_class_name("story")
# for words in inside_text:
#     text_test+=words.text
# print(text_test)
    
    

time.sleep(5)
driver.quit()
# link.click()
# driver.find
#%%

class_title_text = []
class_title = driver.find_elements_by_class_name("nav_1")



#%%

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np 
from collections import Counter

#斷詞

with open("C:/Users/沈睿朋/Desktop/NLP/stopword.txt","r",encoding=("utf-8-sig")) as f:
    stops = f.read().split("\n")

train = []
for t in jieba.cut(text,cut_all=(False)):
    if t not in stops:
        train.append(t)



diction  = Counter(train)

font = "C:/windows/Fonts/simsun.ttc"
mask = np.array(Image.open("C:/Users/沈睿朋/Desktop/heart.jpg"))
wordcloud = WordCloud(background_color="white",mask = mask,
                      font_path = font)
wordcloud.generate_from_frequencies(diction)

plt.figure(figsize = (6,6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# wordcloud.to_file("news.png")