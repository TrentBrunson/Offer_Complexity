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
