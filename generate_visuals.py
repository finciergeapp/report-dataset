import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("blood_reports_dataset.csv")

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set style for plots
sns.set_theme(style="whitegrid")

# 1. Infection Trends over Time
plt.figure(figsize=(12, 6))
infection_df = df[df['Diagnosis'].isin(['Bacterial infection', 'Viral infection'])]
infection_counts = infection_df.groupby('Date').size().reset_index(name='count')
sns.lineplot(data=infection_counts, x='Date', y='count')
plt.title('Daily Infection Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.tight_layout()
plt.savefig('infection_trends.png')
plt.close()

# 2. Anemia Distribution by Age and Gender
plt.figure(figsize=(12, 6))
anemia_df = df[df['Diagnosis'] == 'Anemia']
sns.histplot(data=anemia_df, x='Age', hue='Gender', multiple='stack', bins=20)
plt.title('Anemia Cases Distribution by Age and Gender')
plt.xlabel('Age')
plt.ylabel('Number of Cases')
plt.tight_layout()
plt.savefig('anemia_distribution.png')
plt.close()

# 3. CRP Trends (Inflammation Spikes)
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='CRP_mg_L')
plt.title('CRP Levels Over Time')
plt.xlabel('Date')
plt.ylabel('CRP (mg/L)')
plt.tight_layout()
plt.savefig('crp_trends.png')
plt.close()

print("Static visuals generated and saved as PNG files.")