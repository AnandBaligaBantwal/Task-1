import pandas as pd
import numpy as np

original_df = pd.read_csv(
    "C:\\Users\\abali\\Downloads\\marketing_campaign.csv", sep="\t"
)

Original_df = pd.DataFrame(original_df)  # Original_df is the original DataFrame

df = pd.DataFrame(original_df)  # df is the DataFrame we will be working with

df.head()

# Handling Missing Values
df.isnull().sum()
income_median = df["Income"].median()
df["Income"] = df["Income"].fillna(income_median)

# Dropping Duplicates
df.drop_duplicates()

# Column Renaming
updated_df.columns = updated_df.columns.str.lower().str.replace(" ", "_")

updated_df
