"""
Data Preprocessing Module for Diabetes Prediction System
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict, Any

# Column definitions
FEATURE_COLUMNS = [
    'Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
    'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
    'Itching', 'Irritability', 'delayed healing', 'partial paresis',
    'muscle stiffness', 'Alopecia', 'Obesity'
]

BINARY_SYMPTOMS = [
    'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness',
    'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching',
    'Irritability', 'delayed healing', 'partial paresis',
    'muscle stiffness', 'Alopecia', 'Obesity'
]

TARGET_COLUMN = 'class'

def load_raw_data(filepath: str = 'data/diabetes_data_upload.csv') -> pd.DataFrame:
    """Load the raw dataset and verify its expected dimensions."""
    df = pd.read_csv(filepath)
    if df.shape[1] != 17:
        raise ValueError(f"Expected 17 columns, found {df.shape[1]}")
    return df

def validate_data_quality(df: pd.DataFrame) -> Dict[str, Any]:
    """Inspect missing values, duplicates, and category integrity."""
    missing_counts = df.isnull().sum().to_dict()
    total_missing = sum(missing_counts.values())
    exact_duplicates = int(df.duplicated().sum())
    
    # Check conflicting predictor combinations
    df_dedup = df.drop_duplicates()
    predictor_dups = df_dedup.duplicated(subset=FEATURE_COLUMNS).sum()
    
    target_dist = df_dedup[TARGET_COLUMN].value_counts().to_dict()
    
    # Age outlier analysis using standard IQR
    age = df_dedup['Age'].dropna()
    q1 = float(age.quantile(0.25))
    median = float(age.median())
    q3 = float(age.quantile(0.75))
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = int(((age < lower_bound) | (age > upper_bound)).sum())
    
    return {
        'total_records': len(df),
        'unique_records': len(df_dedup),
        'exact_duplicates': exact_duplicates,
        'total_missing': total_missing,
        'conflicting_patterns': int(predictor_dups),
        'target_distribution': target_dist,
        'age_stats': {
            'min': int(age.min()),
            'q1': q1,
            'median': median,
            'q3': q3,
            'max': int(age.max()),
            'iqr': iqr,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'flagged_outliers': outliers
        }
    }

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove exact duplicate rows and encode categorical variables to binary indicators:
      - Gender: Female=0, Male=1
      - Symptom/risk indicators: No=0, Yes=1
      - Target: Negative=0, Positive=1
      - Age: numerical
    """
    df_clean = df.drop_duplicates().copy()
    
    # Encode Gender
    df_clean['Gender'] = df_clean['Gender'].map({'Female': 0, 'Male': 1}).astype(int)
    
    # Encode binary symptom features
    for col in BINARY_SYMPTOMS:
        df_clean[col] = df_clean[col].map({'No': 0, 'Yes': 1}).astype(int)
        
    # Encode target
    if TARGET_COLUMN in df_clean.columns:
        df_clean[TARGET_COLUMN] = df_clean[TARGET_COLUMN].map({'Negative': 0, 'Positive': 1}).astype(int)
        
    df_clean['Age'] = pd.to_numeric(df_clean['Age'])
    
    return df_clean

if __name__ == '__main__':
    raw = load_raw_data()
    print("Raw Data Loaded:", raw.shape)
    quality = validate_data_quality(raw)
    print("Quality Report:", quality)
    clean = preprocess_data(raw)
    print("Preprocessed Data:", clean.shape)
    clean.to_csv('data/diabetes_cleaned_preprocessed.csv', index=False)
    print("Saved clean data to data/diabetes_cleaned_preprocessed.csv")

