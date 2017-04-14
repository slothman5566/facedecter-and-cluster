# -*- coding: utf-8 -*-
import cv2
from FileReader import *
import numpy as np

#利用opencv從source資料夾圖裁出人臉並輸出ouput資料夾
def detect(path,filename,filetype):
    img = cv2.imread(path+"\\"+filename+"."+filetype,0)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img,filename): 
    for x1, y1, x2, y2 in rects:
        crop=img[y1:y2,x1:x2]
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
        cv2.imwrite("./data/"+filename[:len(filename)-4]+".jpg", crop);#output file

p=FileReader()
data=p.file_read("./data","jpg")#source file，檔案類型

for f in data:
    rects, img = detect(p.DATA_DIR,f,p.file_type)
    box(rects, img,f)


