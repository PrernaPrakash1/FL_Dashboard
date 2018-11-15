# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:05:25 2018

@author: prerna.prakash
"""
import os
import pandas as pd
import pycel as py
import FLModule as fm
import datetime
class EDGE() :
    def __init__(self):
     self.DefaultPath = fm.getDefaultPath()  
        
     if os.path.exists(self.DefaultPath+"Edge.csv") == 'False' :
         return False
     else :
         cols = ['ORDER_REFERENCE','ORDER_TYPE','ORDER_RECEIVED_DATE','STATUS','SALES_ORDER_ID','SERVICE_ID','COMMITTED_DATE','USERNAME','PWD','STATUS_CODE','STATUS_MESSAGE','STATUS_TYPE']
         dfEDGE = pd.read_csv(self.DefaultPath+"Edge.csv",low_memory = False, error_bad_lines=False)
         dfEDGE = pd.read_csv(self.DefaultPath+"Edge.csv",low_memory = True, error_bad_lines=True,usecols = cols)
         
         dfEDGE[['Order Number','AID']] = dfEDGE['ORDER_REFERENCE'].str.split('_',n=1,expand=True)
         
         cols = ['Order Number','ORDER_TYPE','ORDER_RECEIVED_DATE','STATUS','SALES_ORDER_ID','SERVICE_ID','COMMITTED_DATE','USERNAME','PWD','STATUS_CODE','STATUS_MESSAGE','STATUS_TYPE']
         
         dfEDGE = dfEDGE[cols]
         
         dfEDGE['ORDER_RECEIVED_DATE'] = pd.to_datetime(dfEDGE['ORDER_RECEIVED_DATE'],format='%Y-%m-%d %H:%M:%S',yearfirst= True)         
         
         dfEDGE = dfEDGE.sort_values(by=['ORDER_RECEIVED_DATE'],ascending = False)
         
         dfEDGE = dfEDGE.drop_duplicates(["Order Number"], keep='first',).reset_index(drop=True)
         
         dfEDGE.rename(columns={'ORDER_TYPE':'EDGE ORDER TYPE_M','STATUS': 'EDGE STATUS_M','SALES_ORDER_ID':'Edge salesorderid_M','SERVICE_ID':'edge service ID_M','COMMITTED_DATE':'edge committed date_M','USERNAME':'edge username_M','PWD':'edge PW_M','STATUS_CODE':'edge status code_m','STATUS_MESSAGE':'edge status message_m','STATUS_TYPE':'edge status_type_m'}, inplace=True)
         
         py.saveExcel(self.DefaultPath+"FormattedEdge.xlsx",'Sheet1',dfEDGE)

