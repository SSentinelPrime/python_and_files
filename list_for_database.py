# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:28:05 2019

@author: Ahmets Project
"""

from os import listdir
import pandas as pd

directory = input("Path to directory: ")
files_dir =  listdir(directory)
newlist = []
for names in files_dir:
    if names.endswith(".xlsx"):
        newlist.append(names)
print(newlist)

df1 = pd.read_excel('denemeler-1.xlsx')
for i in newlist:
    df2 = pd.read_excel('%s' %i)
    results = df1.merge(df2, on='Koma53')
    sort_by_time = results.sort_values('Sira')
    pd.DataFrame(sort_by_time).to_excel('new' + '%s' %i )