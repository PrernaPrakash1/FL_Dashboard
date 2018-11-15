# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:43:31 2018

@author: prerna.prakash
"""

import os
import pandas as pd
import pycel as py
import FLModule as fm
import datetime
class Carisma() :
    def __init__(self):
     self.DefaultPath = fm.getDefaultPath()  
        
     if os.path.exists(self.DefaultPath+"Carisma.xlsx") == 'False' :
         return False
     else :
         dfCar = pd.read_excel(self.DefaultPath+"Carisma.xlsx")         
         self.cols = ['Order Number','Router Service ID']
         self.newpath = self.findPreviousDate()         
         dfCar = dfCar[self.cols]
         dfCar = self.addPrevious(dfCar)
                  
         dfCar = dfCar.drop_duplicates(["Order Number"], keep='first',).reset_index(drop=True)         
         dfCar.rename(columns={'Router Service ID':'Router Service ID from Carisma'})         
         py.saveExcel(self.DefaultPath+"CarismaFormatted.xlsx",'Sheet1',dfCar)


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
                
    def addPrevious(self,dfcar) :
        cols = ['Order Number','Router Service ID from Carisma']
        dfPrevious = pd.read_excel(self.newpath+"\\FormattedFLBBDasboardFinal.xlsx")
        dfPrevious = dfPrevious[cols]
        dfPrevious= dfPrevious.rename(columns={'Router Service ID  from Carisma':'Router Service ID'})         
        dfcar = dfcar.append(dfPrevious)
        return dfcar
        
        