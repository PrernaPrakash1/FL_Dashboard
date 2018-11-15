# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:52:37 2018

@author: prerna.prakash
"""
import FLModule as fm
import pycel as py
import glob
import pandas as pd
import os
import datetime
import logging
import logging.config

class FLnoCCD :
    def __init__(self):

        self.path = "C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\"
        self.unzipNoCCD()
        self.DateToday = datetime.date.today()
        self.month = str(self.DateToday.month) 
        self.day = str(self.DateToday.day)
        self.DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+self.day+self.month+"\\"  


   

    
    def concatinate(self) :
        df = pd.DataFrame()
        os.chdir("C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\files")
        for root, dirs, files in os.walk("C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\files"):
            for name in files:
                print(root,"\\",name)
                newname = fm.CCDrename(root+name)
                print(newname)
                if newname :   
                     os.chdir(root)
                     os.rename(name,newname+".csv")
                     name = root+"\\"+newname+ ".csv"
                     self.appendToMainFile(name)
                   
        return False
             


    def unzipNoCCD(self) :
        os.chdir(self.path)
        for file in glob.glob('*.zip') :
            fm.unzipfile(self.path+file,self.path+"files\\",b"")
        self.concatinate()
        return False 
    
    
    def appendToMainFile(self,name) :
        if 'EDGEID' in name :
            dfCCDEDGEID = pd.read_excel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\Main\\EDGEID.xlsx')
            dfEDGEID = pd.read_csv(name,low_memory = False, error_bad_lines=False)
            dfCCDEDGEID= dfCCDEDGEID.append(dfEDGEID)
            print('Appending EDGEID')
            dfCCDEDGEID = dfCCDEDGEID.drop_duplicates(["OrderID"], keep='last',).reset_index(drop=True)
            py.saveExcel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\Main\\EDGEID.xlsx','Sheet1',dfCCDEDGEID)
        
        if 'SIID' in name :
            dfCCDEDGEID = pd.read_excel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\Main\\SIID.xlsx')
            dfEDGEID = pd.read_csv(name,low_memory = False, error_bad_lines=False)
            dfCCDEDGEID= dfCCDEDGEID.append(dfEDGEID)
            print('Appending SIID')
            dfCCDEDGEID = dfCCDEDGEID.drop_duplicates(["OrderID"], keep='last',).reset_index(drop=True)
            py.saveExcel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\Main\\SIID.xlsx','Sheet1',dfCCDEDGEID)
           
        if 'WithoutID' in name :
            dfCCDEDGEID = pd.read_excel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\Main\\WithoutID.xlsx')
            dfEDGEID = pd.read_csv(name,low_memory = False, error_bad_lines=False)
            cols = ['Success Order without ID']
            dfEDGEID = dfEDGEID[cols]
            dfCCDEDGEID =dfCCDEDGEID[cols]
            dfCCDEDGEID= dfCCDEDGEID.append(dfEDGEID)
            print('Appending WithoutID')
            dfCCDEDGEID = dfCCDEDGEID.drop_duplicates(["Success Order without ID"], keep='first',).reset_index(drop=True)
            dfCCDEDGEID['temp']= 'WithoutID'
            py.saveExcel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\\Main\\WithoutID.xlsx','Sheet1',dfCCDEDGEID)
              
        if 'Failed' in name :
            dfCCDEDGEID = pd.read_excel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\Main\\Failed.xlsx')
            dfEDGEID = pd.read_csv(name,low_memory = False, error_bad_lines=False)
            dfCCDEDGEID= dfCCDEDGEID.append(dfEDGEID)
            print('Appending Failed')
            dfCCDEDGEID = dfCCDEDGEID.drop_duplicates(["OrderID"], keep='last',).reset_index(drop=True)
            py.saveExcel('C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\CCD\Main\\Failed.xlsx','Sheet1',dfCCDEDGEID)
            
      