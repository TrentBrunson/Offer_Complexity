#%%
'''emulate notebooks for code testing'''
#%%
# import dependencies
# from glob import glob
from enum import unique
import os
import glob
import numpy as np
import pandas as pd
# from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
#%%
df = pd.read_csv('data\DOM_NBK_DATA_AMER_202206102000.csv')
# %%
df
# %%
df.shape
# %%
df.columns
# %%
# df = df.drop('id', axis=1)
# not needed
# %%
df.describe()
# %%
# rename columns
df = df.rename(columns= {'line_of_business_id' : 'LOB_ID',
                        'line_of_business_name' : 'LOB_Name'})
# %%
# check for duplicated records
dupes = df.duplicated()
dupes
# %%
sum(dupes)
# non dupes found in US data set
# %%
df.isnull().sum()
# 0 nulls found
# %%
df.isna().sum()
# isnull references this; isna
# no need for dropna
# %%
pd.isnull
#%%
df.chassis_id.unique()
#%%
df.chassis_id.unique().sum()
#%%
# list comprehension for entire df
pd.Series({c: df[c].unique() for c in df})
# drop all 'status codes' and 'current version flag'
#%%
# put all unique values in list of lists for viewing/manipulation
unique_list_of_lists = [df[i].unique().tolist() for i in df.columns]
# %%
# cleaned data output
df.to_csv('data/US_data_cleaned.csv', index=False, mode='x')
# add code to check for output dir and make dir if not present 
# overwrite if needed

filename = 'data/US_data_cleaned.csv'

# search for any files which matching filename
files_present = glob.glob(filename)

# if no matching files, write to csv, if there are matching files, print statement
if not files_present:
    pd.to_csv(filename)
else:
    print('WARNING: This file already exists!')
# %%
numeric_df = df.drop([
                        'LOB_Name'
])
# %%
# for numeric only list of values using numpy
unique_vals = np.unique(np.array(numeric_df))
unique_value_list = list(np.unique(np/pd.array(df)))