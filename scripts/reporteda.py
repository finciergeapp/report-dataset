"""Module for generating synthetic blood report data.

This module uses the Faker library to create a synthetic dataset of blood reports,
including various blood parameters, patient demographics, and diagnostic flags.
The generated data is saved as a CSV file.
"""

import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating realistic-looking data
fake = Faker()

# Define the number of records to generate for the dataset
num_records = 10000  # Temporarily reduced for development. Will be increased to 1,000,000 for final dataset.

def generate_random_bounded_value(mean: float, std: float, low: float, high: float) -> float:
    """Generates a realistic random value from a normal distribution, bounded within a specified range.

    Args:
        mean (float): The mean of the normal distribution.
        std (float): The standard deviation of the normal distribution.
        low (float): The lower bound for the generated value.
        high (float): The upper bound for the generated value.

    Returns:
        float: A random value within the specified bounds.
    """
    val = np.random.normal(mean, std)
    return float(np.clip(val, low, high))

def generate_blood_report_data(num_records: int = 10000) -> pd.DataFrame:
    """Generates a synthetic blood report dataset.

    Args:
        num_records (int): The number of records to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the synthetic blood report data.
    """
    fake = Faker()
    data = []

    for i in range(num_records):
        gender = np.random.choice(['M', 'F'])
        age = np.random.randint(5, 80)
        
        # Simulate various blood parameters with realistic ranges
        hb = generate_random_bounded_value(14 if gender=='M' else 12.5, 2, 7, 18)  # Haemoglobin (g/dL)
        tlc = generate_random_bounded_value(7500, 2000, 4000, 15000)  # Total Leukocyte Count (per cumm)
        poly = generate_random_bounded_value(55, 15, 20, 80)  # Polymorphs (%)
        lymph = generate_random_bounded_value(40, 10, 15, 80)  # Lymphocytes (%)
        eos = generate_random_bounded_value(2, 1.5, 0, 8)  # Eosinophils (%)
        mono = generate_random_bounded_value(3, 2, 0, 10)  # Monocytes (%)
        platelets = generate_random_bounded_value(2.8, 0.7, 1.0, 5.0)  # Platelets (lakh/cumm)
        hct = hb * 3  # Hematocrit (%)
        mcv = generate_random_bounded_value(85, 8, 60, 110)  # Mean Corpuscular Volume (fl)
        mch = generate_random_bounded_value(29, 3, 20, 36)  # Mean Corpuscular Hemoglobin (pg)
        mchc = generate_random_bounded_value(32, 2, 26, 36)  # Mean Corpuscular Hemoglobin Concentration (g/dL)
        crp = abs(generate_random_bounded_value(4, 8, 0, 80))  # C-Reactive Protein (mg/L) - inflammation marker
        
        # Determine diagnosis based on simulated blood parameters
        if hb < 11:
            diagnosis = "Anemia"
        elif crp > 10 and tlc > 10000:
            diagnosis = "Bacterial infection"
        elif crp > 10 and lymph > 50:
            diagnosis = "Viral infection"
        elif crp > 6:
            diagnosis = "Mild inflammation"
        else:
            diagnosis = "Normal"

        # Set abnormal flag based on diagnosis
        abnormal = "Yes" if diagnosis != "Normal" else "No"
        
        # Generate synthetic blood report data for each record
        record = {
            "Report_ID": f"RPT_{i+1:05d}",
            "Date": fake.date_between(start_date='-120d', end_date='today'),
            "Gender": gender,
            "Age": age,
            "Haemoglobin_g_dl": round(hb, 1),
            "TLC_count_per_cumm": int(tlc),
            "Polymorph_%": round(poly, 1),
            "Lymphocytes_%": round(lymph, 1),
            "Eosinophils_%": round(eos, 1),
            "Monocytes_%": round(mono, 1),
            "Platelets_lakh_per_cumm": round(platelets, 2),
            "HCT_%": round(hct, 1),
            "MCV_fl": round(mcv, 1),
            "MCH_pg": round(mch, 1),
            "MCHC_g_dl": round(mchc, 1),
            "CRP_mg_L": round(crp, 1),
            "Diagnosis": diagnosis,
            "Abnormal_Flag": abnormal
        }
        data.append(record)

    # Convert the list of records into a Pandas DataFrame
    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    # Define the number of records to generate for the dataset
    num_records_to_generate = 10000  # Can be increased for a larger dataset

    # Generate the blood report data
    blood_report_df = generate_blood_report_data(num_records_to_generate)

    # Save the generated DataFrame to a CSV file in the 'data' directory
    output_path = "data/blood_reports_dataset.csv"
    blood_report_df.to_csv(output_path, index=False)

    print(f"✅ CSV generated successfully: {output_path}")
    print(blood_report_df.head())
