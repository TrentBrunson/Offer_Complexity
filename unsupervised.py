'''
data already processed in eda - no nulls, values are tolerable 
for unsupervised ML though not always reasonable with place holders 
still in there for some active items
'''
#%%
import pandas as pd
import glob
import os
#%%
df = pd.read_csv('data\input\\NBK_US-CA-MX_WITH_CATALOGUE_20220622.csv')
df
# %%
for f in glob.glob('data\input\*.csv'):
    df = pd.read_csv(f, lineterminator='\n')
df
# %%
# exclude subdirectories in input folder
# df = [f for f in glob('data\input\*') if not os.path.isdir(f)]
# %%
df
# %%
