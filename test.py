import pandas as pd
import glob

for f in glob.glob('data/input/*'):
    df = pd.read_excel(f)
df