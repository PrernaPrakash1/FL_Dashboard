# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:42:13 2017

@author: prerna.prakash
"""

#FL 

import sys
import win32com.client
import zipfile
import pandas as pd
import datetime
import os
import time
start_time = time.time()
lists = []
cwd = os.getcwd()
print(cwd)
fobj = open(cwd+"\\config.txt")
for line in fobj:
    lists.append(line.rstrip())

names = ['SIEBEL','AID','AID2','STATUS','REASON']

# unzip all files in list from command line
aa = datetime.date.today()
month = str(aa.month)
day = str(aa.day)
print(datetime.date.today())

zip_ref = zipfile.ZipFile(lists[0], 'r')
zip_ref.extractall('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL'+day+month)
zip_ref.close()
print("FL unzipped")

pwds = b'jockey'
zip_ref = zipfile.ZipFile(lists[1], 'r')
zip_ref.extractall('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL'+day+month,pwd = pwds)
zip_ref.close()
print("SI unzipped")

pwds = b'jockey'
zip_ref = zipfile.ZipFile(lists[2], 'r')
zip_ref.extractall('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL'+day+month,pwd = pwds)
zip_ref.close()
print("EDGE unzipped")

zip_ref = zipfile.ZipFile(lists[3], 'r')
zip_ref.extractall('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL'+day+month,pwd = pwds)
zip_ref.close()
print("Consumer unzipped")

#zip_ref = zipfile.ZipFile(lists[4], 'r')
#zip_ref.extractall('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL'+day+month,pwd = pwds)
#zip_ref.close()
#print("SI unzipped")

#move to df
files = os.listdir("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\")
print("Files in '%s': %s " % (cwd, files))
files_xlsx = [f for f in files if f[-3:] == 'csv']
df = pd.read_csv("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"+files[0],low_memory = False)
df2 = pd.read_csv("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"+files[1],low_memory = False)
df1 = pd.read_csv("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"+files[2],low_memory = False)
df3 = pd.read_excel("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"+files[3],sheetname = 'All Orders')
df4 = pd.read_csv(lists[4],header=None,names = names)

#df3 = pd.read_csv("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+day+month+"\\"+files[3],low_memory = False)
#SPLIT oRDERNUMBER
df1[['Order_Number','AID']] = df1['Case Reference'].str.split('_',expand=True)
df2[['Order_Number','AID']] = df2['ORDER_REFERENCE'].str.split('_',n=1,expand=True)
df3[['Order_Number','AID']] = df3['Customer Order Refer'].str.split('_',expand=True)
df1['Created At'] = pd.to_datetime(df1['Created At'],format='%Y-%m-%d %H:%M:%S',yearfirst= True)
df2['ORDER_RECEIVED_DATE'] = pd.to_datetime(df2['ORDER_RECEIVED_DATE'],format='%Y-%m-%d %H:%M:%S',yearfirst= True)
df1 = df1.sort_values(by=['Created At'],ascending = False)
df2 = df2.sort_values(by=['ORDER_RECEIVED_DATE'],ascending = False)

#df2.sort_values(by=['ORDER_RECEIVED_DATE'])

writer = pd.ExcelWriter('C:\\Users\\prerna.prakash\\Desktop\\Input\\Checkthis.xlsx')
df2.to_excel(writer,'Sheet1',index = False)

writer.save() 

print("performing actions on SI")
i = 0
for each in df['Order Number']:
    j = 0 
    for feach in df1['Order_Number']:
        if each == feach :
            df['SI_STATUS'] = df1['Status']
            df['SI_Current Order Status'] = df1['Current Order Status']
            df['SI_Osf Order Reference Buyers Id'] = df1['Osf Order Reference Buyers Id']
            df['SI_Committed Date'] = df1['Committed Date']
            df['SI_Sub Order Type'] = df1['Sub Order Type']
            break
            
print("performing actions on EDGE")
i = 0
for each in df['Order Number']:
    j = 0 
    for feach in df2['Order_Number']:
        if each == feach :
            df['EDGE_SALES_ORDER_ID'] = df2['SALES_ORDER_ID']
            df['EDGE_SERVICE_ID'] = df2['SERVICE_ID']
            df['EDGE_ORDER_TYPE'] = df2['ORDER_TYPE']
            df['EDGE_STATUS'] = df2['STATUS']
            df['EDGE_STATUS_CODE'] = df2['STATUS_CODE']
            df['EDGE_STATUS_MESSAGE'] = df2['STATUS_MESSAGE']
            df['EDGE_STATUS_TYPE'] = df2['STATUS_TYPE']
            df['EDGE_USERNAME'] = df2['USERNAME']
            df['EDGE_PWD'] = df2['PWD']
            break
            
print("performing actions on Consumer Report")
i = 0
for each in df['Order Number']:
    j = 0 
    for feach in df3['Order_Number']:
        if each == feach :
            df['EDGE_ORRef'] = df3['ORRef']
            df['EDGE_PSTN Status'] = df3['PSTN Status']
            df['SI_SalesOrderRef'] = df3['SalesOrderRef']
            df['SI_STATUS'] = df3['Status']
            break

print("performing actions on SR Report")
i = 0
for each in df['Order Number']:
    j = 0 
    for feach in df4['SIEBEL']:
        if each == feach :
            df['SR_AID'] = df4['AID']
            df['SR_STATUS'] = df4['STATUS']
            df['SR_REASON'] = df4['REASON']
            break
            

writer = pd.ExcelWriter('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL'+day+month+'\\FL DASHBOARD.xlsx')
df.to_excel(writer,'Sheet1',index = False)

writer.save()     
print("File Saved")
print("--- %s seconds ---" % (time.time() - start_time))