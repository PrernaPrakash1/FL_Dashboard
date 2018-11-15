# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:23:15 2018

@author: prerna.prakash
"""

import FLModule as fm
import pandas as pd
import pycel as py

df = pd.read_excel("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL28\\FormattedFLBBDasboard1.xlsx")
df =fm.removeDuplicates(df)
py.saveExcelWithIndex("C:\\Users\\prerna.prakash\\Desktop\\Input\\FL28\\tempcheck.xlsx","Sheet1",df)