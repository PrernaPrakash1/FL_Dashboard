# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:05:22 2018

@author: prerna.prakash
"""

import pandas as pd
df = pd.read_excel('C:\\Users\\prerna.prakash\\Desktop\\jsonexample.xlsx',dtype=str)
exm = df.to_json()
print(exm)