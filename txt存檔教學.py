# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:34:44 2022

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

PATH = "C:/Users/沈睿朋/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://money.udn.com/money/cate/12017?from=edn_navibar")

while