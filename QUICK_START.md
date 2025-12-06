# Quick Start Guide

## For First-Time Setup

### 1. Activate Virtual Environment (if not already active)

```powershell
.\.venv\Scripts\Activate.ps1
```

**How to know if it's active?** You'll see `(.venv)` at the start of your terminal prompt.

### 2. Install Packages (if not already installed)

```powershell
pip install -r requirements.txt
```

**Only needed once!** Unless you add new packages.

---

## Running the Analysis

### Option 1: Use Sample Data (Quick Start)

```powershell
# Generate sample data
python generate_sample_data.py

# Run analysis
python data_analysis.py
```

### Option 2: Use Your Own Dataset

1. Download a dataset from Kaggle (see DATASETS.md)
2. Place the CSV file in this folder
3. Rename it to `sales_data.csv` (or update the filename in `data_analysis.py`)
4. Run:

```powershell
python data_analysis.py
```

---

## What Gets Created?

After running `data_analysis.py`, you'll have:

✅ **cleaned_data.csv** - Your cleaned dataset  
✅ **top_categories.csv** - Results for Question 1  
✅ **monthly_sales.csv** - Results for Question 2  
✅ **analysis_results.json** - Summary in JSON format  
✅ **sales_analysis_results.png** - Your charts!

---

## Viewing Results

### View the Charts

Double-click `sales_analysis_results.png` to open it.

### View the Data

Open any of the CSV files in Excel or a text editor.

### View JSON Results

Open `analysis_results.json` in VS Code or any text editor.

---

## Modifying the Code

### Change Number of Top Categories

In `data_analysis.py`, line ~140:

```python
top_5_categories = category_revenue.head(5)  # Change 5 to any number
```

### Analyze Different Time Periods

In `data_analysis.py`, after cleaning:

```python
# Filter to only 2023
df_clean = df_clean[df_clean['Order_Date'].dt.year == 2023]
```

### Change Chart Colors

In `create_visualizations()` function:

```python
# Change 'steelblue' to any color: 'red', 'green', 'purple', etc.
top_categories.plot(kind='bar', ax=ax1, color='steelblue')
```

---

## Common Issues

### ❌ "ModuleNotFoundError: No module named 'pandas'"

**Solution:** Install packages

```powershell
pip install pandas matplotlib numpy
```

### ❌ "FileNotFoundError: sales_data.csv"

**Solution:** Generate sample data first

```powershell
python generate_sample_data.py
```

### ❌ "cannot access local variable 'top_categories'"

**Solution:** Make sure all functions return values (check for `pass` statements)

### ❌ Virtual environment not activating

**Solution:** You might need to change PowerShell execution policy

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## File Structure

```
week6/
├── data_analysis.py          # Main analysis script
├── generate_sample_data.py   # Creates sample data
├── requirements.txt          # Package dependencies
├── README.md                 # Project documentation
├── GUIDE.md                  # Step-by-step guide
├── TUTORIAL.md               # Code explanation
├── DATASETS.md               # Dataset recommendations
├── QUICK_START.md            # This file
├── .gitignore                # Git ignore file
├── .venv/                    # Virtual environment (don't commit)
├── sales_data.csv            # Your dataset
└── [Output files]            # Generated after running analysis
    ├── cleaned_data.csv
    ├── top_categories.csv
    ├── monthly_sales.csv
    ├── analysis_results.json
    └── sales_analysis_results.png
```

---

## Development Workflow

### Day-to-Day Work

1. **Start**: Activate virtual environment

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. **Work**: Make changes to `data_analysis.py`

3. **Test**: Run your script

   ```powershell
   python data_analysis.py
   ```

4. **Review**: Check the output files and charts

5. **Iterate**: Repeat steps 2-4 until satisfied

6. **Document**: Update README.md with your findings

---

## Tips for Success

### 💡 **Start Small**

- Run the sample data first
- Make one small change at a time
- Test after each change

### 💡 **Use Print Statements**

Add `print()` to see what's happening:

```python
print(f"Data shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
```

### 💡 **Save Your Work**

Use Git to save progress:

```powershell
git add .
git commit -m "Completed data cleaning"
```

### 💡 **Read Error Messages**

- They tell you exactly what's wrong
- Google the error message
- Check line numbers

### 💡 **Ask for Help**

- Stack Overflow for pandas questions
- Official pandas documentation
- GitHub Copilot or ChatGPT for explanations

---

## Next Steps

1. ✅ Run the analysis with sample data
2. ✅ Understand the code (read TUTORIAL.md)
3. ✅ Get a real dataset from Kaggle
4. ✅ Customize the analysis for your data
5. ✅ Update README.md with findings
6. ✅ Create visualizations
7. ✅ Record demo video
8. ✅ Submit project

---

## Useful Commands Cheat Sheet

```powershell
# Activate environment
.\.venv\Scripts\Activate.ps1

# Deactivate environment
deactivate

# Install packages
pip install pandas matplotlib numpy

# Install from requirements
pip install -r requirements.txt

# List installed packages
pip list

# Run Python script
python script_name.py

# Run Python with specific version
python3 script_name.py

# Check Python version
python --version

# Open Python interactive shell
python

# Clear terminal
cls
```

---

## Questions & Debugging

### How do I know what columns are in my dataset?

```python
print(df.columns.tolist())
```

### How do I see the first few rows?

```python
print(df.head())
```

### How do I check data types?

```python
print(df.dtypes)
```

### How do I see unique values in a column?

```python
print(df['Category'].unique())
```

### How do I filter data?

```python
electronics = df[df['Category'] == 'Electronics']
high_sales = df[df['Sales'] > 1000]
```

---

**Good luck with your project! 🚀**

Remember: The best way to learn is by doing. Don't be afraid to experiment and make mistakes!
