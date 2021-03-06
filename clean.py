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
# amer_unique = [df_amer[i].unique().tolist() for i in df_amer.columns]
# amer_unique
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
df_emeapj = pd.concat([df_apj, df_emea])
df_emeapj.shape
# right number of rows
# next reshape rows & columns
# %%
# reduce number of rows to work with - drop repeated catalog info

# %%
df_amer.count()
# ''' some nulls in two columns
# item_unit_price          1764257
# business_segment_code    1767701
# '''
# %%
# amer_values = df_amer.value_counts()
# amer_values
# %%
df_apj.count()
# ''' some nulls in 
# price                      81486
# '''
# %%
df_emea.count()
# some nulls in two columns
# item_unit_cost           1210432
# price                     560775
# %%
df_amer.isna().sum()
# %%
df_amer.isna().sum().sum()
# %%
df_apj.isna().sum()
# %%
df_apj.isna().sum().sum()
# %%
df_emea.isna().sum()
# %%
df_emea.isna().sum().sum()
# %%
'''no other hidden nulls in rows'''
# %%
