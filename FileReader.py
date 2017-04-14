# -*- coding: utf-8 -*-

import os
import json

class FileReader:
    def __init__(self):
        self.DATA_DIR = ""#資料夾
        self.file_type=""#檔案類型
        self.file_data=[]
        

    def file_read(self,path,type):
        self.DATA_DIR=path
        self.file_type=type
        
        for root, dirs, files in os.walk(self.DATA_DIR):
            for f in files:
                if f[len(f)-len(self.file_type):]==self.file_type:#檔案類型
                     self.file_data.append(f[:len(f)-len(self.file_type)-1])
        return self.file_data
    def json_write(self,file,input):
        f= open('./'+file+'.json','w')
        f.write(json.dumps(input))
        f.close();
        
    def json_read(self,file):
        f= open('./'+file+'.json')
        data  =  json.load(f)
        f.close()
        return data