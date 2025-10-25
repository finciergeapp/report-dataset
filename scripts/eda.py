"""Module for performing Exploratory Data Analysis (EDA) on the blood reports dataset.

This module loads the synthetic blood reports dataset, displays basic information,
summary statistics, performs outlier detection, and calculates the correlation matrix
for numerical columns.
"""

import pandas as pd

def perform_eda(file_path: str = "data/blood_reports_dataset.csv") -> None:
    """Performs exploratory data analysis on the blood reports dataset.

    Args:
        file_path (str): The path to the blood reports CSV file.
    """
    # Load the dataset
    df = pd.read_csv(file_path)

    # Display basic information about the dataset
    print("Dataset Info:")
    print(df.info())

    # Display descriptive statistics for numerical columns
    print("\nDataset Description:")
    print(df.describe())

    # Summary statistics for numerical columns (redundant with df.describe(), keeping for clarity if specific stats were needed)
    print("\nSummary Statistics (numerical columns):")
    print(df.describe(include=np.number))

    # Outlier detection (example: using IQR for Haemoglobin)
    # Calculate Q1 (25th percentile) and Q3 (75th percentile) for Haemoglobin
    Q1 = df['Haemoglobin_g_dl'].quantile(0.25)
    Q3 = df['Haemoglobin_g_dl'].quantile(0.75)
    IQR = Q3 - Q1  # Calculate the Interquartile Range

    # Define outlier thresholds
    outlier_threshold_upper = Q3 + 1.5 * IQR
    outlier_threshold_lower = Q1 - 1.5 * IQR

    # Identify outliers in Haemoglobin
    outliers_hb = df[(df['Haemoglobin_g_dl'] < outlier_threshold_lower) | (df['Haemoglobin_g_dl'] > outlier_threshold_upper)]
    print(f"\nOutliers in Haemoglobin_g_dl (using IQR): {len(outliers_hb)} records")

    # Correlation matrix for numerical columns
    print("\nCorrelation Matrix (numerical columns):")
    print(df.corr(numeric_only=True))

if __name__ == '__main__':
    import numpy as np # Import numpy here as it's only used in this block
    perform_eda()