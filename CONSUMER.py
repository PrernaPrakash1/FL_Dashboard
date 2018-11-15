# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:17:51 2018

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
import FLModule as fm

class CONSUMER() :
    def __init__(self):

        self.DefaultPath = fm.getDefaultPath()
        
        if os.path.exists(self.DefaultPath+"Consumer.xlsx") == 'False' :
            return False
        else :
         dfCONSUMER = pd.read_excel(self.DefaultPath+"Consumer.xlsx",sheetname = 'All Orders')
         
         dfCONSUMER[['Order Number','AID']] = dfCONSUMER['Customer Order Refer'].str.split('_',n=1,expand=True)
         
         col = ['Order Number','ORRef',"PSTN Status","SalesOrderRef","Status"]
         
         dfCONSUMER = dfCONSUMER[col]

         
         dfCONSUMER.rename(columns={'ORRef': 'Consumer SI sales orderid_M','PSTN Status':'Consumer SI status_M','SalesOrderRef':'Consumer EDGE SalesOrderID_M','STATUS_CODE':'edge status code_m','STATUS_MESSAGE':'edge status message_m','STATUS_TYPE':'edge status_type_m','Status':'Consumer EDGE status_M'}, inplace=True)
         
         py.saveExcel(self.DefaultPath+"FormattedConsumer.xlsx",'Sheet1',dfCONSUMER)

#check consumer columns