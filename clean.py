'''read in files, clean and join'''
#%%
import os
import pandas as pd

# %%
df_amer = pd.read_csv('data\input\\NBK_US-CA-MX_WITH_CATALOGUE_20220622.csv')
df_apj = pd.read_csv('data\input\\NBK_APAC_WITH_CATALOG_20220622.csv')
df_emea = pd.read_csv('data\input\\NBK_UK-DE-FR_WITH_CATALOG_20220622.csv')
#%%
df_amer
# %%
df_apj
# %%
df_emea
# %%
df_amer.columns
# %%
df_apj.columns
# %%
df_emea.columns
#%%
amer_unique = [df_amer[i].unique().tolist() for i in df_amer.columns]
amer_unique
# missing column header label
#%%
amer_unique = pd.Series({c: df_amer[c].unique() for c in df_amer})
amer_unique
# all region codes correctly labeled as AMER
#%%
apj_unique = pd.Series({c: df_apj[c].unique() for c in df_apj})
apj_unique
# all region codes correctly labeled as EMEA
#%%
emea_unique = pd.Series({c: df_emea[c].unique() for c in df_emea})
emea_unique
# all region codes correctly labeled as EMEA
# %%
# join data sets and set like columns same

# first merge emea and apj - most alike
