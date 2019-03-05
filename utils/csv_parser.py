import pandas as pd
import seaborn as sns  # visualization tool
import matplotlib.pyplot as plt
import pymongo
df = pd.read_csv("../../FlightAware_IAI_2015-04-01_2015-06-30_tracks.csv", low_memory=False)

print(df.head().to_csv("head.csv",index=False))

from data_access_layer.mongodb_connection import put_df
put_df(df)
# TypeError: document must be an instance of dict, bson.son.SON, bson.raw_bson.RawBSONDocument, or a type that inherits from collections.MutableMapping



print(df.info())

print(df.corr())

f, ax = plt.subplots(figsize=(50, 50))
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.show()

print(df.describe())

