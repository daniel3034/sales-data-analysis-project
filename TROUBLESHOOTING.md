# Troubleshooting Guide

Common issues and how to fix them.

---

## Installation Issues

### Problem: "pip is not recognized"

**Cause:** Python not properly installed or not in PATH

**Solution:**

1. Reinstall Python from python.org
2. During installation, check "Add Python to PATH"
3. Or use: `python -m pip install pandas` instead of `pip install pandas`

---

### Problem: "Cannot activate virtual environment"

**Error:**

```
.\.venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled
```

**Solution:**
Run PowerShell as Administrator and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### Problem: Packages won't install

**Error:**

```
ERROR: Could not find a version that satisfies the requirement pandas
```

**Solutions:**

1. Update pip first:

   ```powershell
   python -m pip install --upgrade pip
   ```

2. Try installing one package at a time:

   ```powershell
   pip install pandas
   pip install matplotlib
   pip install numpy
   ```

3. Check Python version (need 3.7+):
   ```powershell
   python --version
   ```

---

## Data Loading Issues

### Problem: "FileNotFoundError: sales_data.csv"

**Cause:** File doesn't exist or is in wrong location

**Solution:**

1. Check file exists:

   ```powershell
   dir sales_data.csv
   ```

2. Generate sample data:

   ```powershell
   python generate_sample_data.py
   ```

3. Or update the filepath in code:
   ```python
   df = load_data('path/to/your/data.csv')
   ```

---

### Problem: "UnicodeDecodeError" when loading CSV

**Cause:** File has special encoding

**Solution:**
Add encoding parameter:

```python
df = pd.read_csv(filepath, encoding='utf-8')
# Or try:
df = pd.read_csv(filepath, encoding='latin-1')
```

---

### Problem: Dates not parsing correctly

**Symptoms:** Dates shown as text, can't resample

**Solution 1 - Specify format:**

```python
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%Y-%m-%d')
```

**Common formats:**

- `'%Y-%m-%d'` → 2022-01-31
- `'%m/%d/%Y'` → 01/31/2022
- `'%d-%m-%Y'` → 31-01-2022

**Solution 2 - Let pandas infer:**

```python
df['Order_Date'] = pd.to_datetime(df['Order_Date'], infer_datetime_format=True)
```

---

## Analysis Issues

### Problem: "KeyError: 'Category'"

**Cause:** Column name doesn't match

**Solution:**

1. Check actual column names:

   ```python
   print(df.columns.tolist())
   ```

2. Update code to match exact column name (case-sensitive):

   ```python
   # If the column is actually named 'category' (lowercase)
   df.groupby('category')['Sales'].sum()
   ```

3. Or rename columns:
   ```python
   df = df.rename(columns={'category': 'Category'})
   ```

---

### Problem: "TypeError: unsupported operand type(s)"

**Example:**

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**Cause:** Trying to do math with wrong data types

**Solution:**
Convert to correct type:

```python
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
```

Check data types:

```python
print(df.dtypes)
```

---

### Problem: Empty results from groupby

**Symptoms:** Getting 0 or empty results

**Solution:**

1. Check for missing values:

   ```python
   print(df['Category'].isnull().sum())
   print(df['Sales'].isnull().sum())
   ```

2. Check data exists:

   ```python
   print(df.shape)
   print(df.head())
   ```

3. Print intermediate results:
   ```python
   grouped = df.groupby('Category')
   print(grouped.size())  # Shows count in each group
   ```

---

### Problem: "FutureWarning: 'M' is deprecated"

**Warning:**

```
FutureWarning: 'M' is deprecated and will be removed in a future version, please use 'ME' instead.
```

**Solution:**
Replace `'M'` with `'ME'`:

```python
# Old:
monthly_sales = df_time['Sales'].resample('M').sum()

# New:
monthly_sales = df_time['Sales'].resample('ME').sum()
```

**Other frequency codes:**

- 'D' → Daily
- 'W' → Weekly
- 'ME' → Month End (new)
- 'MS' → Month Start
- 'Q' → Quarterly
- 'Y' → Yearly

---

## Visualization Issues

### Problem: Charts not showing

**Cause:** `plt.show()` might be blocking or not working

**Solution 1 - Save instead of show:**

```python
plt.savefig('chart.png')
# Then open chart.png manually
```

**Solution 2 - Use non-interactive backend:**

```python
import matplotlib
matplotlib.use('Agg')  # Add this before importing pyplot
import matplotlib.pyplot as plt
```

---

### Problem: Chart looks bad / labels cut off

**Solution:**
Add these before saving:

```python
plt.tight_layout()  # Adjusts spacing
plt.savefig('chart.png', bbox_inches='tight')  # Prevents cutting
```

For better quality:

```python
plt.savefig('chart.png', dpi=300, bbox_inches='tight')
```

---

### Problem: "ValueError: x and y must have same first dimension"

**Cause:** Data shapes don't match

**Solution:**
Check data shapes:

```python
print(f"x shape: {x.shape}")
print(f"y shape: {y.shape}")
```

For plotting from DataFrame:

```python
# This handles shapes automatically
df.plot(x='Date', y='Sales')
```

---

## Runtime Errors

### Problem: "NameError: name 'df' is not defined"

**Cause:** Variable not created yet

**Solution:**
Make sure you:

1. Load data first: `df = load_data('file.csv')`
2. Run functions in order
3. Check for typos in variable names

---

### Problem: "AttributeError: 'NoneType' object has no attribute"

**Cause:** Function returned None instead of data

**Solution:**
Check function returns value:

```python
def my_function(df):
    result = df.groupby('Category')['Sales'].sum()
    return result  # Make sure this line exists!
```

Replace any `pass` statements with actual code or `return` statements.

---

### Problem: "ValueError: cannot convert float NaN to integer"

**Cause:** Missing values in data

**Solution:**
Handle missing values before converting:

```python
df['Quantity'] = df['Quantity'].fillna(0).astype(int)
```

Or remove missing values:

```python
df = df.dropna(subset=['Quantity'])
df['Quantity'] = df['Quantity'].astype(int)
```

---

## Performance Issues

### Problem: Code runs very slowly

**Causes & Solutions:**

1. **Large dataset:**

   - Test with smaller subset first:

   ```python
   df_small = df.head(1000)  # Use first 1000 rows
   ```

2. **Inefficient loops:**

   - Use pandas built-in functions instead of loops
   - Bad: `for row in df.iterrows()`
   - Good: `df.groupby()`, `df.apply()`

3. **Reading file repeatedly:**
   - Load once, save to variable
   - Don't reload inside loops

---

## Output Issues

### Problem: Numbers show as 1.234567e+06

**Cause:** Scientific notation

**Solution:**
Set pandas display options:

```python
pd.options.display.float_format = '{:,.2f}'.format
```

Or format when printing:

```python
print(f"Sales: ${value:,.2f}")
```

---

### Problem: Too much output / output truncated

**Solution:**
Control pandas display:

```python
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
```

---

## Git Issues

### Problem: Accidentally committed large files

**Solution:**

1. Add to .gitignore:

   ```
   *.csv
   *.png
   ```

2. Remove from git (keep local):
   ```powershell
   git rm --cached filename.csv
   git commit -m "Remove large file"
   ```

---

## Debugging Tips

### 1. Print Everything

Add print statements to see what's happening:

```python
print(f"Data shape: {df.shape}")
print(f"Column names: {df.columns.tolist()}")
print(f"First row: {df.iloc[0]}")
```

### 2. Test with Small Data

Create tiny test dataset:

```python
test_df = pd.DataFrame({
    'Category': ['A', 'A', 'B'],
    'Sales': [100, 200, 150]
})
```

### 3. Check Types

```python
print(type(variable))
print(df.dtypes)
```

### 4. Use Try-Except

Catch errors gracefully:

```python
try:
    df = pd.read_csv('sales_data.csv')
except FileNotFoundError:
    print("File not found! Generating sample data...")
    df = generate_sample_data()
```

### 5. Read Error Messages Carefully

Error messages tell you:

- What went wrong
- Where it happened (line number)
- Sometimes how to fix it

### 6. Google the Error

Search for:

- The error message (exact text)
- "pandas" + error message
- Your specific operation + error

---

## Getting Help

### Stack Overflow

Search or ask questions: https://stackoverflow.com/questions/tagged/pandas

### Pandas Documentation

Official docs: https://pandas.pydata.org/docs/

### ChatGPT / GitHub Copilot

Ask:

- "How do I [specific task] in pandas?"
- "What does this error mean: [error message]"
- "Explain this code: [paste code]"

### VS Code Debugger

Set breakpoints and step through code:

1. Click left of line number to add breakpoint
2. Press F5 to start debugging
3. Use F10 to step through code

---

## Still Stuck?

### Checklist:

- [ ] Read the error message completely
- [ ] Check spelling and capitalization
- [ ] Verify file/column names are correct
- [ ] Print intermediate results
- [ ] Try with smaller dataset
- [ ] Google the exact error
- [ ] Check pandas documentation
- [ ] Ask ChatGPT or instructor

### When Asking for Help, Include:

1. What you're trying to do
2. What you expected to happen
3. What actually happened (full error message)
4. Relevant code snippet
5. Sample of your data

**Good question:**

> "I'm trying to group sales by category, but I get KeyError: 'Category'. Here's my code: [code].
> My columns are: ['order_id', 'date', 'category', 'sales']. What am I doing wrong?"

**Bad question:**

> "My code doesn't work. Help!"

---

**Remember:** Everyone gets errors! They're part of learning. The key is learning how to debug them systematically.
