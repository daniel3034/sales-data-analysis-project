# Sales Data Analysis - Step-by-Step Guide

This guide will walk you through the entire data analysis process.

## Week 1: Setup and Data Preparation

### Day 1: Environment Setup and Data Search (3 hours)

#### Step 1: Set up Python environment

1. Open terminal in VS Code
2. Create a virtual environment:
   ```powershell
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```

#### Step 2: Find a suitable dataset

1. Go to [Kaggle.com](https://kaggle.com)
2. Search for "sales data" or "retail sales"
3. Recommended datasets:
   - "Superstore Sales Dataset"
   - "Online Retail Dataset"
   - "Sales Product Data"
4. Download the CSV file and place it in your project folder
5. Rename it to `sales_data.csv` or update the filename in `data_analysis.py`

### Day 2: Load and Clean Data (3 hours)

#### Understanding the code structure:

- `load_data()`: Reads CSV file using pandas
- `explore_data()`: Shows first rows, data types, missing values
- `clean_data()`: Prepares data for analysis

#### Tasks:

1. Run the script to see the raw data
2. Identify columns for:
   - Date/Time
   - Product Category
   - Sales/Revenue
3. Implement cleaning steps in `clean_data()` function

### Day 3: Exploratory Data Analysis (3 hours)

#### What to explore:

- Data shape (rows, columns)
- Data types of each column
- Missing values
- Summary statistics
- Unique values in categorical columns

#### Tasks:

1. Add code to check for duplicates
2. Add code to check date ranges
3. Document your findings in comments

### Day 4: Answer Question 1 (2 hours)

**Question:** Which are the top 5 product categories by revenue?

#### Concepts you'll learn:

- **Grouping**: Combine rows with same category
- **Aggregation**: Sum revenue for each group
- **Sorting**: Order results from highest to lowest

#### Implementation steps:

```python
# Group by category and sum revenue
category_revenue = df.groupby('Category')['Revenue'].sum()

# Sort in descending order and take top 5
top_5 = category_revenue.sort_values(ascending=False).head(5)
```

### Day 5: Answer Question 2 (2 hours)

**Question:** How do monthly sales change over the last two years?

#### Concepts you'll learn:

- **Data conversion**: Convert string dates to datetime objects
- **Resampling**: Group data by time periods (months)
- **Time series analysis**: Analyze trends over time

#### Implementation steps:

```python
# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set date as index
df.set_index('Date', inplace=True)

# Resample by month and sum sales
monthly_sales = df['Sales'].resample('M').sum()
```

### Day 6: Buffer/Testing (1 hour)

## Week 2: Visualization and Documentation

### Day 8: Create Visualizations (2 hours)

#### Chart 1: Bar chart for top categories

```python
top_categories.plot(kind='bar', color='steelblue')
plt.title('Top 5 Product Categories by Revenue')
plt.xlabel('Category')
plt.ylabel('Revenue ($)')
```

#### Chart 2: Line chart for monthly sales

```python
monthly_sales.plot(kind='line', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
```

### Day 9: Save Results (2 hours)

The code will save:

1. `cleaned_data.csv` - Your cleaned dataset
2. `top_categories.csv` - Results for Question 1
3. `monthly_sales.csv` - Results for Question 2
4. `analysis_results.json` - Summary in JSON format
5. `sales_analysis_results.png` - Visualization charts

### Day 10: Write Documentation (2 hours)

Update README.md with:

1. Dataset description and link
2. Your analysis results
3. Insights you discovered
4. Screenshots of visualizations

### Day 11: Prepare Report (1 hour)

### Day 12: Final Testing (1 hour)

Run the complete analysis and verify:

- [ ] All packages install correctly
- [ ] Data loads without errors
- [ ] Both questions are answered
- [ ] Visualizations are created
- [ ] All files are saved
- [ ] Code is well-commented

## Common Issues and Solutions

### Issue 1: Date parsing errors

**Solution:** Check date format and use `pd.to_datetime()` with format parameter

### Issue 2: Missing values cause errors

**Solution:** Use `df.dropna()` or `df.fillna()` to handle missing data

### Issue 3: Column names don't match

**Solution:** Print `df.columns` to see actual column names in your dataset

## Key Pandas Functions You'll Use

| Function           | Purpose                    | Example                        |
| ------------------ | -------------------------- | ------------------------------ |
| `pd.read_csv()`    | Load CSV file              | `df = pd.read_csv('data.csv')` |
| `df.head()`        | Show first 5 rows          | `df.head()`                    |
| `df.info()`        | Show data types and memory | `df.info()`                    |
| `df.describe()`    | Summary statistics         | `df.describe()`                |
| `df.groupby()`     | Group data                 | `df.groupby('Category')`       |
| `df.sort_values()` | Sort data                  | `df.sort_values('Revenue')`    |
| `pd.to_datetime()` | Convert to datetime        | `pd.to_datetime(df['Date'])`   |
| `df.resample()`    | Aggregate by time period   | `df.resample('M').sum()`       |

## Tips for Success

1. **Read error messages carefully** - They often tell you exactly what's wrong
2. **Print intermediate results** - Use `print()` to check your work at each step
3. **Start simple** - Get basic code working before adding complexity
4. **Google is your friend** - Search for "pandas how to [what you want to do]"
5. **Save frequently** - Use version control (Git) to save progress

## Next Steps After Core Project

1. Add a third analysis question
2. Try different visualization types (pie charts, scatter plots)
3. Add statistical tests (correlation, t-tests)
4. Create an interactive dashboard with Plotly
5. Automate report generation
