# Sales Data Analysis and Visualization
# This program analyzes sales data to answer business questions

import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

def load_data(filepath):
    """
    Load the dataset from a CSV file
    
    Parameters:
    filepath (str): Path to the CSV file
    
    Returns:
    DataFrame: Loaded pandas DataFrame
    """
    print(f"Loading data from {filepath}...")
    # Try different encodings for compatibility
    try:
        df = pd.read_csv(filepath)
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding='latin-1')
    print(f"Data loaded successfully! Shape: {df.shape}")
    return df


def explore_data(df):
    """
    Perform exploratory data analysis
    
    Parameters:
    df (DataFrame): The dataset to explore
    """
    print("\n=== EXPLORATORY DATA ANALYSIS ===")
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nSummary Statistics:")
    print(df.describe())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nColumn Names:")
    print(df.columns.tolist())


def clean_data(df):
    """
    Clean and prepare the data for analysis
    
    Parameters:
    df (DataFrame): The dataset to clean
    
    Returns:
    DataFrame: Cleaned dataset
    """
    print("\n=== CLEANING DATA ===")
    
    # Make a copy to avoid modifying original
    df_clean = df.copy()
    
    # Step 1: Convert date columns to datetime
    # This converts string dates to datetime objects for time-based analysis
    print("Converting date columns to datetime...")
    df_clean['Order Date'] = pd.to_datetime(df_clean['Order Date'])
    df_clean['Ship Date'] = pd.to_datetime(df_clean['Ship Date'])
    
    # Step 2: Handle missing values
    # Check for missing values and decide how to handle them
    print(f"Missing values before cleaning: {df_clean.isnull().sum().sum()}")
    df_clean = df_clean.dropna()  # Remove rows with any missing values
    print(f"Missing values after cleaning: {df_clean.isnull().sum().sum()}")
    
    # Step 3: Remove duplicates
    # Remove any duplicate rows
    duplicates = df_clean.duplicated().sum()
    print(f"Duplicate rows found: {duplicates}")
    df_clean = df_clean.drop_duplicates()
    
    # Step 4: Fix data types
    # Ensure numeric columns are the correct type
    df_clean['Sales'] = pd.to_numeric(df_clean['Sales'], errors='coerce')
    df_clean['Profit'] = pd.to_numeric(df_clean['Profit'], errors='coerce')
    df_clean['Quantity'] = pd.to_numeric(df_clean['Quantity'], errors='coerce')
    
    # Step 5: Remove any negative sales (data quality issue)
    df_clean = df_clean[df_clean['Sales'] >= 0]
    
    print(f"Data cleaning completed! Final shape: {df_clean.shape}")
    return df_clean


def question_1_top_categories(df):
    """
    Question 1: Which are the top 3 product categories by revenue?
    
    This demonstrates: grouping, aggregation (sum), and sorting
    
    Parameters:
    df (DataFrame): Cleaned dataset
    
    Returns:
    DataFrame: Top 3 categories by revenue
    """
    print("\n=== QUESTION 1: Top 3 Product Categories by Revenue ===")
    
    # Step 1: Group by category
    # This combines all rows with the same category together
    # Step 2: Sum the revenue (Sales column)
    # The aggregation function sums all sales for each category
    category_revenue = df.groupby('Category')['Sales'].sum()
    
    # Step 3: Sort in descending order (highest to lowest)
    # ascending=False means we want the biggest values first
    category_revenue = category_revenue.sort_values(ascending=False)
    
    # Step 4: Take all categories (Superstore has 3)
    top_categories = category_revenue
    
    # Display results
    print("\nTop 3 Categories by Revenue:")
    for i, (category, revenue) in enumerate(top_categories.items(), 1):
        print(f"{i}. {category}: ${revenue:,.2f}")
    
    return top_categories


def question_2_monthly_sales(df):
    """
    Question 2: How do monthly sales change over the last two years?
    
    This demonstrates: date conversion, resampling/aggregation
    
    Parameters:
    df (DataFrame): Cleaned dataset
    
    Returns:
    DataFrame: Monthly sales aggregated
    """
    print("\n=== QUESTION 2: Monthly Sales Trends ===")
    
    # Step 1: Create a copy and ensure date is datetime (already done in cleaning)
    df_time = df.copy()
    
    # Step 2: Set date as index
    # This allows us to use time-based operations like resample
    df_time = df_time.set_index('Order Date')
    
    # Step 3: Resample by month ('M' means month-end frequency)
    # Step 4: Aggregate sales by summing
    # This groups all sales within each month and sums them
    monthly_sales = df_time['Sales'].resample('M').sum()
    
    # Display results
    print(f"\nMonthly sales from {monthly_sales.index[0].strftime('%Y-%m')} to {monthly_sales.index[-1].strftime('%Y-%m')}")
    print(f"Average monthly sales: ${monthly_sales.mean():,.2f}")
    print(f"Highest month: {monthly_sales.idxmax().strftime('%Y-%m')} with ${monthly_sales.max():,.2f}")
    print(f"Lowest month: {monthly_sales.idxmin().strftime('%Y-%m')} with ${monthly_sales.min():,.2f}")
    
    print("\nFirst few months:")
    print(monthly_sales.head())
    
    return monthly_sales


def create_visualizations(top_categories, monthly_sales):
    """
    Create visualizations for the analysis results
    
    Parameters:
    top_categories (DataFrame): Top categories data
    monthly_sales (DataFrame): Monthly sales data
    """
    print("\n=== CREATING VISUALIZATIONS ===")
    
    # Create a figure with 2 subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Chart 1: Bar chart for top categories
    # This shows which categories generate the most revenue
    top_categories.plot(kind='bar', ax=ax1, color='steelblue', edgecolor='black')
    ax1.set_title('Top 3 Product Categories by Revenue', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Category', fontsize=12)
    ax1.set_ylabel('Revenue ($)', fontsize=12)
    ax1.set_xticklabels(top_categories.index, rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on top of bars
    for i, v in enumerate(top_categories.values):
        ax1.text(i, v, f'${v/1000:.0f}K', ha='center', va='bottom')
    
    # Chart 2: Line chart for monthly sales
    # This shows how sales trend over time
    monthly_sales.plot(kind='line', ax=ax2, color='green', linewidth=2, marker='o')
    ax2.set_title('Monthly Sales Trend (2014-2017)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Month', fontsize=12)
    ax2.set_ylabel('Sales ($)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    
    # Rotate x-axis labels for better readability
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('sales_analysis_results.png', dpi=300, bbox_inches='tight')
    print("✓ Visualization saved as 'sales_analysis_results.png'")
    plt.show()


def save_results(df_clean, top_categories, monthly_sales):
    """
    Save the analysis results to files
    
    Parameters:
    df_clean (DataFrame): Cleaned dataset
    top_categories (DataFrame): Top categories results
    monthly_sales (DataFrame): Monthly sales results
    """
    print("\n=== SAVING RESULTS ===")
    
    # Save cleaned data
    df_clean.to_csv('cleaned_data.csv', index=False)
    print("Cleaned data saved to 'cleaned_data.csv'")
    
    # Save analysis results as CSV
    top_categories.to_csv('top_categories.csv')
    print("Top categories saved to 'top_categories.csv'")
    
    monthly_sales.to_csv('monthly_sales.csv')
    print("Monthly sales saved to 'monthly_sales.csv'")
    
    # Save results as JSON
    results = {
        'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'top_categories': top_categories.to_dict(),
        'monthly_sales_summary': {
            'mean': float(monthly_sales.mean()),
            'total': float(monthly_sales.sum()),
            'min': float(monthly_sales.min()),
            'max': float(monthly_sales.max())
        }
    }
    
    with open('analysis_results.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Results saved to 'analysis_results.json'")


def main():
    """
    Main function to run the complete analysis
    """
    print("=" * 60)
    print("SALES DATA ANALYSIS AND VISUALIZATION")
    print("=" * 60)
    
    # Step 1: Load data
    df = load_data('sales_data.csv')
    
    # Step 2: Explore data
    explore_data(df)
    
    # Step 3: Clean data
    df_clean = clean_data(df)
    
    # Step 4: Answer Question 1
    top_categories = question_1_top_categories(df_clean)
    
    # Step 5: Answer Question 2
    monthly_sales = question_2_monthly_sales(df_clean)
    
    # Step 6: Create visualizations
    create_visualizations(top_categories, monthly_sales)
    
    # Step 7: Save results
    save_results(df_clean, top_categories, monthly_sales)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - cleaned_data.csv (cleaned dataset)")
    print("  - top_categories.csv (Question 1 results)")
    print("  - monthly_sales.csv (Question 2 results)")
    print("  - analysis_results.json (summary in JSON)")
    print("  - sales_analysis_results.png (visualizations)")
    print("\nNext steps:")
    print("  1. Open sales_analysis_results.png to view charts")
    print("  2. Review the CSV files for detailed data")
    print("  3. Update README.md with your findings")
    print("  4. Create a demo video showing the results")


if __name__ == "__main__":
    main()
