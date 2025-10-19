# Blood Report Analytics Project

This project demonstrates a comprehensive data analysis workflow for synthetic blood test reports, covering data generation, exploratory data analysis (EDA), interactive visualization dashboards, and predictive analytics.

## Project Overview

The goal of this project is to simulate a real-world scenario of analyzing medical data to derive insights and build predictive models. The workflow includes:

1.  **Data Generation**: Creation of a synthetic dataset mimicking blood test reports with various health parameters and diagnoses.
2.  **Exploratory Data Analysis (EDA)**: In-depth analysis of the generated data to understand its characteristics, identify patterns, and detect anomalies.
3.  **Interactive Visualization Dashboards**: Development of a web-based dashboard using Plotly Dash for interactive exploration of key metrics and trends.
4.  **Predictive Analytics**: Implementation of a machine learning model to predict diagnoses based on blood test parameters.
5.  **Professional Reporting**: Generation of a comprehensive PDF report summarizing the project's findings, visualizations, and model performance.

## Features

*   **Synthetic Data Generation**: `reporteda.py` generates a dataset of 1,000,000 synthetic blood test records.
*   **Data Preprocessing**: Scripts for cleaning and preparing data for analysis.
*   **Statistical Summary**: `eda.py` provides summary statistics, outlier detection, and correlation matrices.
*   **Interactive Dashboards**: `dashboard.py` offers interactive visualizations for:
    *   Infection Trends over Time
    *   Anemia Distribution by Age/Gender
    *   CRP Trends to monitor inflammation spikes
*   **Machine Learning Model**: `predictive_analytics.py` implements a Random Forest Classifier for diagnosis prediction with high accuracy.
*   **Automated Reporting**: `generate_report.py` creates a professional PDF report with executive summary, EDA insights, visuals, and model summary.

## Project Structure

```
.
├── Blood_Report_Analytics_Report.pdf
├── anemia_distribution.png
├── blood_reports_dataset.csv
├── client.md
├── crp_trends.png
├── dashboard.py
├── eda.py
├── executive_summary.md
├── generate_report.py
├── generate_visuals.py
├── infection_trends.png
├── predictive_analytics.py
└── reporteda.py
```

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Generate the dataset**:
    ```bash
    python reporteda.py
    ```
    *Note: This will generate a large dataset (1,000,000 records) and may take some time. For quicker testing, you can temporarily reduce `num_records` in `reporteda.py`.*

2.  **Perform Exploratory Data Analysis (EDA)**:
    ```bash
    python eda.py
    ```

3.  **Generate Visuals for Report**:
    ```bash
    python generate_visuals.py
    ```

4.  **Run the Interactive Dashboard**:
    ```bash
    python dashboard.py
    ```
    Open your web browser and navigate to `http://127.0.0.1:8050/` to view the dashboard.

5.  **Run Predictive Analytics Model**:
    ```bash
    python predictive_analytics.py
    ```

6.  **Generate the PDF Report**:
    ```bash
    python generate_report.py
    ```
    This will create `Blood_Report_Analytics_Report.pdf` in the project directory.

## Technologies Used

*   Python
*   Pandas
*   NumPy
*   Faker
*   Plotly Dash
*   Scikit-learn
*   Matplotlib
*   Seaborn
*   ReportLab

## Contact

For any questions or inquiries, please contact Shaikh sadique/ x.com https://x.com/Shaikh_Sadique3?t=TxxFnePvzEl-YZPOSpQ3iQ&s=08 .