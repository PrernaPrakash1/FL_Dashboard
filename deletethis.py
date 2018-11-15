# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:10:39 2018

@author: prerna.prakash
"""

import pandas as pd
import Tracker as tk
import pycel as py 

df = pd.read_excel('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL228\\FormattedFLBBDasboard.xlsx')
Tracker = tk.Tracker()

df = Tracker.Apply(df)

py.saveExcel('C:\\Users\\prerna.prakash\\Desktop\\Input\\FL218\\FormattedFLBBDasboarddd.xlsx','Sheet1',df)