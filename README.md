# EDA Report Generator

A Python project that generates a text-based Exploratory Data Analysis (EDA) report from CSV datasets.

## Features

- Dataset Overview
- Missing Values Analysis
- Duplicate Detection
- Numerical Statistics
  - Mean
  - Median
  - Standard Deviation
  - Minimum
  - Maximum
  - Count
- Categorical Statistics
  - Unique Values
  - Most Frequent Value
  - Frequency
- TXT Report Export

## Project Structure

```text
eda_report_generator/
│
├── data/
│   └── your_dataset.csv
│
├── reports/
│   └── report.txt
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── overview.py
│   ├── missing.py
│   ├── duplicates.py
│   ├── statistics.py
│   └── report_writer.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd eda_report_generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Step 1

Place your CSV file inside the `data/` folder.

Example:

```text
data/
└── adult-test.csv
```

### Step 2

Run the program:

```bash
python main.py
```

### Step 3

Enter the dataset filename:

```text
Enter CSV filename: adult-test.csv
```

### Step 4

The generated report will be saved automatically:

```text
reports/report.txt
```

## Example Output

```text
EDA REPORT
========================================

OVERVIEW
--------------------
Rows: 16281
Columns: 15

DUPLICATES
--------------------
Duplicate Rows: 5
Duplicate Percentage: 0.03%

MISSING VALUES
--------------------
Columns With Missing Values: 0

No missing values detected.
```

## Technologies Used

- Python
- Pandas
- NumPy

## Future Improvements

- Outlier Detection
- Correlation Analysis
- HTML Report Export
- Data Visualizations
- Interactive Reports

## Author

Abror Akhmadkhujaev
