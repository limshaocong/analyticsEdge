# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 18:07:12 2021

@author: shaoc
"""

import pandas as pd
import re

import os
from os import listdir, chdir
from os.path import isfile, join

os.chdir("/Users/shaoc/OneDrive - Massachusetts Institute of Technology/Twitter/Cleaned") # update path accordingly

mypath = "/Users/shaoc/OneDrive - Massachusetts Institute of Technology/Twitter" # update path accordingly

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
suffix = "2020.csv"

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


for file in onlyfiles:
    
    if str.endswith(file, suffix):
    
        filepath = mypath + str("/") + file
        df = pd.read_csv(filepath)

        df["Datetime"] = pd.to_datetime(df["Datetime"])
        
        df["Date"] = df["Datetime"].dt.date
        
        raw_texts = df.iloc[:,2].tolist()
        
        for idx in range(len(raw_texts)):
          raw_text = raw_texts[idx]
          raw_text = re.sub(r"[http]\S+", "", raw_text) # remove urls
          raw_text = re.sub(r"[$][A-Za-z][\S]*", "", raw_text) # remove $tickers
          raw_text = re.sub(r"[\n]", "", raw_text) # remove new line (\n)
          raw_text = deEmojify(raw_text) # remove emoji
          raw_texts[idx] = raw_text
        
        df["Text_clean"] = raw_texts # save data in new column
        df['Delete'] = list(map(lambda x: x.isspace(), df['Text_clean'])) # tag all rows with only white space left
        df = df.loc[df['Delete'] == False] # delete all tagged rows
        df = df.reset_index(drop = True)
        
        texts = df["Text_clean"]
        
        df = df.iloc[:, [4, 5]]
                      
        newfilename = file[:-4] + str("_cleaned.csv")
        
        df.to_csv(newfilename, index = False)
        
    else:
        
        continue

