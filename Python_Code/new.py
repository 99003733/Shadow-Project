import os
import fnmatch 
import pandas as pd
from openpyxl import load_workbook
import openpyxl
from pandas import ExcelWriter

def file_finder():
    treeroot = r"D:\\"
    pattern = '*RateDoc.html'
    results = []                 # an emplty list 
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)                       # fnmatch function to filter the files based on pattern assigned
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

file_found = file_finder()
table_sheet = pd.read_html(file_found[0])

def save_xls(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            df.to_excel(writer,'sheet%s' % n)
        writer.save()



save_xls(table_sheet,"output.xlsx")





# Then the save_xls function works as expected:

# def save_xls(list_dfs, xls_path):
#     with ExcelWriter(xls_path) as writer:
#         for n, df in enumerate(list_dfs):
#             df.to_excel(writer,'sheet%s' % n)
#         writer.save()



# # sheet_names = ['sheet1','sheet2','sheet3','sheet4','sheet5','sheet6','sheet7','sheet8']
# # writer = pd.ExcelWriter('final.xlsx')

