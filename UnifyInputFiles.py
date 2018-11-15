# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:51:56 2018

@author: prerna.prakash
"""

import os
import glob
import FLModule as FM
from shutil import copyfile

class UnifyInputFiles():
    
    def __init__(self,path,pathFinal):
        self.path = path
        self.pathFinal = pathFinal
        self.pathFinal = self.pathFinal
        os.makedirs(self.pathFinal, exist_ok=True)
        os.chdir(self.path)
        self.zip()
        self.csv()
        self.xlsx()
        
        
    def csv(self) :
        
        os.chdir(self.path)
        for files in glob.glob('*.csv'):
            copyfile(self.path+"\\"+files,self.pathFinal+"\\"+files)
            name = FM.rename(files)
            if name :            
                os.chdir(self.pathFinal)
                os.rename(files,name+".csv")
        return False
    
    def xlsx(self) :
        os.chdir(self.path)
        
        for files in glob.glob('*.xlsx'):          
             copyfile(self.path+"\\"+files,self.pathFinal+"\\"+files)
             name = FM.rename(files)
             if name :            
                os.chdir(self.pathFinal)
                os.rename(files,name+".xlsx")
        return False               
            
    def zip(self) :
        os.chdir(self.path)
        for files in glob.glob('*.zip') :
            FM.unzipfile(files,self.path,b'jockey')
            #FM.unzipfile(files,self.pathFinal,b'jockey')
        return False
    
