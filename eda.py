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

'''
real input code...
#%%
# read input file from directory - name changes week to week
for f in glob.glob('data/input/*'):
    df = pd.read_excel(f)
df
# %%
df.info
# %%
df.describe()
# %%
df.value_counts()
# %%
df.count()
'''
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
df.info
# %%
df.describe()
# %%
df.value_counts()
# %%
df.count()
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
# quick look at numeric values only
# add numeric shorter than dropping all obj/str
numeric_df = df[[
                        'LOB_ID',
                        'chassis_id',
                        'module_id',
                        'item_unit_cost',
                        'item_unit_price'
]]
numeric_df
#%%
# check for numeric data types only
numeric_df.dtypes

# OK - int and float only
#%%
unique_vals = np.unique(np.array(numeric_df))
# unique_value_list = list(np.unique(np.array(df)))
#%%
"""
# alternate way to get columns of numeric dataonly
"""
df.dtypes
#%%
df_excluded = df.select_dtypes(exclude=object)
df_excluded
# %%
# for numeric only list of values using numpy
unique_vals = np.unique(np.array(df_excluded))
# %%
unique_vals
# %%
unique_value_list = list(np.unique(np.array(df_excluded)))
unique_value_list
# %%
