from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as pd
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

import os
import warnings


excel_files = [r'GCU_SCA_A_D_CONSOLIDATED_REPORT_BP3.0.xlsm']
def open_excel(excel_files):
    df_dict = {}
    i = 1
    for f in excel_files:
        df = pd.read_excel(f, sheet_name='Summary', index_col=None)
        df1 = df.loc[0:4]
        # df1.dropna(inplace=True)
        df_dict[i] = df1
        i = i + 1
    return df_dict


def open_excel_dataframe(df_dict):
    new_df = pd.DataFrame(index=df_dict[1]['Unnamed: 0'], columns=['Total Nodes', 'Hit'])
    new_df.fillna(0, inplace=True)
    for i in range(1, 5):
        # df_dict[i].set_index('Unnamed: 0', inplace=True)
        new_df["Total Nodes"] += df_dict[i]['Total Nodes']
        new_df["Hit"] += df_dict[i]['Hit']
    return new_df




    # ax = new_df[['Total Nodes', 'Hit']].plot(kind='bar', title="V comp", figsize=(15, 10), legend=True, fontsize=12)
    # ax.set_xlabel("Hour", fontsize=12)
    # ax.set_ylabel("V", fontsize=12)
    # plt.show()

df_dict = open_excel(excel_files)
new_df = open_excel_dataframe(df_dict)

print(new_df)
# ax = df[['Total','V2']].plot(kind='bar', title ="V comp", figsize=(15, 10), legend=True, fontsize=12)
# ax.set_xlabel("Hour", fontsize=12)
# ax.set_ylabel("V", fontsize=12)
# plt.show()