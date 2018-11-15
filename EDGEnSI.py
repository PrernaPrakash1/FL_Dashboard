# -*- coding: utf-8 -*-
"""
Created on Fri May  4 18:33:52 2018

@author: prerna.prakash
"""

import pandas as pd
import pycel as py
import datetime
import os
import FLModule as fm
import logging
import logging.config


class EDGEnSI :
    def __init__(self):

        pass
                
            

    def findPreviousDate (self) :
        n = 1
        #logging.config.fileConfig('log4p.conf')
        #logger = logging.getLogger('simpleLogger')
        while True:
            
            DateToday = datetime.date.today()
            configFile = fm.SetUpConfigFile('FLConfigFile.txt')
            self.path = configFile[0]
            self.previousdate = datetime.date.today()-datetime.timedelta(n)
            self.month = str(self.previousdate.month)
            self.date = str(self.previousdate.day)
            #logger.debug("previous Date",self.previousdate)
            print(self.path+"\\FL"+self.date+self.month)
            if os.path.isdir(self.path+self.date+self.month) :

                self.previousDatePath = self.path+self.date+self.month

               # logger.debug(self.previousdate)
                return str(self.path+self.date+self.month)
            else :
                n = n +1

        
    def defineAnalysisEDGE(self,dfTriage) :
        previouspath = self.findPreviousDate()
        dfprevious = pd.read_excel(previouspath+"\\FormattedFLBBDasboardFinal.xlsx")
        cols = ['Order Number','Edge password','Edge username','Edge order status','Edge sales order Id']
        
        dfprevious = dfprevious[cols]
        cols = ['Order Number','Edge password_temp','Edge username_temp','Edge order status_temp','Edge sales order Id_temp']
        dfTriage = dfTriage.merge(dfprevious,how='left', on='Order Number')
        dfTriage = dfTriage.drop_duplicates()
   
        
        for index,row in dfTriage.iterrows() :
            if pd.isnull(dfTriage.at[index,'EDGE STATUS_M']) and pd.isnull(dfTriage.at[index,'BB Prod Id']):
                dfTriage.at[index,'EDGE STATUS_M'] = 'No Order Required on Edge'
            elif pd.isnull(dfTriage.at[index,'EDGE STATUS_M']) and pd.isnull(dfTriage.at[index,'BB Prod Id'])==False and dfTriage.at[index,'BB Line Item Status']=='Complete':
                dfTriage.at[index,'EDGE STATUS_M'] = 'Complete from Line Item' 
            if pd.isnull(dfTriage.at[index,'Edge password_x']) and pd.isnull(dfTriage.at[index,'Edge password_y'])==False :
                dfTriage.at[index,'Edge password_x'] = dfTriage.at[index,'Edge password_y'] 
            
            
        return   dfTriage
    
    def defineAnalysisSI(self,dfTriage) :
        previouspath = self.findPreviousDate()
        dfprevious = pd.read_excel(previouspath+"\\FormattedFLBBDasboardFinal.xlsx")
        cols = ['Order Number','Edge password','Edge username','Edge order status','Edge sales order Id']        
        dfprevious = dfprevious[cols]
        cols = ['Order Number','Edge password_temp','Edge username_temp','Edge order status_temp','Edge sales order Id_temp']
        dfTriage = dfTriage.merge(dfprevious,how='left', on='Order Number')
        dfTriage = dfTriage.drop_duplicates()
        for index,row in dfTriage.iterrows() :
            if pd.isnull(dfTriage.at[index,'SI status_M']) and pd.isnull(dfTriage.at[index,'FL Prod Id']):
                dfTriage.at[index,'SI status_M'] = 'No Order Required on SI'
            elif pd.isnull(dfTriage.at[index,'SI status_M']) and pd.isnull(dfTriage.at[index,'FL Prod Id'])==False and dfTriage.at[index,'FL Line Item Status']=='Complete':
                dfTriage.at[index,'SI status_M'] = 'Complete from Line Item'   
            
     
        return   dfTriage
    
    
    


       
    
        
   


