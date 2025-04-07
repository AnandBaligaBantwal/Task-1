import pandas as pd

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


# Data Type Conversion
df["Dt_Customer"] = df["Dt_Customer"].astype("datetime64[ns]")
df["Year_Birth"] = df["Year_Birth"].astype("datetime64[ns]").dt.year
df.info()

# Column Renaming and Reordering

new_column_names = {
    "ID": "Customer_ID",
    "Year_Birth": "Year_Of_Birth",
    "Education": "Education_Level",
    "Marital_Status": "Marital_status",
    "Income": "Income",
    "Kidhome": "Kids_At_Home",
    "Teenhome": "Teens_At_Home",
    "Dt_Customer": "Customer_Since",
    "Recency": "Recency",
    "MntWines": "Monthly_Wine",
    "MntFruits": "Monthly_Fruit",
    "MntMeatProducts": "Monthly_Meat_products",
    "MntFishProducts": "Monthly_Fish_products",
    "MntSweetProducts": "Monthly_Sweets_products",
    "MntGoldProds": "Monthly_Gold_products",
    "NumDealsPurchases": "Deal_Purchases",
    "NumWebPurchases": "Web_Purchases",
    "NumCatalogPurchases": "Catalog_Purchases",
    "NumStorePurchases": "Store_Purchases",
    "NumWebVisitsMonth": "Web_Visits_per_Month",
    "AcceptedCmp1": "Accepted_Cmp1",
    "AcceptedCmp2": "Accepted_Cmp2",
    "AcceptedCmp3": "Accepted_Cmp3",
    "AcceptedCmp4": "Accepted_Cmp4",
    "AcceptedCmp5": "Accepted_Cmp5",
    "Complain": "Complained",
    "Z_CostContact": "Z_CostContact",
    "Z_Revenue": "Z_Revenue",
    "Response": "Response",
}


df.rename(columns=new_column_names, inplace=True)
df.columns = df.columns.str.lower()

# Reordering Columns
new_column_order = [
    "customer_id",
    "year_of_birth",
    "education_level",
    "marital_status",
    "income",
    "kids_at_home",
    "teens_at_home",
    "customer_since",
    "recency",
    "monthly_wine",
    "monthly_fruit",
    "monthly_meat_products",
    "monthly_fish_products",
    "monthly_sweets_products",
    "monthly_gold_products",
    "deal_purchases",
    "web_purchases",
    "catalog_purchases",
    "store_purchases",
    "web_visits_per_month",
    "accepted_cmp1",
    "accepted_cmp2",
    "accepted_cmp3",
    "accepted_cmp4",
    "accepted_cmp5",
    "complained",
    "z_costcontact",
    "z_revenue",
    "response",
]


df = df[new_column_order]

df
