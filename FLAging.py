# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:28:32 2018

@author: prerna.prakash
"""

import pandas as pd
import pycel as py
import datetime 

class FLAging :
    def __init__(self,dfMain):
        self.dfMain = dfMain
        self.DateToday = datetime.date.today()
        self.month = str(self.DateToday.month) 
        self.day = str(self.DateToday.day)
        self.DefaultPath = "C:\\Users\\prerna.prakash\\Desktop\\Input\\FL"+self.day+self.month+"\\"  
        print("hello")
        #self.listOfConfigFile = py.setUpConfigFile("ConfigForARTY.txt")
        self.dfMain['Fl Commited Date'] = pd.to_datetime(self.dfMain['Fl Commited Date'],dayfirst=True)
        self.dfMain['BB Commited Date']  = pd.to_datetime(self.dfMain['BB Commited Date'],dayfirst=True)
        self.dfMain['Edge Committed Date'] = pd.to_datetime(self.dfMain['Edge Committed Date'],dayfirst=True)
        self.dfMain['SI committed date'] = pd.to_datetime(self.dfMain['SI committed date'],dayfirst=True)
        self.dfMain['edge committed date_M'] = pd.to_datetime(self.dfMain['edge committed date_M'],dayfirst=True)
        self.dfMain['SI Committed date_M'] = pd.to_datetime(self.dfMain['SI Committed date_M'],dayfirst=True)
        self.dfMain['Order Submit Date'] = pd.to_datetime(self.dfMain['Order Submit Date'],dayfirst=True)
        self.AssignDate()

   
    def AssignDate(self) :
        

        for index,row in self.dfMain.iterrows() :
            
            self.dfMain['tempDate'] = self.dfMain[['Fl Commited Date','BB Commited Date','Edge Committed Date','SI committed date','edge committed date_M','SI Committed date_M']].max(axis=1)
        self.FindAgeCCD()
        return   self.dfMain


    def FindAgeCCD(self) :
        i = 0
        for  each in self.dfMain['Order Number'] :
            self.dfMain.at[i,'AgeCCD'] = (datetime.datetime.now() -self.dfMain.at[i,'tempDate']).days
            self.dfMain.at[i,'AgeCCDCategory'] = self.AssignAgeCategory(self.dfMain.at[i,'AgeCCD'] )
            i = i+1
        self.FindAgeSubmitDate()
    
    def FindAgeSubmitDate(self) :
        i = 0
        for  each in self.dfMain['Order Number'] :
            self.dfMain.at[i,'AgeSubmitDate'] = (datetime.datetime.now() -self.dfMain.at[i,'Order Submit Date']).days
            self.dfMain.at[i,'AgeSubmitDateCategory'] = self.AssignAgeCategory(self.dfMain.at[i,'AgeSubmitDate'] )
            i = i+1
        cols = ['Order Number','Fl Commited Date','BB Commited Date','Edge Committed Date','SI committed date','edge committed date_M','SI Committed date_M','tempDate','AgeCCDCategory','AgeSubmitDate','AgeCCD','AgeSubmitDateCategory','Order Submit Date']
        py.saveExcel(self.DefaultPath+"FormattedFLBBDasboard1.xlsx","Sheet1",self.dfMain)
        self.dfMain = self.dfMain[cols]  
        py.saveExcel(self.DefaultPath+"FormattedFLBBDasboardcheckAge.xlsx","Sheet1",self.dfMain)
            
    
    def AssignAgeCategory(self,days) :
        if days >90 :
            return '90+'
        elif days >= 60 :
            return '60+'
        elif days >=45 :
            return '45+'
        elif days >=30 :
            return '30+'
        elif days >= 15 :
            return '15+'
        elif days >= 7 :
            return '7+'
        elif days >=3 :
            return '3+'
        elif days >=1 :
            return '1+'
        else :
            return 'less than 1'
        
        
        
        