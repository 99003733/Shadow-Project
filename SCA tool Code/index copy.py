
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as pd
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
import webbrowser
import os
import warnings
warnings.filterwarnings("ignore")

excel_files = []
# excel_files = ["E:\GCU_SCA_A_D_CONSOLIDATED_REPORT_BP3.0.xlsm","E:\GCU_SCA_E_I_CONSOLIDATED_REPORT_BP3.0.xlsm","E:\GCU_SCA_L_P_CONSOLIDATED_REPORT_BP3.0.xlsm","E:\GCU_SCA_R_X_CONSOLIDATED_REPORT_BP3.0.xlsm"]
for i in range(4):
  inp = input("Enter the Excel sheet path: ")
  excel_files.append(inp)

def open_excel(excel_files):
    df_dict = {}
    i = 1
    for f in excel_files:
        df = pd.read_excel(f, sheet_name='Summary', index_col=None)
        df1 = df.loc[0:3]
        df1.set_index('Unnamed: 0', inplace=True)
        # df1.dropna(inplace=True)
        df_dict[i] = df1
        i = i + 1
    return df_dict


def open_excel_dataframe(df_dict):
    new_df = pd.DataFrame(index=df_dict[1].index, columns=['Total Nodes', 'Hit'])
    new_df.fillna(0, inplace=True)
    for i in range(1,5):
        #df_dict[i].set_index('Unnamed: 0', inplace=True)
        new_df["Total Nodes"] += df_dict[i]['Total Nodes']
        new_df["Hit"] += df_dict[i]['Hit']
    return new_df

def plot_graph(new_df, imagename):
    new_df.plot(kind="bar")
    # plt.bar(x = "Unnamed :0",y="")
    plt.title("Summary sheet")
    plt.xlabel("Blocks")
    plt.ylabel("Values")
    plt.savefig(imagename + ".png", dpi=300, bbox_inches='tight')


def second_excel(excel_files):
    newdf_dict = {}
    i = 1
    for f in excel_files:
        df = pd.read_excel(f, sheet_name='Summary', index_col=None)
        df1 = df.loc[9:14]
        df1.set_index('Unnamed: 0', inplace=True)
        df1.drop(columns='Total Nodes', inplace=True)
        newdf_dict[i] = df1
        i = i + 1
    return newdf_dict


def percent_graph(new_df, imagename):
    new_df['Percentage'] = (new_df['Hit'] / new_df['Total Nodes']) * 100
    # df1.set_index('Unnamed: 0')
    new_df.plot(y='Percentage', kind="bar")
    plt.title("Summary sheet")
    plt.xlabel("Blocks")
    plt.ylabel("Values")
    plt.savefig(imagename + "p.png", dpi=300, bbox_inches='tight')
    


def second_dataframe(newdf_dict):
    new_dataframe = pd.DataFrame(index=newdf_dict[1].index, columns=['Hit'])
    new_dataframe.fillna(0, inplace=True)
    for i in range(1,5):
        new_dataframe["Hit"] += newdf_dict[i]['Hit']
    return new_dataframe


def second_graph(new_dataframe, imagename):
    new_dataframe.plot(kind="bar")
    plt.title("Summary sheet")
    plt.xlabel("Blocks")
    plt.ylabel("Values")
    plt.savefig(imagename + "s.png", dpi=300, bbox_inches='tight')


df_dict = open_excel(excel_files)
df = open_excel_dataframe(df_dict)
plot_graph(df,"file1")


newdf_dict = second_excel(excel_files)
df2 = second_dataframe(newdf_dict)
second_graph(df2, "second")


secdf_dict = open_excel(excel_files)
new_df = open_excel_dataframe(secdf_dict)
percent_graph(new_df, 'file1')


# to open/create a new html file in the write mode
f = open('beauty.html', 'w')

# the html code which will go in the file GFG.html
html_template = """
<!DOCTYPE html>
<html>
<head>
<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 33.33%;
  padding: 10px;
}

/* Clearfix (clear floats) */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
</head>
<body>

<div class="row">
  <div class="column">
    <img src="file1.png" alt="Total Nodes and Hit" style="width:100%">
  </div>
  <div class="column">
    <img src="seconds.png" alt="Hit Only" style="width:100%">
  </div>
  <div class="column">
    <img src="file1p.png" alt="Percentage" style="width:100%">
  </div>
</div>

</body>
</html>
"""
# writing the code into the file
f.write(html_template)

# close the file
f.close()

# 1st method how to open html files in chrome using
filename = 'file:///'+os.getcwd()+'/' + 'beauty.html'
webbrowser.open_new_tab(filename)




