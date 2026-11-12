"""
Generate Review1_Completed_Data_Analysis.xlsx
Matches Section 13 of the Review I Technical Report
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import pandas as pd
import numpy as np
from src.preprocessing import load_raw_data, validate_data_quality, preprocess_data
from src.feature_engineering import engineer_features, verify_feature_engineering_stats
from src.eda import compute_associations, compute_combined_ranking

def generate_excel_report(output_path: str = 'Review1_Completed_Data_Analysis.xlsx'):
    raw = load_raw_data()
    clean = preprocess_data(raw)
    fe = engineer_features(clean)
    quality = validate_data_quality(raw)
    assoc_df = compute_associations(clean)
    ranking_df = compute_combined_ranking(clean)
    fe_stats = verify_feature_engineering_stats(fe)
    
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # Sheet 1: Project Metadata & Overview
        overview_data = {
            'Attribute': [
                'Project Title', 'Review Stage', 'Student Name', 'Register Number',
                'Degree / Branch', 'Institution', 'Academic Year',
                'Raw Records', 'Attributes', 'Predictor Variables', 'Target Variable',
                'Duplicate Rows Removed', 'Analysis Records (Deduplicated)',
                'Positive Class Records (Clean)', 'Negative Class Records (Clean)',
                'Missing Values', 'Conflicting Predictor Patterns'
            ],
            'Value': [
                'Diabetes Prediction System - Machine Learning Based Early-Stage Risk Prediction',
                'Review I - Technical Project Report',
                'Agarshna R', 'RA2411026050061',
                'B.Tech CSE - Artificial Intelligence & Machine Learning',
                'SRM Institute of Science and Technology, Tiruchirappalli',
                '2026-2027',
                quality['total_records'], 17, 16, 'class',
                quality['exact_duplicates'], quality['unique_records'],
                f"{quality['target_distribution']['Positive']} (68.92%)",
                f"{quality['target_distribution']['Negative']} (31.08%)",
                quality['total_missing'], quality['conflicting_patterns']
            ]
        }
        pd.DataFrame(overview_data).to_excel(writer, sheet_name='Project_Overview', index=False)
        
        # Sheet 2: Data Quality & Outlier Analysis
        age_stats = quality['age_stats']
        outlier_data = {
            'Age Statistic': [
                'Minimum', 'Q1 (25th Percentile)', 'Median (50th Percentile)',
                'Q3 (75th Percentile)', 'Maximum', 'Interquartile Range (IQR)',
                'IQR Lower Bound (Q1 - 1.5*IQR)', 'IQR Upper Bound (Q3 + 1.5*IQR)',
                'Flagged Outliers (> Upper Bound)'
            ],
            'Value': [
                age_stats['min'], age_stats['q1'], age_stats['median'],
                age_stats['q3'], age_stats['max'], age_stats['iqr'],
                age_stats['lower_bound'], age_stats['upper_bound'],
                age_stats['flagged_outliers']
            ],
            'Handling Decision': [
                'Valid clinical observation retained',
                'Quartile threshold',
                'Distribution midpoint',
                'Quartile threshold',
                'Valid elder observation retained (Age 90)',
                'Spread measurement',
                'Theoretical screening limit',
                'Theoretical screening limit',
                'Screened; no automatic deletion performed'
            ]
        }
        pd.DataFrame(outlier_data).to_excel(writer, sheet_name='Outlier_Analysis', index=False)
        
        # Sheet 3: Encoding Scheme
        encoding_data = {
            'Variable Group': ['Gender', 'Symptom / Risk Indicators (14)', 'Target Class', 'Age'],
            'Original Representation': ['Female / Male', 'No / Yes', 'Negative / Positive', 'Integer / Numeric'],
            'Encoded Representation': ['Female=0, Male=1', 'No=0, Yes=1', 'Negative=0, Positive=1', 'Retained Numeric'],
            'Clinical / Modeling Note': [
                'Binary demographic factor',
                'Questionnaire symptom indicators',
                'Early-stage diabetes risk status',
                'Continuous numerical predictor'
            ]
        }
        pd.DataFrame(encoding_data).to_excel(writer, sheet_name='Encoding_Scheme', index=False)
        
        # Sheet 4: Feature Associations (Table 7.1)
        assoc_df.to_excel(writer, sheet_name='Feature_Associations', index=False)
        
        # Sheet 5: Combined Exploratory Ranking (Table 9.1)
        ranking_df.to_excel(writer, sheet_name='Combined_Ranking', index=False)
        
        # Sheet 6: Feature Engineering Summary (Table 8.1)
        fe_summary = [
            {
                'Engineered Feature': 'Symptom_Count',
                'Construction': 'Sum of 14 symptom/risk indicators',
                'Purpose': 'Overall number of reported symptom/risk indicators',
                'Min': fe_stats['Symptom_Count']['min'],
                'Max': fe_stats['Symptom_Count']['max'],
                'Mean': fe_stats['Symptom_Count']['mean'],
                'Median': fe_stats['Symptom_Count']['median']
            },
            {
                'Engineered Feature': 'Core_Symptom_Score',
                'Construction': 'Sum of Polyuria, Polydipsia, sudden weight loss, Polyphagia, weakness',
                'Purpose': 'Compact score for selected core metabolic symptom group',
                'Min': fe_stats['Core_Symptom_Score']['min'],
                'Max': fe_stats['Core_Symptom_Score']['max'],
                'Mean': fe_stats['Core_Symptom_Score']['mean'],
                'Median': fe_stats['Core_Symptom_Score']['median']
            },
            {
                'Engineered Feature': 'Associated_Symptom_Score',
                'Construction': 'Sum of Genital thrush, visual blurring, Itching, Irritability, delayed healing, partial paresis, muscle stiffness, Alopecia, Obesity',
                'Purpose': 'Captures remaining associated secondary symptom burden',
                'Min': fe_stats['Associated_Symptom_Score']['min'],
                'Max': fe_stats['Associated_Symptom_Score']['max'],
                'Mean': fe_stats['Associated_Symptom_Score']['mean'],
                'Median': fe_stats['Associated_Symptom_Score']['median']
            }
        ]
        pd.DataFrame(fe_summary).to_excel(writer, sheet_name='Feature_Engineering', index=False)
        
        # Sheet 7: Clean Preprocessed Data (251 rows)
        clean.to_excel(writer, sheet_name='Cleaned_Preprocessed_Data', index=False)
        
        # Sheet 8: Feature Engineered Data (251 rows + 3 features)
        fe.to_excel(writer, sheet_name='Feature_Engineered_Data', index=False)

    print(f"Successfully generated Excel artifact at {output_path}")

if __name__ == '__main__':
    generate_excel_report()

