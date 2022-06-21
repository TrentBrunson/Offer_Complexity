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
# rename columns
df = df.rename(columns= {'line_of_business_id' : 'LOB_ID',
                        'line_of_business_name' : 'LOB_Name'})
#%%
# list comprehension for entire df
pd.Series({c: df[c].unique() for c in df})
# drop all 'status codes' and 'current version flag'
#%%
# put all unique values in list of lists for viewing/manipulation
unique_list_of_lists = [df[i].unique().tolist() for i in df.columns]
# %%
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
# %%
