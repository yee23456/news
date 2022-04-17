from selenium import webdriver
import time
import os
import datetime
times = datetime.datetime.now()
# os.mkdir(f"G:/我的雲端硬碟/財金報/新聞文檔/{times.year}_{times.month}_{times.day}")



PATH = "C:/Users/Paul/Desktop/chromedriver/chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.get("https://finance.ettoday.net/")


for h in range(1,3):#0 3 4 5 7 8
    if h == 1 or h == 5 or h == 6:
        find_subtitle_text = []
        link_classification =driver.find_element_by_xpath(f'//*[@id="float_nav"]/ul/li[{h}]/a')
        
        #存txt檔
        path = f'C:/Users/Paul/Desktop/貼標/test/{link_classification.text}.txt'
        f = open(path, 'w',encoding=('UTF-8'))
        #點進小標題裡面
        link_classification.click()
        time.sleep(2)
    
        j = 1
        while j<4:#找前十篇文章
            try:        
                find_times_text = driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div[2]/a[{j}]/p[2]')
                if len(find_times_text.text) <=6:
                    text_test=""
                    time.sleep(2)                                 
                    link_subtitle =driver.find_element_by_xpath(f'//*[@id="finance"]/div[3]/div/div[7]/div/div/div[1]/div[1]/div[2]/a[{j}]')
                    f.writelines(f'{link_subtitle.get_attribute("href")}\n')
                    link_subtitle.click()
                    time.sleep(2)
                    
                    
                    #爬內文
                    inside_text = driver.find_elements_by_class_name("story")
                    for words in inside_text:
                        text_test+=words.text
                    text_test = text_test.replace(' ', '')
                    f.writelines(text_test)
                    f.writelines("\n\n")
                    driver.back()
                    time.sleep(2)
                else:
                    break
                j+=1
            
                
            except:
                break

        f.close()

        


#stop
time.sleep(2)
driver.quit()