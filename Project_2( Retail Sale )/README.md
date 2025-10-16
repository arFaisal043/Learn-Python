# Retail Sales Dataset Analysis

## Overview
This project analyzes a retail sales customer dataset containing 200 records with demographic and acquisition information. The analysis focuses on customer acquisition trends, demographics, and geographic distribution.

## Dataset Information
- **Rows**: 200 customers
- **Columns**: 7 original features + 4 engineered features
- **No missing values**

### Original Columns:
- CustomerID, FirstName, LastName, Gender, BirthDate, City, JoinDate

### Engineered Features:
- JoinYear, JoinMonth, JoinYearMonth, Age

## Key Insights

### 1. Customer Acquisition Trends
- **Peak Acquisition Month**: January (21 customers across all years)
- **Peak Acquisition Year**: 2022 (45 customers)
- Monthly and yearly trends show seasonal patterns in customer growth

### 2. Customer Demographics
- **Gender Distribution**: 113 Male (56.5%), 87 Female (43.5%)
- **Age Range**: 18-71 years
- Age distribution shows customers across all adult age groups

### 3. Geographic Distribution
- Customers are distributed across multiple cities
- Analysis reveals concentration patterns in specific locations

## Visualizations
The analysis includes:
- Monthly customer acquisition trend line chart
- Yearly customer acquisition bar chart  
- Gender distribution visualization

## Tools & Libraries
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook

## Usage
Run the `retail_sales.ipynb` notebook to reproduce the analysis and generate insights for marketing strategy and customer segmentation.