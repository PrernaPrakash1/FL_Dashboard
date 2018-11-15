# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:42:10 2018

@author: prerna.prakash
"""

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
import datetime
import UnifyInputFiles as UF



strtime = time.time()   
DateToday = datetime.date.today()

month = str(DateToday.month) 
day = str(DateToday.day)

setOfConfigFiles = fm.SetUpConfigFile("FLConfigFile.txt")
DefaultPath+" = setOfConfigFiles[0]
inputPath=setOfConfigFiles[1]
DefaultPath = DefaultPath+"+"\\FL"+day+month+"\\"
#DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"  
#inputPath = "C:\\Users\\prerna.prakash\\Desktop\\FL\\Input"

UIF = UF.UnifyInputFiles(inputPath,DefaultPath)
endtime = time.time()
cols = ['Order Number','Revision','Status','Submit date','Status date','Order Type','FL prod id','FL_service_no','FL_Line_item_status','FL fullfilment status','Fl Commited Date','BB Prod Id','BB_service_no','BB_Line_item_status','BB fullfilment status','BB Commited Date','a','b','c','d','e']

print("Time taken to unzip files and process files",endtime-strtime)
dfEDGE = ed.EDGE()
dfSI = si.SI()
#dfCONSUMER = cm.CONSUMER()
dfSR = sr.SR() 

df = pd.read_excel(DefaultPath+"Siebel Report.xlsx")
df.columns = cols
dfEDGE = pd.read_excel(DefaultPath+"FormattedEdge.xlsx")
dfSI= pd.read_excel(DefaultPath+"FormattedSI.xlsx")
#dfCONSUMER= pd.read_excel(DefaultPath+"FormattedConsumer.xlsx")
dfSR= pd.read_excel(DefaultPath+"SRFormatted.xlsx")
df = df.merge(dfEDGE,how='left', on='Order Number')
df = df.merge(dfSI,how='left', on='Order Number')
#df = df.merge(dfCONSUMER,how='left', on='Order Number')
df = df.merge(dfSR,how='left', on='Order Number')
py.saveExcel(DefaultPath+"FormattedFLBBDasboard.xlsx",'Sheet1',df)
endtime = time.time()
print("FLBB Dashboard created with SI,EDGE and SR DATA",strtime-endtime)
templist = fm.CategoryforSiebelReport(df)
df['Category'] = templist
EnS = ES.EDGEnSI() 
df =EnS.defineAnalysisEDGE(df)

FLAging = fa.FLAging(df) 
endtime = time.time()
print("Age Added",endtime-strtime)
print("Time taken is:",endtime-strtime)
df = pd.read_excel(DefaultPath+"FormattedFLBBDasboard1.xlsx")
FLnoCCD = CCD.FLnoCCD()
dfEDGEID = pd.read_excel("C:\\Users\\prerna.prakash\\Downloads\\new\\CCD\\Main\\EDGEID.xlsx")
Failed= pd.read_excel("C:\\Users\\prerna.prakash\\Downloads\\new\\CCD\\Main\\Failed.xlsx")
SIID = pd.read_excel("C:\\Users\\prerna.prakash\\Downloads\\new\\CCD\\Main\\SIID.xlsx")
WithoutID = pd.read_excel("C:\\Users\\prerna.prakash\\Downloads\\new\\CCD\\Main\\WithoutID.xlsx")
df = df.merge(dfEDGEID,how='left', on='Order Number')

df = df.merge(Failed,how='left', on='Order Number')

df = df.merge(SIID,how='left', on='Order Number')

#df = df.merge(WithoutID, on='Order Number')
list1 = []
cols = ['Order Number','Payment Type','OrderType Code','Revision','Channel','Order Status','Account  Number','Delivery Method','Delivery Status','Status Date','Division','OSM ID','OSM Reference Number','Status','Task Description','Error Message','Error Message2','Open Validity','Shipping Flag','CARISMA Status','Order Submit Date','PSTN Service id','FL Prod Id','Fl Commited Date','FL Line Item Status','FL Fulflmnt Status','Fixedline ctn network status','BB Service Id','BB Prod Id','BB Line Item Status','BB ctn network status','BB Fulflmnt Status','BB Commited Date','Router Service id','Router Prod Id','Router  Fulflmnt  Status','Router Line Item Status','Router','CARISMA Dispatch Date','CARISMA Pick Date','CARISMA Created Date','CARISMA Error Message','Edge sales order Id','Edge completed date','Edge Committed Date','Edge order status','Edge order received date','Edge customer required date','Edge username','Edge password','Edge status code','Edge status message','Edge status received date','Fixed Line DN Number','SI sales order id','SI order status','SI created date','SI sub order type','SI completed date','SI committed date','SI cancellation reason','Edge order type','Edge status type','FL OSM ID','FL TIL Status','BB OSM ID','BB TIL Status','OSM Task Name','OSM Start Time','Error Message2','BB Action CD','Router Action CD','FL Action CD','SR_NUM_M','SR TITLE_M','SR DESC_M','SI status_M','Edge status_M','SI sales orderid_M','Edge salesorderid_M','Consumer SI status_M','Consumer EDGE status_M','Consumer SI sales orderid_M','Consumer Edge salesorderid_M','edge service ID_M','Edge ORDER_Type_M','Edge Committed Date_M','edge status code_M','edge status message_M','edge status_type_M','edge username_M','edge PW_M','SI sub order type_M','SI committed date_M','Category']
cols = ['Order Number','Payment Type','OrderType Code','Revision','Channel','Order Status','Account  Number','Delivery Method','Delivery Status','Status Date','Division','OSM ID','OSM Reference Number','Status','Task Description','Error Message','Error Message2','Open Validity','Shipping Flag','CARISMA Status','Order Submit Date','PSTN Service id','FL Prod Id','Fl Commited Date','FL Line Item Status','FL Fulflmnt Status','Fixedline ctn network status','BB Service Id','BB Prod Id','BB Line Item Status','BB ctn network status','BB Fulflmnt Status','BB Commited Date','Router Service id','Router Prod Id','Router  Fulflmnt  Status','Router Line Item Status','Router','CARISMA Dispatch Date','CARISMA Pick Date','CARISMA Created Date','CARISMA Error Message','Edge sales order Id','Edge completed date','Edge Committed Date','Edge order status','Edge order received date','Edge customer required date','Edge username','Edge password','Edge status code','Edge status message','Edge status received date','Fixed Line DN Number','SI sales order id','SI order status','SI created date','SI sub order type','SI completed date','SI committed date','SI cancellation reason','Edge order type','Edge status type','FL OSM ID','FL TIL Status','BB OSM ID','BB TIL Status','OSM Task Name','OSM Start Time','Error Message2.1','BB Action CD','Router Action CD','FL Action CD','Account Type','BB Service ID','AID_M','SR_STATUS_M','REASON_M','SI status_M','EDGE STATUS_M','SI sales orderid_M','Edge salesorderid_M','Consumer SI status_M','Consumer EDGE status_M','Consumer SI sales orderid_M','Consumer EDGE SalesOrderID_M','edge service ID_M','EDGE ORDER TYPE_M','edge committed date_M','edge status code_m','edge status message_m','edge status_type_m','edge username_M','edge PW_M','SI sub order type_M','SI Committed date_M','Category','tempDate','AgeCCD','AgeCCDCategory','AgeSubmitDate','AgeSubmitDateCategory']
df = df[cols]
py.saveExcel(DefaultPath+"FormattedFLBBDasboardFinal.xlsx",'Sheet1',df)

list1= []
list2 = []
df = pd.read_excel(DefaultPath+"FormattedFLBBDasboardcheckAge.xlsx")
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

