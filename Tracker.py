# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:18:52 2018

@author: prerna.prakash
"""


import pandas as pd
import datetime
import FLModule as fm

class Tracker :
    def __init__(self) :
        
        self.DefaultPath = fm.getDefaultPath()
 
 
    def Cancellation(self,dfMain) :
        cols = ['a','a','a','a','a','Order Num','a','a','a','a','a','a','a','a']
        dfCancellation = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="Cancel recreate",header= None, names = cols)
        canList = dfCancellation['Order Num'].tolist()
        return canList
    
    def ML(self,dfMain) :
        cols = ['a','a','a','a','a','a','Order Num','a','a','a','a','a','a','a','a','a']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="ML",header= None, names = cols)
        mlList = MLList['Order Num'].tolist()
        return mlList 
    
    def Adhoc(self,dfMain) :
        cols = ['a','a','a','a','a','Order Num','a','a','a','a','a','a','a','a','a','a']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="Adhoc",header= None, names = cols)
        mlList = MLList['Order Num'].tolist()
        return mlList 
    
    def Renumber(self,dfMain) :
        cols = ['a','a','a','a','a','Order Num','a','a','a','a','a','a','a','a','a','a','a','s']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="Renumber",header= None, names = cols)
        mlList = MLList['Order Num'].tolist()
        return mlList 
    
    def Spoof(self,dfMain) :
        cols = ['a','a','a','a','Order Num','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="Spoof",header= None, names = cols)
        mlList = MLList['Order Num'].tolist()
        return mlList 


    def DaSpoof(self,dfMain) :
        cols = ['a','a','a','a','a','a','Order Num','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="Daspoof",header= None, names = cols)
        mlList = MLList['Order Num'].tolist()
        return mlList 
    
    def P2C(self,dfMain) :
        cols = ['a','a','a','a','a','Order Num','a','a','a','a','a','a','a','a','a','a']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="P2C",header= None, names = cols)
        mlList = MLList['Order Num'].tolist()
        return mlList 
    
    def A2G(self,dfMain) :
        cols = ['a','ab','ac','ad','ae','af','Order Number','A2G1','A2G3','ag','A2G2','ag','d','g','a','a']
        MLList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="A2G",header= None, names = cols)
        cols = ['Order Number','A2G1','A2G3','A2G2']
        MLList = MLList[cols]
        MLList = MLList.drop_duplicates(subset = ['Order Number'])
        dfMain = dfMain.merge(MLList,how='left', on='Order Number')
        return dfMain
    
    def Router(self,dfMain) :
        cols = ['a','ab','Order Number','Router','ad','ae','af']
        MList = pd.read_excel(self.DefaultPath+"Tracker.xlsx",sheet_name ="Router",header= None, names = cols)
        cols = ['Order Number','Router']
        MList = MList[cols]
        MList = MList.drop_duplicates(subset = ['Order Number'])
        dfMain = dfMain.merge(MList,how='left', on='Order Number')
        return dfMain
        
    def Apply(self,dfMain) :
       canList = self.Cancellation(dfMain)
       ml = self.ML(dfMain)
       adhoc = self.Adhoc(dfMain)
       renumber = self.Renumber(dfMain)
       spoof = self.Spoof(dfMain)
       DaSpoof = self.DaSpoof(dfMain)
       P2C = self.P2C(dfMain)
       for index,row in dfMain.iterrows() :
            if dfMain.at[index,'Order Number'] in canList:
                 print('can')
                 dfMain.at[index,'Track'] = 'Cancellation' 
            if dfMain.at[index,'Order Number'] in ml :
                 print('ml')
                 dfMain.at[index,'Track'] = 'ML'
            if dfMain.at[index,'Order Number'] in adhoc :
                 print('ad')
                 dfMain.at[index,'Track'] = 'ADHOC'
            if dfMain.at[index,'Order Number'] in renumber :
                 print('re')
                 dfMain.at[index,'Track'] = 'Renumber'
            if dfMain.at[index,'Order Number'] in spoof :
                 print('spo')
                 dfMain.at[index,'Track'] = 'Spoof'
            if dfMain.at[index,'Order Number'] in DaSpoof :
                 print('das')
                 dfMain.at[index,'Track'] = 'DaSpoof'
            if dfMain.at[index,'Order Number'] in P2C :
                 dfMain.at[index,'Track'] = str('P2C')
                 
       dfMain = self.A2G(dfMain)
       #dfMain = self.Router(dfMain)
       return dfMain
