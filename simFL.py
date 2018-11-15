# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:09:07 2018

@author: prerna.prakash
"""
import datetime 
import pandas as pd
import pycel as py
class simFL :
    def __init__(self) :
        
        dfMain =  pd.read_excel("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL44\\FormattedFLBBDasboard.xlsx")
        dfMain['Fl Commited Date'] = pd.to_datetime(dfMain['Fl Commited Date'],dayfirst=True)
        dfMain['BB Commited Date']  = pd.to_datetime(dfMain['BB Commited Date'],dayfirst=True)
        dfMain['Edge Committed Date'] = pd.to_datetime(dfMain['Edge Committed Date'],dayfirst=True)
        dfMain['SI committed date'] = pd.to_datetime(dfMain['SI committed date'],dayfirst=True)
        cols = ['Order Number','Fl Commited Date','BB Commited Date','Edge Committed Date','SI committed date']
        now = datetime.datetime.now()
        dfMain= dfMain[cols]

        print(now)
        i = 0
        templist = []
        for each in dfMain['Order Number'] :
            if (dfMain.at[i,'Fl Commited Date']-now).days< 0 :
                    templist.append('Backlog')
            elif (dfMain.at[i,'BB Commited Date']-now).days < 0 :
                templist.append('Backlog')   
            elif (dfMain.at[i,'Edge Committed Date']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'SI committed date']-now).days < 0 :
                templist.append('Backlog')
            elif (dfMain.at[i,'Fl Commited Date']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'BB Commited Date']-now).days >= 0 :
                templist.append('Amber')   
            elif (dfMain.at[i,'Edge Committed Date']-now).days >= 0 :
                templist.append('Amber')
            elif (dfMain.at[i,'SI committed date']-now).days >= 0 :
                templist.append('Amber')
            else :
                templist.append('NOCCD')
            i = i+1
            
        dfMain['Date'] = templist
        py.saveExcel("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL303\\FormattedFLBBDasboard1.xlsx",'Sheet1',dfMain)