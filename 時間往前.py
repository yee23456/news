from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import datetime
times = datetime.datetime.now()
# os.mkdir(f"C:/Users/user/Desktop/同步/{times.year}_{times.month}_{times.day}")
#%%


PATH = "C:/Users/user/Desktop/chromedriver_win32/chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.get("https://finance.ettoday.net/")


#爬小標
# class_title = driver.find_elements_by_class_name("nav_1")
# class_title_text = class_title[0].text.split("\n")




for h in range(1,10):#0 3 4 5 7 8
    if h == 8 or h == 1 or h == 4 or h == 5 or h == 6 :
        find_subtitle_text = []
        link_classification =driver.find_element_by_xpath(f'//*[@id="float_nav"]/ul/li[{h}]/a')
        
        #存txt檔
        path = f'C:/Users/user/Desktop/text/output{link_classification.text}.txt'
        f = open(path, 'w',encoding=('UTF-8'))
        
        #點進小標題裡面
        link_classification.click()
        time.sleep(5)
    
        j = 1
        while True:#找前十篇文章
            try:        
                find_times_text = driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div[2]/a[{j}]/p[2]')
                if len(find_times_text.text) <=6 or find_times_text.text[:10] == '2022-03-07':
                    text_test=""
                    time.sleep(5)                                 
                    link_subtitle =driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div[2]/a[{j}]')
                    f.writelines(f'{link_subtitle.get_attribute("href")}\n')
                    link_subtitle.click()
                    time.sleep(5)
                    
                    
                    #爬內文
                    inside_text = driver.find_elements_by_class_name("story")
                    for words in inside_text:
                        text_test+=words.text
    
                    f.writelines(f'{j}\n')
                    f.writelines(text_test)
                    f.writelines("\n\n\n\n\n\n")
                    driver.back()
                    time.sleep(5)
                else:
                    break
                j+=1
            
                
            except:
                next_page_button = driver.find_element_by_xpath('//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[2]/a[1]')
                next_page_button.click()
                h = j
                while True:
                    try:
                        find_times_text = driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div/a[{h}]/p[2]')
                        if len(find_times_text.text) <=6 or find_times_text.text[:10] == '2022-03-07':
                            text_test=""
                            time.sleep(5)                                 
                            link_subtitle =driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div/a[{h}]')
                            f.writelines(f'{link_subtitle.get_attribute("href")}\n')
                            link_subtitle.click()
                            time.sleep(5)
                            
                        
                         #爬內文
                            inside_text = driver.find_elements_by_class_name("story")
                            for words in inside_text:
                                text_test+=words.text
                         
                            f.writelines(f'{h}\n')
                            f.writelines(text_test)
                            f.writelines("\n\n\n\n\n\n")
                            driver.back()
                            time.sleep(5)
                        else:
                            break
                    except:
                        break
                    h+=1
                break

        f.close()

        


#stop
time.sleep(5)
driver.quit()
