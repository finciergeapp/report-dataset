"""Module for building and evaluating a predictive model on the blood reports dataset.

This module loads the blood reports dataset, preprocesses it by encoding categorical
features, splits the data into training and testing sets, trains a RandomForestClassifier,
and evaluates its performance using accuracy and a classification report.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

def run_predictive_analytics(file_path: str = "data/blood_reports_dataset.csv") -> None:
    """Runs the predictive analytics pipeline on the blood reports dataset.

    Args:
        file_path (str): The path to the blood reports CSV file.
    """
    # Load the dataset
    df = pd.read_csv(file_path)

    # Drop irrelevant columns for prediction
    df = df.drop(columns=['Report_ID', 'Date', 'Abnormal_Flag'])

    # Encode categorical features
    le_gender = LabelEncoder()
    df['Gender'] = le_gender.fit_transform(df['Gender'])

    le_diagnosis = LabelEncoder()
    df['Diagnosis'] = le_diagnosis.fit_transform(df['Diagnosis'])

    # Define features (X) and target (y)
    X = df.drop(columns=['Diagnosis'])
    y = df['Diagnosis']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a RandomForestClassifier model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=le_diagnosis.classes_))

if __name__ == '__main__':
    run_predictive_analytics()