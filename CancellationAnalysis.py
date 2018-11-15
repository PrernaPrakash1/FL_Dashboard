# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:47:48 2018

@author: prerna.prakash
"""
import FLModule as fm
import pycel as py
import pandas as pd

class cancellationAnalysis :
    def __init__(self,dfTriage) :
        self.DefaultPath = fm.getDefaultPath()
        self.dfTriage = dfTriage
        self.Analysis = pd.read_excel("C:\\Users\\prerna.prakash\\Desktop\\FL\\Input\\FL_Triage.xlsx")

    def SIRejected(self) :
        print(len(self.dfTriage.index))
        dftemp = self.dfTriage[self.dfTriage['SI status_M']=='REJECTED']
        print(len(dftemp.index))
        self.dfTriage = py.vlookupine(dftemp,self.Analysis,'SR DESC','SR Desc',['Next Action','Recreation Comment','Cancellation Reason','SIM2','Add in Ad-Hoc','Comments'])
        return self.dfTriage
        
    def analysis(self) :
        for index,row in self.dfTriage.iterrows() :
            for sindex,rows in self.Analysis.iterrows() :
                  if py.mathching(self.dfTriage.at[index,'SI status_M'],self.Analysis.at[sindex,'SI Status']) :
                   if py.mathching(self.dfTriage.at[index,'SR DESC'],self.Analysis.at[sindex,'SR Desc']) :
                    if py.mathching(self.dfTriage.at[index,'BB Prod Id'],self.Analysis.at[sindex,'BB Prod Id']) :
                      if py.mathching(self.dfTriage.at[index,'Router Prod Id'],self.Analysis.at[sindex,'Router Prod ID']) :
                        if py.mathching(self.dfTriage.at[index,'EDGE STATUS_M'],self.Analysis.at[sindex,'Edge Status'])  :
                         if py.mathching(self.dfTriage.at[index,'Shipping Flag'],self.Analysis.at[sindex,'Shipping']) :
                           if py.mathching(self.dfTriage.at[index,'Track'],self.Analysis.at[sindex,'Tracker']) :  
                            if py.mathching(self.dfTriage.at[index,'OrderType Code'],self.Analysis.at[sindex,'OrderType Code']) :                                     
                               
                                self.dfTriage.at[index,'Next Action'] = str(self.Analysis.at[sindex,'Next Action'])
                                self.dfTriage.at[index,'Recreation Comment'] = str(self.Analysis.at[sindex,'Recreation Comment'])
                                self.dfTriage.at[index,'Cancellation Reason'] = str(self.Analysis.at[sindex,'Cancellation Reason'])
                                self.dfTriage.at[index,'SIM2'] = str(self.Analysis.at[sindex,'SIM2'])
                                self.dfTriage.at[index,'Add in Ad-Hoc'] = str(self.Analysis.at[sindex,'Add in Ad-Hoc'])
                                self.dfTriage.at[index,'Comments'] = str(self.Analysis.at[sindex,'Comments'])
                                               #self.Billing.at[i,'NEXT ACTION'] = str(dfTriage.at[j,'Comments'])
                                break  
     
        return   self.dfTriage