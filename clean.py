'''read in files, clean and join'''
#%%
import os
import pandas as pd

# %%
df_amer = pd.read_csv('data\input\\NBK_US-CA-MX_WITH_CATALOGUE_20220622.csv')
df_apj = pd.read_csv('data\input\\NBK_APAC_WITH_CATALOG_20220622.csv')
df_emea = pd.read_csv('data\input\\NBK_UK-DE-FR_WITH_CATALOG_20220622.csv')
# %%
df_amer.columns
# %%
df_apj.columns
# %%
df_emea.columns
# %%
df_apj
# %%
df_apj.describe()
# %%
