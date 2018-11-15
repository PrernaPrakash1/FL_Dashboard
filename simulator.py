# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 18:57:52 2018

@author: prerna.prakash
"""
import FLAging as fa
import os
import FLnoCCD as CCD
import simFL 
import EDGE as ed
import pandas as pd
import pycel as py
import SI as si
import CONSUMER as cm
import SR as sr
import time
import FLModule as fm
import EDGEnSI as ES
import logging
import logging.config
import datetime
import Tracker as tk
import Carisma
import UnifyInputFiles as UF



logging.config.fileConfig('log4p.conf')
logger = logging.getLogger('simpleLogger')
startime = time.time()   
DateToday = datetime.date.today()

month = str(DateToday.month) 
day = str(DateToday.day)

setOfConfigFiles = fm.SetUpConfigFile("FLConfigFile.txt")

DefaultPath = fm.getDefaultPath()  
InputPath = setOfConfigFiles[1]

UIF = UF.UnifyInputFiles(InputPath,DefaultPath)
endtime = time.time()

logger.debug('files unzipped')
dfEDGE = ed.EDGE()
dfSI = si.SI()
dfCarisma = Carisma.Carisma()
#dfCONSUMER = cm.CONSUMER()
dfCONSUMER = sr.SR()
if os.path.exists(DefaultPath+"FLBBDashboard.csv"):
    df = pd.read_csv(DefaultPath+"FLBBDashboard.csv",low_memory = False, error_bad_lines=False)
elif os.path.exists(DefaultPath+"FLBBDashboard.xlsx"):
    df = pd.read_excel(DefaultPath+"FLBBDashboard.xlsx")
print("No of Rows are 54 ",len(df))
df =fm.removeDuplicates(df)    
print("No of Rows are 56 ",len(df))
dfEDGE = pd.read_excel(DefaultPath+"FormattedEdge.xlsx")
dfSI= pd.read_excel(DefaultPath+"FormattedSI.xlsx")
#dfCONSUMER= pd.read_excel(DefaultPath+"FormattedConsumer.xlsx")
dfSR= pd.read_excel(DefaultPath+"SRFormatted.xlsx")

dfCarisma= pd.read_excel(DefaultPath+"CarismaFormatted.xlsx")
df = df.merge(dfEDGE,how='left', on='Order Number')
print("No of Rows are 63 ",len(df))
df = df.merge(dfSI,how='left', on='Order Number')
print("No of Rows are 65 ",len(df))
#df = df.merge(dfCONSUMER,how='left', on='Order Number')
df = df.merge(dfSR,how='left', on='Order Number')
print("No of Rows are 68 ",len(df))

df = df.merge(dfCarisma,how='left', on='Order Number')
print("No of Rows are 71 ",len(df))

endtime = time.time()
logger.debug('Files Formatted')
templist = fm.category(df)
logger.debug('Files Formatted1')
print("No of Rows are 73 ",len(df))
logger.debug('Files Formatted2')
df['Category'] = templist
logger.debug('Files Formatted3')
EnS = ES.EDGEnSI() 
logger.debug('Files Formatted4')          
df =EnS.defineAnalysisEDGE(df)
logger.debug('Files Formatted5')
print("No of Rows are 77 ",len(df))
df =EnS.defineAnalysisSI(df)
print("No of Rows are 79 ",len(df))
#FLAging = fa.FLAging(df) 
endtime = time.time()
logger.debug('Age Added')

print("No of Rows are 85 ",len(df))
Tracker = tk.Tracker()
df = Tracker.Apply(df)
FLnoCCD = CCD.FLnoCCD()
dfEDGEID = pd.read_excel(InputPath+"\\CCD\Main\\EDGEID.xlsx")
dfEDGEID.rename(columns={'OrderID': 'Order Number','EDGEID':'TILVFC'}, inplace=True)
Failed= pd.read_excel(InputPath+"\\CCD\Main\\Failed.xlsx")
Failed.rename(columns={'OrderID': 'Order Number','APP':'TILFAILED','Reason':'TILERROR'}, inplace=True)
SIID = pd.read_excel(InputPath+"\\CCD\Main\\SIID.xlsx")
SIID.rename(columns={'OrderID': 'Order Number','SIID':'TIL ORID'}, inplace=True)
WithoutID = pd.read_excel(InputPath+"\\CCD\\Main\\WithoutID.xlsx")
WithoutID.rename(columns={'Success Order without ID': 'Order Number','temp':'TIL SUCCESS'}, inplace=True)
df = df.merge(dfEDGEID,how='left', on='Order Number')
print("No of Rows are 92 ",len(df))
df = df.merge(Failed,how='left', on='Order Number')
print("No of Rows are 94 ",len(df))
df = df.merge(SIID,how='left', on='Order Number')
print("No of Rows are 96 ",len(df))
df = df.merge(WithoutID,how='left', on='Order Number')
list1 = []
#cols = ['Order Number','Payment Type','OrderType Code','Revision','Channel','Order Status','Account  Number','Delivery Method','Delivery Status','Status Date','Division','OSM ID','OSM Reference Number','Status','Task Description','Error Message','Error Message2','Open Validity','Shipping Flag','CARISMA Status','Order Submit Date','PSTN Service id','FL Prod Id','Fl Commited Date','FL Line Item Status','FL Fulflmnt Status','Fixedline ctn network status','BB Service Id','BB Prod Id','BB Line Item Status','BB ctn network status','BB Fulflmnt Status','BB Commited Date','Router Service id','Router Prod Id','Router  Fulflmnt  Status','Router Line Item Status','Router','CARISMA Dispatch Date','CARISMA Pick Date','CARISMA Created Date','CARISMA Error Message','Edge sales order Id','Edge completed date','Edge Committed Date','Edge order status','Edge order received date','Edge customer required date','Edge username','Edge password','Edge status code','Edge status message','Edge status received date','Fixed Line DN Number','SI sales order id','SI order status','SI created date','SI sub order type','SI completed date','SI committed date','SI cancellation reason','Edge order type','Edge status type','FL OSM ID','FL TIL Status','BB OSM ID','BB TIL Status','OSM Task Name','OSM Start Time','Error Message2','BB Action CD','Router Action CD','FL Action CD','SR_NUM_M','SR TITLE_M','SR DESC_M','SI status_M','Edge status_M','SI sales orderid_M','Edge salesorderid_M','edge service ID_M','Edge ORDER_Type_M','Edge Committed Date_M','edge status code_M','edge status message_M','edge status_type_M','edge username_M','edge PW_M','SI sub order type_M','SI committed date_M','Category']
#cols = ['Order Number','Payment Type','OrderType Code','Revision','Channel','Order Status','Account  Number','Delivery Method','Delivery Status','Status Date','Division','OSM ID','OSM Reference Number','Status','Task Description','Error Message','Error Message2','Open Validity','Shipping Flag','CARISMA Status','Order Submit Date','PSTN Service id','FL Prod Id','Fl Commited Date','FL Line Item Status','FL Fulflmnt Status','Fixedline ctn network status','BB Service Id','BB Prod Id','BB Line Item Status','BB ctn network status','BB Fulflmnt Status','BB Commited Date','Router Service id','Router Prod Id','Router  Fulflmnt  Status','Router Line Item Status','Router','CARISMA Dispatch Date','CARISMA Pick Date','CARISMA Created Date','CARISMA Error Message','Edge sales order Id','Edge completed date','Edge Committed Date','Edge order status','Edge order received date','Edge customer required date','Edge username','Edge password','Edge status code','Edge status message','Edge status received date','Fixed Line DN Number','SI sales order id','SI order status','SI created date','SI sub order type','SI completed date','SI committed date','SI cancellation reason','Edge order type','Edge status type','FL OSM ID','FL TIL Status','BB OSM ID','BB TIL Status','OSM Task Name','OSM Start Time','Error Message2.1','BB Action CD','Router Action CD','FL Action CD','Account Type','BB Service ID','SR_NUM','SR TITLE','SR DESC','SI status_M','EDGE STATUS_M','SI sales orderid_M','Edge salesorderid_M','edge service ID_M','EDGE ORDER TYPE_M','edge committed date_M','edge status code_m','edge status message_m','edge status_type_m','edge username_M','edge PW_M','SI sub order type_M','SI Committed date_M','Category','tempDate','AgeCCD','AgeCCDCategory','AgeSubmitDate','AgeSubmitDateCategory']
logger.debug('Adding Tracker')

logger.debug('Added Tracker')
py.saveExcel(DefaultPath+"FormattedFLBBDasboardFinal.xlsx",'Sheet1',df)
endtime = time.time()
print(startime-endtime)
print("No of Rows are 103 ",len(df))
"""
df = pd.read_excel(DefaultPath+"FormattedFLBBDasboardFinal.xlsx")


list1= []
list2 = []
df = pd.read_excel(DefaultPath+"FormattedFLBBDasboardcheckAge.xlsx")
print("No of Rows are 108 ",len(df))
list1.append(len(df[(df['AgeSubmitDateCategory']=='less than 1')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='1+')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='3+')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='7+')].index))

list1.append(len(df[(df['AgeSubmitDateCategory']=='15+')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='30+')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='45+')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='60+')].index))
list1.append(len(df[(df['AgeSubmitDateCategory']=='90+')].index))
for each in list1 :
    list2.append(str(each))
endtime = time.time()
print(list2)
fm.browser(list2)
print("TIL Status Added:",endtime-strtime)

"""