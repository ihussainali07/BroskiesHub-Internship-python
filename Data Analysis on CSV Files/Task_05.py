import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\INFORMATION\Softwares\VS Code Files\sales_data.csv')

print("🔍 First 5 rows of the dataset:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

df.dropna(inplace=True)

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
else:
    print("'Date' column not found!")

if 'Product' in df.columns and 'Sales' in df.columns:
    product_sales = df.groupby('Product')['Sales'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(product_sales['Product'], product_sales['Sales'], color='teal')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("'Product' or 'Sales' column not found!")

if 'Month' in df.columns and 'Sales' in df.columns:
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Sales'],
             marker='o', color='orange')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("No 'Month' or 'Sales' column found!")

if 'Product' in df.columns and 'Quantity' in df.columns:
    qty_by_product = df.groupby('Product')['Quantity'].sum().reset_index()

    qty_by_product.plot(kind='bar', x='Product', y='Quantity', legend=False, color='purple')
    plt.title("Total Quantity Sold by Product")
    plt.ylabel("Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
