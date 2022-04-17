import os
import joblib
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
#%%
stop_word = ['h','▲','記者','▼','【','►',' ','《','[']
def input_file(name):
    path = f"C:/Users/Paul/Desktop/貼標/{name}" #資料夾目錄
    files= os.listdir(path) #得到資料夾下的所有檔名稱
    word = []
    word_text = ''
    for file in files: #遍歷資料夾
        if not os.path.isdir(file): #判斷是否是資料夾，不是資料夾才開啟
            f = open(path+"/"+file,encoding=('utf-8')); #開啟檔案
            iter_f = iter(f); #建立迭代器
        for i in iter_f:
            line = i.splitlines()
            if line == ['']:
                word.append(word_text)
                word_text = ''
            
            elif line[0][0:3] == ['看全文']:
                continue
            
            elif line[0][0:2] == '記者':
                continue
            
            elif line[0][0] in stop_word:
                continue

            word_text+=i.rstrip()
    return word , len(word)


domestic,d_num = input_file('國內')
foreign,f_num = input_file('國外')
data = pd.DataFrame(domestic+foreign,columns=['file'])
data['lable']= '國內'
data['lable'][d_num:] = '國外'
data.drop(data[data['file'] == ''].index,inplace=True)
#%%

print(data.iloc[175:225])
#%%

import jieba
data['file_Participle'] = data['file'].apply(lambda i:jieba.cut(i) )
data['file_Participle'] =[' '.join(i) for i in data['file_Participle']]


#%%
lbl_enc = preprocessing.LabelEncoder()
y = lbl_enc.fit_transform(data.lable.values)
xtrain, xvalid, ytrain, yvalid = train_test_split(data.file_Participle.values, y, 
                                                  stratify=y, 
                                                  random_state=42, 
                                                  test_size=0.2, shuffle=True)

print (xtrain.shape)
# print (ytrain.shape)
print (xvalid.shape)


#%%


def multiclass_logloss(actual, predicted, eps=1e-15):
    """对数损失度量（Logarithmic Loss  Metric）的多分类版本。
    :param actual: 包含actual target classes的数组
    :param predicted: 分类预测结果矩阵, 每个类别都有一个概率
    """
    # Convert 'actual' to a binary array if it's not already:
    if len(actual.shape) == 1:
        actual2 = np.zeros((actual.shape[0], predicted.shape[1]))
        for i, val in enumerate(actual):
            actual2[i, val] = 1
        actual = actual2

    clip = np.clip(predicted, eps, 1 - eps)
    rows = actual.shape[0]
    vsota = np.sum(actual * np.log(clip))
    return -1.0 / rows * vsota


#%%
stwlist=[line.strip() for line in open('C:/Users/Paul/Desktop/貼標/stopwords0.txt',
'r',encoding='utf-8').readlines()]

ctv = CountVectorizer(min_df=3,
                      max_df=0.5,
                      ngram_range=(1,2),
                      stop_words = stwlist)

# 使用Count Vectorizer来fit训练集和测试集（半监督学习）
ctv.fit(list(xtrain) + list(xvalid))
xtrain_ctv =  ctv.transform(xtrain) 
xvalid_ctv = ctv.transform(xvalid)

#利用提取的word counts特征来fit一个简单的Logistic Regression 
# clf = RandomForestClassifier(n_estimators=50,max_features="sqrt",oob_score=True,random_state=3)
clf = LogisticRegression(C=1.0,solver='lbfgs',multi_class='multinomial') #test_size=0.2
# clf = MLPClassifier(solver='lbfgs',hidden_layer_sizes=(8,3), random_state=1)
clf.fit(xtrain_ctv, ytrain)
predictions = clf.predict_proba(xvalid_ctv)

predictions_2 = clf.predict(xvalid_ctv)

print(confusion_matrix(yvalid,predictions_2))
print(classification_report(yvalid,predictions_2))
print ("logloss: %0.3f " % multiclass_logloss(yvalid, predictions))


#%%
joblib.dump(clf,'clf.pkl')
joblib.dump(ctv,'ctv.pkl')
#%%
#讀取時分小標

import joblib
import pandas as pd
stop_word = ['h','▲','記者','▼','【','►',' ','《','[']
path = "C:/Users/Paul/Desktop/貼標/測試" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱
word = []
word_text = ''
for file in files: #遍歷資料夾
    if not os.path.isdir(file): #判斷是否是資料夾，不是資料夾才開啟
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

print(len(word))
#%%

clf2 = joblib.load('C:/Users/Paul/Desktop/貼標/clf.pkl')
ctv2 = joblib.load('C:/Users/Paul/Desktop/貼標/ctv.pkl')
df = pd.DataFrame(word,columns = ['file'])
df['file_Participle'] = df['file'].apply(lambda i:jieba.cut(i) )
df['file_Participle'] =[' '.join(i) for i in df['file_Participle']]
df['test_dis'] = df['file_Participle'] .apply(lambda x : clf2.predict(ctv2.transform([x])))
df['分類項目'] = df['test_dis'].apply(lambda x: '國內' if x == 0 else '國外')
print(df.head())

#%%

#編寫時分小標存檔
def dis(dis_name,sub):    
    path = f'C:/Users/Paul/Desktop/貼標/{dis_name}/2022_4_13.txt'
    f = open(path, 'w',encoding=('UTF-8'))
    for i in range(len(df)):
        if df.分類項目.iloc[i] == sub:
            f.writelines(df.file.iloc[i])
            f.writelines('\n\n')
        else:
            pass
    f.close
    
    
dis('domestic','國內')
dis('foreign','國外')

