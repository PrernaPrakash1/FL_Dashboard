# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:00:15 2018

@author: prerna.prakash
"""

import pandas as pd
import pycel as py
import datetime

class FLAnalysis :
    def __init__(self,df):
        self.df = df
        self.DateToday = datetime.date.today()
        self.month = str(self.DateToday.month) 
        self.day = str(self.DateToday.day)
        self.DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+self.day+self.month+"\\"  
        df = pd.read_excel("")
   


   
    def defineAnalysis(self,dfTriage) :
        for index,row in self.UIM.iterrows() :
            for sindex,rows in dfTriage.iterrows() :
                  if py.mathching(dfTriage.at[sindex,'LAST_TASK'],self.UIM.at[index,'LAST_TASK']) & py.mathching(dfTriage.at[sindex,'ERROR_MESSAGE1'],self.UIM.at[index,'ERROR_MESSAGE1']) & py.mathching(dfTriage.at[sindex,'ORDERTYPECODE'],self.UIM.at[index,'ORDERTYPECODE'])& py.mathching(dfTriage.at[sindex,'ORDER_TYPE'],self.UIM.at[index,'ORDER_TYPE']) & py.mathching(dfTriage.at[sindex,'SHIPPING'],self.UIM.at[index,'SHIPPING'])& py.mathching(dfTriage.at[sindex,'ORDER TYPECODE2'],self.UIM.at[index,'ORDER TYPECODE2']) & py.mathching(dfTriage.at[sindex,'COLLECT_TO_STORE/DELIVER_TO_STORE'],self.UIM.at[index,'COLLECT_TO_STORE/DELIVER_TO_STORE']) :
                 #if py.mathching(dfTriage.at[sindex,'Task Name'],self.External.at[index,'LAST_TASK']) :    
                    #print(dfTriage.at[index,'Task Name'],self.External.at[sindex,'LAST_TASK'])
                    
                    self.UIM.at[index,'Analysis'] = str(dfTriage.at[sindex,'Analysis'])
                                           #self.Billing.at[i,'NEXT ACTION'] = str(dfTriage.at[j,'Comments'])
                    break             
     
        return   self.UIM


    def Analysis(self,dfTriage) :
        self.UIM=  self.defineAnalysis(dfTriage)
        py.saveExcel(self.listOfConfigFile[4]+"\\UIMTriage.xlsx","Sheet1",self.UIM)
        return self.UIM