import pandas as pd

pd.set_option('display.max_colwidth',5)
ufo = pd.read_csv("scrubbed.csv",low_memory=False)

noshape = ufo.loc[ufo["shape"].isna()]

for i in noshape.index:
    print(i)
    ufo.loc[i]["shape"] = "unknown"
    print(ufo.loc[i]["shape"])

#print(noshape["shape"])