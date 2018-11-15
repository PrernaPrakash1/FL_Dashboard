# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:58:23 2018

@author: prerna.prakash
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:05:25 2018

@author: prerna.prakash
"""
import os
import pandas as pd
import pycel as py
from datetime import datetime,date,timedelta

class SR() :
    def __init__(self):
     self.DateToday = date.today()
     yesterday = date.today()- timedelta(1)
     print(yesterday)
     yesterday = date.today()- timedelta(1)
     print(type(yesterday))
     print(yesterday.day)
     print(yesterday.month)
     self.DefaultPath = 'C:\\Users\\prerna.prakash\\Desktop\\Input'
     self.month = str(self.DateToday.month) 
     self.day = str(self.DateToday.day)
     while True :
            if os.path.exists(self.DefaultPath+"\\FL"+str(yesterday.day)+str(yesterday.month)) == True :
                break
            else :
                yesterday = yesterday-timedelta(1)
            print(self.DefaultPath+"\\FL"+str(yesterday.day)+str(yesterday.month))
    
     self.DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+self.day+self.month+"\\"  
  
     if os.path.exists(self.DefaultPath+"FLSR.csv") == 'False' :
         return False
     elif os.path.exists(self.DefaultPath+"FLSR.xlsx"):
         names = ['Order Number','Date','AID','AID2','STATUS','REASON']
         #,'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
         #,'a','a','a','a','a','a'
         dfSR  = pd.read_excel(self.DefaultPath+"FLSR.xlsx",header= None,names= names,parse_cols = "A:F")


         dfSR = dfSR.iloc[:,0:6] 
        
         SRcol = ['Order Number','Date',"AID","STATUS","REASON"]
         
         dfSR = dfSR[SRcol]
         
         dfSR['Date'] = pd.to_datetime(dfSR['Date'],format='%d-%m-%Y %H:%M:%S',yearfirst= True)         
         
         dfSR = dfSR.sort_values(by=['Date'],ascending = False)
         
         dfSR = dfSR.drop_duplicates(['Order Number']).reset_index(drop= 'True')
         
         dfSR.rename(columns={'AID': 'SR_NUM','STATUS':'SR TITLE','REASON':'SR DESC'}, inplace=True)
         
         py.saveExcel(self.DefaultPath+"SRFormatted.xlsx",'Sheet1',dfSR)

         
     else :
         names = ['Order Number','Date','AID','AID2','STATUS','REASON']
         dfSR  = pd.read_csv(self.DefaultPath+"FLSR.csv",header= None,names= names,low_memory = False, error_bad_lines= True)

         dfSR = dfSR.iloc[:,0:6] 
        
         SRcol = ['Order Number','Date',"AID","STATUS","REASON"]
         
         dfSR = dfSR[SRcol]
         
         dfSR['Date'] = pd.to_datetime(dfSR['Date'],yearfirst= True)    
         
         dfSR = dfSR.sort_values(by=['Date'],ascending = False)

         dfSR = dfSR.drop_duplicates(['Order Number']).reset_index(drop= 'True')
         
         dfSR.rename(columns={'AID': 'SR_NUM','STATUS':'SR TITLE','REASON':'SR DESC'}, inplace=True)
         
         py.saveExcel(self.DefaultPath+"SRFormatted.xlsx",'Sheet1',dfSR)

