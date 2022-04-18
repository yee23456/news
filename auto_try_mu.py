# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:22:16 2022

@author: 沈睿朋
"""
import os
import jieba
import joblib
import pandas as pd
clf2 = joblib.load('C:/Users/Paul/Documents/github/news/clf.pkl')
ctv2 = joblib.load('C:/Users/Paul/Documents/github/news/ctv.pkl')
#%%

def make_dataframe():
    df = pd.DataFrame(word,columns = ['file'])
    df['file_Participle'] = df['file'].apply(lambda i:jieba.cut(i) )
    df['file_Participle'] =[' '.join(i) for i in df['file_Participle']]
    df['test_dis'] = df['file_Participle'] .apply(lambda x : clf2.predict(ctv2.transform([x])))
    df['分類項目'] = df['test_dis'].apply(lambda x: '國內' if x == 0 else '國外')
    return df



def dis(data,sub):
    path = f'C:/Users/Paul/Desktop/貼標/2022_4_6/{file_new_name}分類/{sub}.txt'
    f = open(path, 'w',encoding=('UTF-8'))
    for i in range(len(data)):
        if data.分類項目.iloc[i] == sub:
            f.writelines(data.file.iloc[i])
            f.writelines('\n\n')
        else:
            pass
    f.close()
    



#%%
#讀取時分小標

stop_word = ['h','▲','記者','▼','【','►',' ','《','[']
path = "C:/Users/Paul/Desktop/貼標/2022_4_6" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱


for file in files: #遍歷資料夾
    word = []
    word_text = ''
    f = open(path+"/"+file,encoding=('utf-8')); #開啟檔案
    iter_f = iter(f); #建立迭代器
    for i in iter_f:
        line = i.splitlines()
        if line == ['']:
            word.append(word_text)
            word_text = ''
            
        elif line[0][0:3] == '看全文':
            continue
        
        elif line[0][0:2] == '記者':
            continue
        
        elif line[0][0] in stop_word:
            continue
        
        word_text+=i.rstrip()
    word.append(word_text)
    file_new_name = file.replace('.txt', '')
    f.close()
    os.mkdir(f"C:/Users/Paul/Desktop/貼標/2022_4_6/{file_new_name}分類")
    dis(make_dataframe(), '國內')
    dis(make_dataframe(), '國外')
    
