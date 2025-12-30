import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')

# load the messy data
df = pd.read_csv('marketing_campaign_data_messy.csv')

print(df.head())
print(df.duplicated().sum())
print(df.columns.tolist()) # many columns heading has some space
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print("Fixed the columns problems...")
print(df.columns.tolist())
print(df.head())

# Remove the '$' sign
dirty_spend_mask = df['spend'] = df['spend'].astype(str).str.replace('$', '', regex=False).str.strip()
dirty_spend_mask

# Convert to numeric value(float) for calculation
df['spend'] = pd.to_numeric(df['spend'])