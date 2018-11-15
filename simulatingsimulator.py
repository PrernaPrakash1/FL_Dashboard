# -*- coding: utf-8 -*-
"""
Created on Mon May  7 19:07:30 2018

@author: prerna.prakash
"""

import pycel as py
import pandas as pd
import FLModule as FM
import FLnoCCD as CCD
import time
import CancellationAnalysis as ca
strtime = time.time()
df = pd.read_excel("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL3010\\FormattedFLBBDasboardFinal.xlsx")
#cols = ['Order Number','Fl Commited Date','BB Commited Date','edge committed date_M','SI Committed date_M']
#df = df[cols]
#templist = FM.category(df)
#df['category'] = templist
cancellationAnalysis = ca.cancellationAnalysis(df)
df = cancellationAnalysis.analysis()

py.saveExcel("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL3010\\FormattedFLBBDasboardcheck1.xlsx","Sheet1",df)
endtime = time.time()
print('time taken is', endtime-strtime)