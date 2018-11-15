# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:49:07 2018

@author: prerna.prakash
"""

import pandas as pd
import zipfile
import os
import datetime
import webbrowser

import numpy as np


def CCD(filename) :
    unzipfile(filename,filename,'')

    
def rename(fileName) :
    if 'SI' in fileName :

        return 'SI'
    if 'Siebel' in fileName :

        return 'Siebel Report'
    if 'siebel' in fileName :

        return 'Siebel Report'
    
    elif 'BB' in fileName :

        return 'FLBBDashboard'
    elif 'EDGE' in fileName :

        return 'Edge'
    elif 'Line' in fileName :

        return 'Edge'
    elif 'Consumer'  in fileName :

        return 'Consumer'
    
    elif 'SR' in fileName :

        return 'FLSR'
    
    elif 'Tracker' in fileName :

        return 'Tracker'
    
    elif 'Carisma' in fileName :

        return 'Carisma'
    
    
def CCDrename(fileName) :
    if 'Failed' in fileName :

        return 'Failed'
    elif 'EDGEID' in fileName :

        return 'EDGEID'
   
    elif 'WithoutID' in fileName :

        return 'WithoutID'
    elif 'SIID' in fileName :

        return 'SIID'


def unzipfile(FilePath,fileSavePath,pswrd) :
    
    zip_ref = zipfile.ZipFile(FilePath, 'r')
    zip_ref.extractall(fileSavePath,pwd = pswrd)
    zip_ref.close()
    
    
def vlookup(dfbase,dfcopyfrom,DfBaseElement,DfCopyFromeElement,listofElements,name) :
    print("Applying Vlookup.")
 
    i = 0
    for each in dfbase[DfBaseElement] :
        j = 0
        for feach in dfcopyfrom[DfCopyFromeElement]:          
            if each == feach :
                k =0
                for preach in listofElements : 
                     
                    dfbase.at[i,name[k]] = str(dfcopyfrom.at[j,preach])
                    k = k+1
                break
                
            j = j+1
        i = i+1
    return dfbase 

def saveExcel(FileName,Sheetname,df) :
    writer = pd.ExcelWriter(FileName)
    df.to_excel(writer,index = False)
    writer.save()
    
def readcsvAddHeader(file,names):
    df = pd.read_csv(file,names,low_memory = False, error_bad_lines=False)
    return df
    
def readFilecsv(FilePath) :
    df = pd.read_csv(FilePath, error_bad_lines=False)
    return df

def SetUpConfigFile(name) :
    listOfConfigDetails = []
    cwd = os.path.expanduser("~")
    print(cwd)
    fobj = open(cwd+"\\"+name)   
    for line in fobj:
        listOfConfigDetails.append(line.rstrip())
    return listOfConfigDetails


def Category(dfMain) :
        
        dfMain['Fl Commited Date'] = pd.to_datetime(dfMain['Fl Commited Date'],dayfirst=True)
        dfMain['BB Commited Date']  = pd.to_datetime(dfMain['BB Commited Date'],dayfirst=True)
        dfMain['Edge Committed Date'] = pd.to_datetime(dfMain['Edge Committed Date'],dayfirst=True)
        dfMain['SI committed date'] = pd.to_datetime(dfMain['SI committed date'],dayfirst=True)
        dfMain['edge committed date_M'] = pd.to_datetime(dfMain['edge committed date_M'],dayfirst=True)
        dfMain['SI Committed date_M'] = pd.to_datetime(dfMain['SI Committed date_M'],dayfirst=True)
        
        now = datetime.datetime.now()
        print(now)
        i = 0
        templist = []
        for each in dfMain['Order Number'] :
            if (dfMain.at[i,'Fl Commited Date']-now).days>= 0 :
                    templist.append('Amber')
            elif (dfMain.at[i,'BB Commited Date']-now).days >= 0 :
                templist.append('Amber')   
            elif (dfMain.at[i,'Edge Committed Date']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'SI committed date']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'edge committed date_M']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'SI Committed date_M']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'Fl Commited Date']-now).days< 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'BB Commited Date']-now).days < 0 :
                templist.append('Backlog')   
            elif (dfMain.at[i,'Edge Committed Date']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'SI committed date']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'edge committed date_M']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'SI Committed date_M']-now).days < 0 :
                templist.append('Backlog')
            else :
                templist.append('NOCCD')
            i = i+1
        return templist  


def category(dfMain) :
        now = datetime.datetime.now()
        dfMain['Fl Commited Date'] = pd.to_datetime(dfMain['Fl Commited Date'],dayfirst=True)
        dfMain['BB Commited Date']  = pd.to_datetime(dfMain['BB Commited Date'],dayfirst=True)
        #dfMain['Edge Committed Date'] = pd.to_datetime(dfMain['Edge Committed Date'],dayfirst=True)
        #dfMain['SI committed date'] = pd.to_datetime(dfMain['SI committed date'],dayfirst=True)
        dfMain['edge committed date_M'] = pd.to_datetime(dfMain['edge committed date_M'],dayfirst=True)
        dfMain['SI Committed date_M'] = pd.to_datetime(dfMain['SI Committed date_M'],dayfirst=True)
        flc = dfMain['Fl Commited Date'].isnull()
        flb = dfMain['BB Commited Date'].isnull()
        fle = dfMain['edge committed date_M']
        fls = dfMain['SI Committed date_M']
        flm = (flc & flb)
        dfMain['flm']=flm.replace(False,'NO CCD')
        
        dfMain['fle'] = fle.apply(lambda x:'Amber' if (x-now).days >= 0 else 'Backlog')
        dfMain['fls'] = fls.apply(lambda x: 'Amber' if (x - now).days >= 0 else 'Backlog')
        #dfMain['flm'] = dfMain[['Fl Commited Date','BB Commited Date']].apply(lambda x,y : 'Amber' if x == 'NO CCD'  else 'k' ,axis = 1)

        i = 0
        templist = []
        for each in dfMain['Order Number'] :           
            if pd.isnull(dfMain.at[i,'Fl Commited Date']) and pd.isnull(dfMain.at[i,'BB Commited Date']):
                 
                    templist.append('No CCD')
                    if  (dfMain.at[i,'edge committed date_M']-now).days >= 0 :
                        templist.pop()  
                        templist.append('Amber')
                    elif (dfMain.at[i,'SI Committed date_M']-now).days >= 0 :
                        templist.pop()  
                        templist.append('Amber')
                    elif (dfMain.at[i,'SI Committed date_M']-now).days < 0 :
                        templist.pop()  
                        templist.append('Backlog')
                    elif (dfMain.at[i,'SI Committed date_M']-now).days < 0 :
                        templist.pop()  
                        templist.append('Backlog')
            else :
               templist.append('not updated') 
            """
            elif (dfMain.at[i,'BB Commited Date']-now).days >= 0 :
                templist.append('Amber')   
            elif (dfMain.at[i,'Edge Committed Date']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'SI committed date']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'edge committed date_M']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'SI Committed date_M']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'Fl Commited Date']-now).days< 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'BB Commited Date']-now).days < 0 :
                templist.append('Backlog')   
            elif (dfMain.at[i,'Edge Committed Date']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'SI committed date']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'edge committed date_M']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'SI Committed date_M']-now).days < 0 :
                templist.append('Backlog')
            else :
                templist.append('NOCCD')
            i = i+1
        """
        return templist 
        
    
def CategoryforSiebelReport(dfMain) :
        
        dfMain['Fl Commited Date'] = pd.to_datetime(dfMain['Fl Commited Date'],dayfirst=True)
        dfMain['BB Commited Date']  = pd.to_datetime(dfMain['BB Commited Date'],dayfirst=True)
       
        print(dfMain['Fl Commited Date'])
        now = datetime.date.today()
        print(now)
        i = 0
        templist = []

        for each in dfMain['Order Number'] :
            print(each)
            if (dfMain.at[i,'BB Commited Date']-now).days>= 0 :
                    print('Amber')
                    templist.append('Amber')
            elif (dfMain.at[i,'BB Commited Date']-now).days >= 0 :
                templist.append('Amber')   
            elif (dfMain.at[i,'Fl Commited Date']-now).days< 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'BB Commited Date']-now).days < 0 :
                templist.append('Backlog')   
            else :
                templist.append('NOCCD')
            i = i+1
        return templist
    
    
def removeDuplicates(dfMain) :
    dfExchange = dfMain[dfMain['OrderType Code']== 'E']
    dfNotExchange = dfMain[dfMain['OrderType Code']!= 'E']
    dftemp = pd.concat(g for _, g in dfExchange.groupby("Order Number") if len(g) > 1)
    dfDupl = dftemp['Order Number'].tolist()

    for index,row in dfExchange.iterrows() : 
        if dfExchange.at[index,'Order Number'] in dfDupl and dfExchange.at[index,'Router Action CD'] == 'Delete' :            
            dfExchange = dfExchange.drop(index)
        elif dfExchange.at[index,'Order Number'] not in dfDupl and dfExchange.at[index,'Router Action CD'] == 'Delete' :  
            dfExchange.at[index,'Router Service id'] = ''
        elif dfExchange.at[index,'Order Number'] in dfDupl and dfExchange.at[index,'Router Action CD'] == 'Delete' and pd.isnull(dfExchange.at[index,'Router Service id']) :
            dfExchange = dfExchange.drop(index)
        
    dfNotExchange = dfNotExchange.sort_values(by=['Revision'],ascending = False)
    dfNotExchange = dfNotExchange.drop_duplicates(['Order Number']).reset_index(drop=True)
    dfMain = pd.concat([dfExchange, dfNotExchange], ignore_index=True)
    return dfMain

def getDefaultPath() :

    DateToday = datetime.date.today()
    month = str(DateToday.month) 
    day = str(DateToday.day)
    setOfConfigFiles = SetUpConfigFile("FLConfigFile.txt")
    DefaultPath = setOfConfigFiles[0]+day+month+"\\"
    return DefaultPath

def browser(listofnumbers) :
        f = open('Report.html','w')
        message = """<!DOCTYPE html>
        
        <html>
        <head>
        <style>

        body {
            background-color: white;
        }
        
        h1 {
        
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            color: #FF6347 ;
            text-align: center;
        }
        h2 {
        
        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            color: black;
            text-align: leftwards;
        }
        
        table, td, th {
            border: 1px solid black;
        }
        
        #ARTBOX {
            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }
        
        #ARTBOX td, #ARTBOX th {
            border: 1px solid #ddd;
            padding: 8px;
        
        text-align: center;
        
        
        }

        table, th, td {
            border: 1px solid black;text-align: center;
        }
        </style>
        </head>
        <body>
        <h1> AGE DISTRIBUTION</h1> 
        <h2>AGE DISTRIBUTION OF ORDERS</h2>
        
        <table id = "ARTBOX">
          <tr>
            <th>AGE CATEGORY</th>
            <th>COUNT</th>
          </tr>
          <tr>
            <td> less than 1</td>
            <td>"""+listofnumbers[0]+"""</td>
          </tr>
          <tr>
            <td>1+</td>
            <td>"""+listofnumbers[1]+"""</td>
          </tr>
          <tr>
            <td>3+</td>
            <td>"""+listofnumbers[2]+"""</td>
          </tr>
          <tr>
            <td>7+</td>
            <td>"""+listofnumbers[3]+"""</td>
          </tr>
          <tr>
            <td>15+</td>
            <td>"""+listofnumbers[4]+"""</td>
          </tr>
          <tr>
            <td>30+</td>
            <td>"""+listofnumbers[5]+"""</td>
          </tr>
          <tr>
            <td>45+</td>
            <td>"""+listofnumbers[6]+"""</td>
          </tr>
          <tr>
            <td>60+</td>
            <td>"""+listofnumbers[7]+"""</td>
          </tr>
          <tr>
            <td>90+</td>
            <td>"""+listofnumbers[8]+"""</td>
          </tr>
         
        </table>
        
        </body>
        </html>"""
        
        f.write(message)
        f.close()
        
        webbrowser.open_new_tab('Report.html')


def createStatusQuery(order:list) :
    
    return False

#def Backlog()