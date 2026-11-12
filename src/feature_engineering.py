"""
Feature Engineering Module for Diabetes Prediction System
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple

# Base feature groups
CORE_SYMPTOMS = ['Polyuria', 'Polydipsia', 'sudden weight loss', 'Polyphagia', 'weakness']
ASSOCIATED_SYMPTOMS = [
    'Genital thrush', 'visual blurring', 'Itching', 'Irritability',
    'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity'
]
ALL_SYMPTOMS = CORE_SYMPTOMS + ASSOCIATED_SYMPTOMS

ORIGINAL_16_FEATURES = [
    'Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
    'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
    'Itching', 'Irritability', 'delayed healing', 'partial paresis',
    'muscle stiffness', 'Alopecia', 'Obesity'
]

# Top selected subset based on exploratory rankings (FS-6)
SELECTED_SUBSET_FEATURES = [
    'Polyuria', 'Polydipsia', 'sudden weight loss', 'partial paresis',
    'Gender', 'Polyphagia', 'Alopecia', 'Irritability', 'Age'
]

def engineer_features(df_clean: pd.DataFrame) -> pd.DataFrame:
    """
    Construct clinically grounded aggregate symptom burden scores:
      - Symptom_Count: Sum of all 14 symptom/risk indicators (0-14)
      - Core_Symptom_Score: Sum of 5 primary diabetes symptoms (0-5)
      - Associated_Symptom_Score: Sum of 9 secondary/associated symptoms (0-9)
    """
    df = df_clean.copy()
    
    # 1. Total reported symptom count (0 to 14)
    df['Symptom_Count'] = df[ALL_SYMPTOMS].sum(axis=1)
    
    # 2. Core osmotic/metabolic symptom score (0 to 5)
    df['Core_Symptom_Score'] = df[CORE_SYMPTOMS].sum(axis=1)
    
    # 3. Associated symptom burden score (0 to 9)
    df['Associated_Symptom_Score'] = df[ASSOCIATED_SYMPTOMS].sum(axis=1)
    
    return df

def get_feature_sets() -> Dict[str, Dict[str, any]]:
    """
    Returns the 6 planned experimental feature set definitions from Section 10 of Review I:
      - FS-1: Original 16 predictors (baseline)
      - FS-2: Original + Symptom_Count
      - FS-3: Original + Core_Symptom_Score
      - FS-4: Original + Associated_Symptom_Score
      - FS-5: Original + all engineered features (19 features)
      - FS-6: Top selected feature subset
    """
    return {
        'FS-1': {
            'name': 'Original 16 Predictors',
            'features': list(ORIGINAL_16_FEATURES),
            'description': 'Baseline raw representation (16 features).'
        },
        'FS-2': {
            'name': 'Original + Symptom_Count',
            'features': ORIGINAL_16_FEATURES + ['Symptom_Count'],
            'description': 'Tests overall symptom burden feature.'
        },
        'FS-3': {
            'name': 'Original + Core_Symptom_Score',
            'features': ORIGINAL_16_FEATURES + ['Core_Symptom_Score'],
            'description': 'Tests compact core metabolic symptom information.'
        },
        'FS-4': {
            'name': 'Original + Associated_Symptom_Score',
            'features': ORIGINAL_16_FEATURES + ['Associated_Symptom_Score'],
            'description': 'Tests additional symptom grouping.'
        },
        'FS-5': {
            'name': 'Original + All Engineered Features',
            'features': ORIGINAL_16_FEATURES + ['Symptom_Count', 'Core_Symptom_Score', 'Associated_Symptom_Score'],
            'description': 'Tests combined full feature representation (19 features).'
        },
        'FS-6': {
            'name': 'Selected Subset',
            'features': list(SELECTED_SUBSET_FEATURES),
            'description': 'Tests whether fewer high-impact predictors maintain generalization.'
        }
    }

def verify_feature_engineering_stats(df_fe: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    """Verify engineered score distributions against Report Table 8.1."""
    stats = {}
    for col in ['Symptom_Count', 'Core_Symptom_Score', 'Associated_Symptom_Score']:
        s = df_fe[col]
        stats[col] = {
            'min': int(s.min()),
            'max': int(s.max()),
            'mean': round(float(s.mean()), 2),
            'median': round(float(s.median()), 2)
        }
    return stats

if __name__ == '__main__':
    from preprocessing import load_raw_data, preprocess_data
    raw = load_raw_data()
    clean = preprocess_data(raw)
    fe = engineer_features(clean)
    print("Engineered Data Shape:", fe.shape)
    stats = verify_feature_engineering_stats(fe)
    print("Engineered Stats Verification:", stats)
    fe.to_csv('data/diabetes_feature_engineered.csv', index=False)
    print("Saved feature-engineered dataset to data/diabetes_feature_engineered.csv")

