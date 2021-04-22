import os
import fnmatch 
import pandas as pd
from openpyxl import load_workbook
import openpyxl

#######################################################
# Function to find out the RateDoc Files present in the Directory
#######################################################
def multiple_dfs(df_list, sheets,spaces):
    # writer = pd.ExcelWriter(file_name,engine='xlsxwriter')   
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0)   
        row = row + len(dataframe.index) + spaces + 1
    # writer.save()

def file_finder():
    treeroot = r"D:\\"
    pattern = '*RateDoc.html'
    results = []                 # an emplty list 
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)                       # fnmatch function to filter the files based on pattern assigned
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

file_found = file_finder()
sheets = ['df1','df2','df3','df4','df5','df6','df7','df8'] 
j=0
writer = pd.ExcelWriter('test2.xlsx',engine='xlsxwriter') 
for f in file_found:
    table_sheet = pd.read_html(f)
    multiple_dfs(table_sheet, sheets[j], 1)
    j = j+1


writer.save()



