import pandas as pd
pd.set_option('display.max_colwidth',5)
ufo = pd.read_csv("scrubbed.csv",low_memory=False)
date = ufo["datetime"]
misdate = ufo[ufo["shape"].isna()]

print(misdate)