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
df.value_counts().sum() # value counts looked all unique...verifying...true
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
# no dupes found in US data set
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
'''
visualize
'''

fig, ax = plt.subplots(figsize=(10,8))
sns.boxplot(df_excluded['LOB_ID'],
                        orient='v'
                        )
# %%
# do all features in one plot
fig, ax = plt.subplots(figsize=(10,8))
bp = sns.boxplot(data = df_excluded)
bp.set_xticklabels(bp.get_xticklabels(), rotation=75)
# %%
# scale data for easier comparison 
# orders of magnitude difference making uninterpreteable
# get Z-scores
# first zero mean and unit variance
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_array = scaler.fit_transform(df_excluded)
# %%
scaled_data = pd.DataFrame(scaled_array, columns=df_excluded.columns)
scaled_data
# %%
scaled_data.describe()
# %%
# visaulize scaled data features in one plot
fig, ax = plt.subplots(figsize=(10,8))
bp_scaled = sns.boxplot(data = scaled_data)
bp_scaled.set_xticklabels(bp_scaled.get_xticklabels(), rotation=75)
# %%
# interquartile ranges
Q1 = df_excluded.quantile(0.25)
Q3 = df_excluded.quantile(0.75)

IQR = Q3 - Q1

print(IQR)
# %%
# remove potential outliers technique based on IQR
# compute D-values not necessary - most of this is categorical data, even though numeric
outliers_removed_df = df_excluded[~ ((df_excluded < (Q1 - 1.5*IQR)) \
                                | (df_excluded > (Q3 + 1.5*IQR))).any(axis=1)]
outliers_removed_df.shape
# 29% may have no value (27,163)
# this df kept only 66,721 of 93,884
# %%
# do all features in one plot
fig, ax = plt.subplots(figsize=(10,8))
bp_outliers_removed = sns.boxplot(data = outliers_removed_df)
bp.set_xticklabels(bp_outliers_removed.get_xticklabels(), rotation=75)
# %%
