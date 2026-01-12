import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset 
# Dataset from UCI / Databricks: https://github.com/databricks/Spark-The-Definitive-Guide (Databricks.com, 2018)
# Code written for exploratory analysis using common pandas/matplotlib patterns

url = "https://raw.githubusercontent.com/databricks/Spark-The-Definitive-Guide/master/data/retail-data/all/online-retail-dataset.csv"
df = pd.read_csv(url)

# Clean and process
# Convert InvoiceDate to datetime format for time series analysis (McKinney, 2010)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Drop rows with missing Quantity or UnitPrice values (McKinney, 2010)
df.dropna(subset=['Quantity', 'UnitPrice'], inplace=True)

# Compute total transaction amount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')
df['Weekday'] = df['InvoiceDate'].dt.dayofweek

# Stats
print(f"Revenue: ${df['TotalAmount'].sum():,.2f}")
print(f"Avg Transaction: ${df['TotalAmount'].mean():.2f}")
print(f"Items Sold: {df['Quantity'].sum():,}")
print(f"Unique Customers: {df['CustomerID'].nunique()}")
print(f"Unique Products: {df['StockCode'].nunique()}")
print(f"Date Range: {df['InvoiceDate'].min().date()} to {df['InvoiceDate'].max().date()}")

# Visualizations
fig, ax = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Online Retail Dataset Analysis', fontsize=16)

# Daily sales
df.groupby(df['InvoiceDate'].dt.date)['TotalAmount'].sum().plot(ax=ax[0, 0], title='Daily Sales')

# Monthly sales
df.groupby('YearMonth')['TotalAmount'].sum().plot(kind='bar', ax=ax[0, 1], title='Monthly Sales')

# Quantity vs Unit Price
ax[1, 0].scatter(df['Quantity'], df['UnitPrice'], alpha=0.4)
ax[1, 0].set(title='Quantity vs Unit Price', xlabel='Quantity', ylabel='Unit Price')

# Transaction amount distribution (trimmed outliers)
a = df['TotalAmount']
a[(a > a.quantile(0.05)) & (a < a.quantile(0.95))].plot.hist(bins=40, alpha=0.7, ax=ax[1, 1])
ax[1, 1].set(title='Transaction Amount Distribution', xlabel='Amount', ylabel='Count')

plt.tight_layout(); plt.show()

# Insights
w = df.groupby('Weekday')['TotalAmount'].mean()
print(f"Largest Transaction: ${df['TotalAmount'].max():.2f}")
if (r := df[df['TotalAmount'] < 0]).shape[0]:
    print(f"Returns/Refunds: {len(r)} ({len(r)/len(df)*100:.1f}%)")
print(f"Best Sales Day: {['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][w.idxmax()]} (${w.max():.2f}/txn)")
print(f"Quantity-UnitPrice Correlation: {df['Quantity'].corr(df['UnitPrice']):.2f}")
