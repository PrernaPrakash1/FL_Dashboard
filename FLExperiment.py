# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:38:47 2018

@author: prerna.prakash
"""

import pandas as pd
import zipfile
import UnifyInputFiles as UF
import datetime
import FLModule as fm
import os
import time

"""
class FLReport() :
    def main() :
        return False
""" 
strtime = time.time()   
DateToday = datetime.date.today()
month = str(DateToday.month)
day = str(DateToday.day)

setOfConfigFiles = fm.SetUpConfigFile("FLConfigFile.txt")
DefaultPath = setOfConfigFiles[0]
inputPath=setOfConfigFiles[1]
DefaultPath = DefaultPath+"\\FL"+day+month+"\\"
#DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"  
#inputPath = "C:\\Users\\prerna.prakash\\Downloads\\new"
UIF = UF.UnifyInputFiles(inputPath,DefaultPath)

os.chdir(DefaultPath)
names = ['SIEBEL','AID','AID2','STATUS','REASON']

dfSR  = pd.read_csv(DefaultPath+"FLSR.csv",header= None,names= names,low_memory = False, error_bad_lines=False)
dfSR = dfSR.iloc[:,0:5] 
dfFLDB = pd.read_csv(DefaultPath+"FLBBDashboard.csv",low_memory = False, error_bad_lines=False)
dfEdge = pd.read_csv(DefaultPath+"Edge.csv",low_memory = False, error_bad_lines=False)
dfSI = pd.read_csv(DefaultPath+"SI.csv",low_memory = False, error_bad_lines=False)
dfConsumer = pd.read_excel(DefaultPath+"Consumer.xlsx",sheetname = 'All Orders')


dfSI[['Order_Number','AID']] = dfSI['Case Reference'].str.split('_',n=1,expand=True)
dfEdge[['Order_Number','AID']] = dfEdge['ORDER_REFERENCE'].str.split('_',n=1,expand=True)
dfConsumer[['Order_Number','AID']] = dfConsumer['Customer Order Refer'].str.split('_',n=1,expand=True)
dfSI['Created At'] = pd.to_datetime(dfSI['Created At'],format='%Y-%m-%d %H:%M:%S',yearfirst= True)
dfSI['Committed Date'] = pd.to_datetime(dfSI['Committed Date'],format='%Y-%m-%d %H:%M:%S',yearfirst= True)
dfEdge['ORDER_RECEIVED_DATE'] = pd.to_datetime(dfEdge['ORDER_RECEIVED_DATE'],format='%Y-%m-%d %H:%M:%S',yearfirst= True)
dfSI = dfSI.sort_values(by=['Created At'],ascending = False)
dfSI = dfSI.reset_index(drop=True)
dfEdge = dfEdge.sort_values(by=['ORDER_RECEIVED_DATE'],ascending = False)
dfEdge = dfEdge.reset_index(drop=True)

fm.saveExcel(DefaultPath+"FormattedSI.xlsx","Sheet1",dfSI)
fm.saveExcel(DefaultPath+"FormattedEdge.xlsx","Sheet1",dfEdge)

print("Time taken :",time.time()- strtime)

fm.vlookup(dfFLDB,dfSI,"Order Number","Order_Number",["Status","Current Order Status","Osf Order Reference Buyers Id","Committed Date","Sub Order Type"],"SI ")
print("Time taken :",time.time()- strtime)
fm.vlookup(dfFLDB,dfEdge,"Order Number","Order_Number",["SALES_ORDER_ID","SERVICE_ID","ORDER_TYPE","STATUS","STATUS_CODE","STATUS_MESSAGE","STATUS_TYPE","USERNAME","PWD"],"Edge ")
fm.vlookup(dfFLDB,dfConsumer,"Order Number","Customer Order Refer",["ORRef","PSTN Status"],"Edge")
fm.vlookup(dfFLDB,dfConsumer,"Order Number","Customer Order Refer",["SalesOrderRef","Status"],"SI")
fm.vlookup(dfFLDB,dfSR,"Order Number","SIEBEL",["AID","STATUS","REASON"],"SR")


fm.saveExcel(DefaultPath+"FormattedFLBBDasboard.xlsx","Sheet1",dfFLDB)
endtime = time.time()
print("Time taken :",endtime- strtime)

"""


print("Sort and Split")


""" 