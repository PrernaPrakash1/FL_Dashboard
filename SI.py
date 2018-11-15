# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:50:43 2018

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
import datetime
class SI() :
    def __init__(self):
     self.DateToday = datetime.date.today()
     self.month = str(self.DateToday.month) 
     self.day = str(self.DateToday.day)
     self.DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+self.day+self.month+"\\"  
        
     if os.path.exists(self.DefaultPath+"SI.csv") == 'False' :
         return False
     else :
         cols = ['Case Reference','Created At','Current Order Status','Osf Order Reference Buyers Id','Committed Date','Sub Order Type']
         dfSI = pd.read_csv(self.DefaultPath+"SI.csv",usecols = cols,low_memory = True, error_bad_lines=True)
         
         dfSI[['Order Number','AID']] = dfSI['Case Reference'].str.split('_',n=1,expand=True)
         py.saveExcel(self.DefaultPath+"FormattedSI3.xlsx",'Sheet1',dfSI)
         print("Columns in SI",len(dfSI.index))
         
         dfSI['Created At'] = pd.to_datetime(dfSI['Created At'],errors = 'ignore',infer_datetime_format=True,yearfirst= True,exact=False)         
         py.saveExcel(self.DefaultPath+"FormattedSI2.xlsx",'Sheet1',dfSI)
         print("Columns in SI",len(dfSI.index))
         #dfSI = dfSI.sort_values(by=['Created At'],ascending = True)
         dfSI = dfSI.sort_values(by=['Created At'],ascending = False)
         py.saveExcel(self.DefaultPath+"FormattedSI1.xlsx",'Sheet1',dfSI)
         dfSI.drop_duplicates('Order Number', keep='first',).reset_index(drop=True)
         print("Columns in SI",len(dfSI.index))
         #dfSI.drop_duplicates('Order Number', keep='last',).reset_index(drop=True)
        
         print("Columns in SI",len(dfSI.index))
         dfSI.rename(columns={'Osf Order Reference Buyers Id':'SI sales orderid_M','Current Order Status': 'SI status_M','Committed Date':'SI Committed date_M','Sub Order Type':'SI sub order type_M'}, inplace=True)
         
         py.saveExcel(self.DefaultPath+"FormattedSI.xlsx",'Sheet1',dfSI)

