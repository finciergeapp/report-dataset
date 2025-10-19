import pandas as pd

# Load the dataset
df = pd.read_csv("blood_reports_dataset.csv")

# Display basic information
print("Dataset Info:")
print(df.info())

print("\nDataset Description:")
print(df.describe())

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Outlier detection (example: using IQR for Haemoglobin)
Q1 = df['Haemoglobin_g_dl'].quantile(0.25)
Q3 = df['Haemoglobin_g_dl'].quantile(0.75)
IQR = Q3 - Q1
outlier_threshold_upper = Q3 + 1.5 * IQR
outlier_threshold_lower = Q1 - 1.5 * IQR

outliers_hb = df[(df['Haemoglobin_g_dl'] < outlier_threshold_lower) | (df['Haemoglobin_g_dl'] > outlier_threshold_upper)]
print(f"\nOutliers in Haemoglobin_g_dl (using IQR): {len(outliers_hb)} records")

# Correlation matrix for numerical columns
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))