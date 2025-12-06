# Sample Dataset Generator
# Use this to create test data if you don't have a real dataset yet

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_sales_data():
    """
    Generate a sample sales dataset for testing
    This creates realistic-looking sales data with:
    - Dates over 2 years
    - Multiple product categories
    - Varying sales amounts
    """
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Parameters
    n_records = 5000
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    
    # Categories and subcategories
    categories = {
        'Electronics': ['Phones', 'Laptops', 'Tablets', 'Accessories'],
        'Furniture': ['Chairs', 'Desks', 'Tables', 'Storage'],
        'Office Supplies': ['Paper', 'Pens', 'Binders', 'Art'],
        'Clothing': ['Shirts', 'Pants', 'Shoes', 'Accessories'],
        'Home & Garden': ['Decor', 'Tools', 'Kitchen', 'Outdoor']
    }
    
    # Generate random dates
    date_range = (end_date - start_date).days
    random_dates = [start_date + timedelta(days=int(np.random.random() * date_range)) 
                    for _ in range(n_records)]
    
    # Generate random categories
    category_list = []
    subcategory_list = []
    for _ in range(n_records):
        category = np.random.choice(list(categories.keys()))
        subcategory = np.random.choice(categories[category])
        category_list.append(category)
        subcategory_list.append(subcategory)
    
    # Generate sales data with realistic patterns
    # Electronics tend to have higher prices
    base_price = []
    for cat in category_list:
        if cat == 'Electronics':
            base_price.append(np.random.uniform(200, 2000))
        elif cat == 'Furniture':
            base_price.append(np.random.uniform(100, 1500))
        elif cat == 'Clothing':
            base_price.append(np.random.uniform(20, 200))
        elif cat == 'Home & Garden':
            base_price.append(np.random.uniform(15, 500))
        else:  # Office Supplies
            base_price.append(np.random.uniform(5, 100))
    
    # Generate quantities
    quantities = np.random.randint(1, 10, n_records)
    
    # Calculate sales and profit
    sales = [round(p * q, 2) for p, q in zip(base_price, quantities)]
    profit = [round(s * np.random.uniform(0.1, 0.4), 2) for s in sales]
    
    # Generate regions and states
    regions = ['East', 'West', 'Central', 'South']
    states = ['California', 'Texas', 'Florida', 'New York', 'Illinois', 
              'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
    
    # Create DataFrame
    df = pd.DataFrame({
        'Order_ID': [f'ORD-{i:05d}' for i in range(1, n_records + 1)],
        'Order_Date': random_dates,
        'Ship_Date': [d + timedelta(days=np.random.randint(1, 7)) 
                      for d in random_dates],
        'Category': category_list,
        'Sub_Category': subcategory_list,
        'Product_Name': [f'{sub} - Model {np.random.randint(100, 999)}' 
                         for sub in subcategory_list],
        'Sales': sales,
        'Quantity': quantities,
        'Profit': profit,
        'Region': np.random.choice(regions, n_records),
        'State': np.random.choice(states, n_records)
    })
    
    # Sort by date
    df = df.sort_values('Order_Date').reset_index(drop=True)
    
    return df


def main():
    print("Generating sample sales dataset...")
    
    # Generate the data
    df = generate_sample_sales_data()
    
    # Save to CSV
    output_file = 'sales_data.csv'
    df.to_csv(output_file, index=False)
    
    print(f"\nDataset generated successfully!")
    print(f"Saved to: {output_file}")
    print(f"\nDataset info:")
    print(f"- Records: {len(df)}")
    print(f"- Date range: {df['Order_Date'].min()} to {df['Order_Date'].max()}")
    print(f"- Categories: {df['Category'].nunique()}")
    print(f"- Total sales: ${df['Sales'].sum():,.2f}")
    
    print("\nFirst few rows:")
    print(df.head())
    
    print("\nSummary statistics:")
    print(df[['Sales', 'Quantity', 'Profit']].describe())


if __name__ == "__main__":
    main()
