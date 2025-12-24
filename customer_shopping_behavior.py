import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "customer_shopping_behavior.csv")

df = pd.read_csv(csv_path)
print(df.head())

print("BEFORE CLEANING")
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Fill null value using median
df['Review Rating'] = df.groupby('Category')['Review Rating'] \
    .transform(lambda x: x.fillna(x.median()))
df['Review Rating'].fillna(df['Review Rating'].median(), inplace=True)

# Check cleaning result
print("\nAFTER CLEANING")
print(df.isnull().sum())

# Change customer id and purchase amount column
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})

# Check formatting
print("\nAFTER FORMATTING - COLUMNS")
print(df.columns)

# create a column age_group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)

# Check formatting
print("\nAFTER FORMATTING - COLUMNS")
print(df[['age','age_group']].head(10))

# create column purchase_frequency_days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# Check formatting
print("\nAFTER FORMATTING - COLUMNS")
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))

# Check before drop column
print("\nBEFORE FORMATTING - COLUMNS")
print(df[['discount_applied', 'promo_code_used']].head(10))

# Check before drop column
print("\nIs two column have same value?")
print((df['discount_applied'] == df['promo_code_used']).all())

# Delete column
df = df.drop('promo_code_used', axis=1)

# Check formatting
print("\nAFTER FORMATTING - COLUMNS")
print(df.columns)

# SAVE cleaned data
df.to_csv("customer_shopping_behavior_cleaned.csv", index=False)
print("Cleaned data saved successfully.")

