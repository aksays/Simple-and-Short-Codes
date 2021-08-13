# download python and install
# set environment variable for python
# download and install ffmpeg
# pip install youtube-dl
# pip install pandas
# pip install openpyxl

# --------------------------------------

import pandas as pd
import os

file = 'D:\abc.xlsx' # pass your excel file location 

ss = pd.read_excel(file, engine='openpyxl',sheet_name='Sheet1') 


for vid in range(len(ss['Formula'])):
    
    if (ss['status'][0] != 'Downloaded'):
        print(vid)
        os.system('cmd /c '+ ss['Formula'][vid] )  # to execute in command prompt
