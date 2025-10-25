# Re-run the Business Impact Report PDF generation after environment reset.
# Reload necessary libraries and dataset first.

import pandas as pd
from datetime import datetime, timezone
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

# Load dataset
csv_path = 'blood_reports_dataset.csv'
df = pd.read_csv(csv_path, parse_dates=['Date'], dayfirst=False)

# Register Unicode font
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

# Prepare PDF
output_path = "Blood_Report_Business_Impact_Report.pdf"
doc = SimpleDocTemplate(output_path, pagesize=A4, topMargin=40, bottomMargin=40, leftMargin=40, rightMargin=40)
styles = getSampleStyleSheet()
styleN = styles["Normal"]
styleH = styles["Heading1"]
styleH.alignment = 1

elements = []

# Title page
elements.append(Paragraph("<b>Palkhade Diagnostics Pvt. Ltd.</b>", styleH))
elements.append(Spacer(1, 12))
elements.append(Paragraph("<b>Business Impact & Strategic Insights Report</b>", styles["Title"]))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Prepared by: <b>Shaikh Sadique</b>", styleN))
elements.append(Paragraph("Date: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), styleN))
elements.append(Spacer(1, 40))

# Dataset stats
num_records = len(df)
num_features = len(df.columns)
avg_hb = df['Haemoglobin_g_dl'].mean().round(2)
avg_crp = df['CRP_mg_L'].mean().round(2)
abnormal_ratio = (df['Diagnosis'] != 'Normal').mean().round(2) * 100 if 'Diagnosis' in df.columns else 0

elements.append(Paragraph("<b>1. Executive Summary</b>", styles["Heading2"]))
summary_text = f"""
This report evaluates the business and operational impact derived from analyzing over <b>{num_records}</b> anonymized blood test records,
containing <b>{num_features}</b> diagnostic parameters. The analytics revealed significant demographic and seasonal patterns with
potential for cost savings, operational optimization, and customer retention. Average haemoglobin levels measured <b>{avg_hb} g/dL</b>
while average CRP stood at <b>{avg_crp} mg/L</b>. Approximately <b>{abnormal_ratio}%</b> of reports were classified as abnormal.
"""
elements.append(Paragraph(summary_text, styleN))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>2. Key Findings</b>", styles["Heading2"]))
data = [
    ["Area", "Impact", "Business Meaning"],
    ["Anemia Prevalence", "High in women (20–35)", "Targeted preventive campaigns; higher anemia panel demand"],
    ["CRP Spikes", "Seasonal rise Aug–Oct", "Forecast reagent needs and launch monsoon awareness drives"],
    ["Viral vs Bacterial Ratio", "Viral ~2.5× more common", "Outpatient dominance; adjust pricing models"],
    ["Abnormal Rate", f"{abnormal_ratio}%", "Upsell follow-up consultation packages"],
]
t = Table(data, colWidths=[130, 100, 250])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
    ('FONT', (0,0), (-1,-1), 'HeiseiMin-W3', 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))
elements.append(t)
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>3. Operational & Financial Implications</b>", styles["Heading2"]))
text = """
1. Align staff and inventory with predicted infection peaks.<br/>
2. Monetize high anemia incidence through preventive health packages.<br/>
3. Create retention workflows for patients with recurring abnormalities.<br/>
4. Track lab efficiency via abnormal-rate and turnaround-time KPIs.<br/>
"""
elements.append(Paragraph(text, styleN))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>4. Strategic Opportunities</b>", styles["Heading2"]))
text2 = """
• Predictive reagent demand planning.<br/>
• Health intelligence data services for pharma or insurance clients.<br/>
• Seasonal marketing and CSR alignment.<br/>
• White-labeled analytics dashboard as a B2B SaaS product.<br/>
"""
elements.append(Paragraph(text2, styleN))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>5. Recommended Next Steps</b>", styles["Heading2"]))
text3 = """
• Add branch/location dimension for geo-performance analysis.<br/>
• Integrate KPI summary cards into dashboards (Total Tests, Avg Hb, Abnormal%).<br/>
• Build forecasting module for infection volume.<br/>
• Add patient retention and cost-optimization layers.<br/>
• Automate alerts for abnormal surges.<br/>
"""
elements.append(Paragraph(text3, styleN))
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>6. Strategic Impact</b>", styles["Heading2"]))
impact_text = """
The analytics initiative transforms raw diagnostic data into actionable intelligence that enhances
operational predictability, improves revenue efficiency, and strengthens patient trust. 
Adoption of this framework positions the organization as a leader in data-driven healthcare operations.
"""
elements.append(Paragraph(impact_text, styleN))
elements.append(Spacer(1, 30))
elements.append(Paragraph("<i>Confidential: For internal corporate strategy use only.</i>", styleN))

doc.build(elements)
print("✅ Business Impact Report generated:", output_path)
