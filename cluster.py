# -*- coding: utf-8 -*-

from matplotlib.colors import ListedColormap
import warnings
from FileReader import *
import numpy as np
from FileReader import *
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


def classifier(start,end,dic):
    
    X_train=dic[start:end][:end,1:]
    y_train=dic[start:end][:end,:1]
    #隨機分類測試資料40%學習資料60%
    X_train, X_test, y_train, y_test = train_test_split(
             X_train, y_train, test_size=0.4, random_state=0)
    #正規劃處理資料
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    #X_combined_std = np.vstack((X_train_std, X_test_std))
    #y_combined = np.hstack((y_train, y_test))
#    svm = SVC(kernel='linear', C=0.01, random_state=0)
#    svm.fit(X_train_std, y_train)
        
    #使用Perceptron分類器，深度20 學習速率0.1 
    ppn = Perceptron(n_iter=20, eta0=0.1, random_state=0)
    ppn.fit(X_train_std, y_train)
    y_pred = ppn.predict(X_test_std)
    print('Misclassified samples: %d' % (y_test != y_pred).sum())
    print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

#設定資料範圍200
end=200
dic=FileReader().json_read('data')
dic=np.array(dic)
label=dic[:end][:end,:1]
label=np.reshape(label,end)
dic1=FileReader().json_read('data1')
dic1=np.array(dic1)
classifier(0,200,dic)








