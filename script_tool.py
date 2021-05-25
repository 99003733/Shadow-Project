from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import pandas as pd
import os

#####################################################
#seacrch for all the bat files present in the D drive or specify the directory u want to search
#################################################
bat_files_path = []                           #list of path where bat files found
bat_files_names = []                          #list of names of bat files
def GetListOfFilesFromFolder():
    for root, dirs, files in os.walk("D:"):
        for file in files:
            if file.endswith(".bat"):
                bat_files_path.append(os.path.join(root, file))
                file = file.replace('.bat' ,'')
                bat_files_names.append(file)

GetListOfFilesFromFolder()


file_names = []                                 #list of file names inside the file name
result_file = []                                # list of result file name inside file name 
for file in bat_files_path:
    with open(file,'r') as f:
        text = f.read()
        words = ["File Name:","Results Criteria/Evaluation:"]
        text2 = text.split("\n")
        for itemIndex in range(len(text2)):
            if words[0] in text2[itemIndex]:
                strip_word = "# File Name:"
                first_word = text2[itemIndex].strip()
                first_word = " ".join(first_word.split())
                first_word = first_word[first_word.startswith(strip_word) and len(strip_word):].strip()
                first_word_update = first_word.replace('.bat' ,'')
                file_names.append(first_word_update)
            if words[1] in text2[itemIndex]:
                rem_word = "# (1)"
                wordlist = text2[itemIndex+1].strip()
                wordlist = " ".join(wordlist.split())
                wordlist = wordlist[wordlist.startswith(rem_word) and len(rem_word):].strip()
                wordlist_update = wordlist.replace('.res','')
                result_file.append(wordlist_update)
                
                
                
#checking for the evaluation as all the names are qual or not

answer = []
status = []
i = 0
for a,b,c in zip(bat_files_names, file_names, result_file):
    if a==b==c:
        answer.append(a)
        print("These files are already OK ",(answer))
        status.append("Proper")    
    else:
        with open(bat_files_path[i]) as f:
            newText=f.read().replace(file_names[i],bat_files_names[i])

        with open(bat_files_path[i], "w") as f:
            f.write(newText)
        status.append("Updated")
    i = i+1
    
    
df = pd.DataFrame({"File Name":bat_files_names,"File Path":bat_files_path, "Status":status})

# creating the excel sheet and saving the data frame into sheet


writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
df.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')