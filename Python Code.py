import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\abali\\Downloads\\marketing_campaign.csv", sep="\t")

df = pd.DataFrame(df)

df.head()

df.drop_duplicates()

df.isnull().sum()

income_median = df["Income"].median()

updated_df = df["Income"].fillna(income_median)

updated_df.isnull().sum()
