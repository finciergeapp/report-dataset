import pandas as pd
import numpy as np
from faker import Faker

# Setup
fake = Faker()
num_records = 10000  # Temporarily reduced for development. Will be increased to 1,000,000 for final dataset.

def random_range(mean, std, low, high):
    """Generate a realistic random value bounded within range"""
    val = np.random.normal(mean, std)
    return float(np.clip(val, low, high))

# Prepare dataset list
data = []

for i in range(num_records):
    gender = np.random.choice(['M', 'F'])
    age = np.random.randint(5, 80)
    
    # Base normal physiology ranges
    hb = random_range(14 if gender=='M' else 12.5, 2, 7, 18)
    tlc = random_range(7500, 2000, 4000, 15000)
    poly = random_range(55, 15, 20, 80)
    lymph = random_range(40, 10, 15, 80)
    eos = random_range(2, 1.5, 0, 8)
    mono = random_range(3, 2, 0, 10)
    platelets = random_range(2.8, 0.7, 1.0, 5.0)
    hct = hb * 3
    mcv = random_range(85, 8, 60, 110)
    mch = random_range(29, 3, 20, 36)
    mchc = random_range(32, 2, 26, 36)
    crp = abs(random_range(4, 8, 0, 80))  # inflammation marker
    
    # Simple diagnostic rule-based labels
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

    abnormal = "Yes" if diagnosis != "Normal" else "No"
    
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

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("blood_reports_dataset.csv", index=False)

print("✅ CSV generated successfully: blood_reports_dataset.csv")
print(df.head())
