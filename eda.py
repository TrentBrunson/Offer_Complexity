#%%
'''emulate notebooks for code testing'''
#%%
# import dependencies
# from glob import glob
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
# %%
# cleaned data output
df.to_csv('data/US_data_cleaned.csv', index=False, mode='x')
# add code to check for output dir and make dir if not present 
# overwrite if needed
# %%
