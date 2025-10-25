"""Module for generating static visualizations from the blood reports dataset.

This module loads the preprocessed blood reports dataset and generates several
key visualizations, including infection trends, anemia distribution, and CRP levels
over time. The visualizations are saved as PNG files in the 'reports/' directory.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_static_visuals(file_path: str = "../data/blood_reports_dataset.csv", output_dir: str = "../reports/") -> None:
    """Generates and saves static visualizations from the blood reports dataset.

    Args:
        file_path (str): The path to the blood reports CSV file.
        output_dir (str): The directory where the generated image files will be saved.
    """
    # Load the dataset
    df = pd.read_csv(file_path)

    # Ensure 'Date' column is in datetime format for time-series analysis
    df['Date'] = pd.to_datetime(df['Date'])

    # Set a professional style for all plots
    sns.set_theme(style="whitegrid")

    # --- Visualization 1: Infection Trends over Time ---
    plt.figure(figsize=(12, 6))
    # Filter data for bacterial and viral infections
    infection_df = df[df['Diagnosis'].isin(['Bacterial infection', 'Viral infection'])]
    # Group by date and count the number of infection cases
    infection_counts = infection_df.groupby('Date').size().reset_index(name='count')
    # Plot the daily infection cases
    sns.lineplot(data=infection_counts, x='Date', y='count')
    plt.title('Daily Infection Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.tight_layout()
    # Save the plot to the specified output directory
    plt.savefig(f'{output_dir}infection_trends.png')
    plt.close()

    # --- Visualization 2: Anemia Distribution by Age and Gender ---
    plt.figure(figsize=(12, 6))
    # Filter data for anemia cases
    anemia_df = df[df['Diagnosis'] == 'Anemia']
    # Plot the distribution of anemia cases by age, separated by gender
    sns.histplot(data=anemia_df, x='Age', hue='Gender', multiple='stack', bins=20)
    plt.title('Anemia Cases Distribution by Age and Gender')
    plt.xlabel('Age')
    plt.ylabel('Number of Cases')
    plt.tight_layout()
    # Save the plot
    plt.savefig(f'{output_dir}anemia_distribution.png')
    plt.close()

    # --- Visualization 3: CRP Trends (Inflammation Spikes) ---
    plt.figure(figsize=(12, 6))
    # Plot CRP levels over time to identify inflammation trends
    sns.lineplot(data=df, x='Date', y='CRP_mg_L')
    plt.title('CRP Levels Over Time')
    plt.xlabel('Date')
    plt.ylabel('CRP (mg/L)')
    plt.tight_layout()
    # Save the plot
    plt.savefig(f'{output_dir}crp_trends.png')
    plt.close()

    print(f"✅ Static visuals generated and saved to {output_dir}")

if __name__ == '__main__':
    generate_static_visuals()