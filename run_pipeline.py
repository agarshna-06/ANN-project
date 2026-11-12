"""
End-to-End Execution Pipeline for Diabetes Prediction System
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import os
import sys
import subprocess

# Ensure src is in python path
sys.path.insert(0, os.path.abspath('src'))
sys.path.insert(0, os.path.abspath('.'))

def main():
    print("=" * 70)
    print("SRM INSTITUTE OF SCIENCE AND TECHNOLOGY - CSE (AIML)")
    print("DIABETES PREDICTION SYSTEM: END-TO-END EXECUTION PIPELINE")
    print("Student: Agarshna R | Register No: RA2411026050061")
    print("=" * 70)
    
    # Step 1: Preprocessing
    print("\n[Step 1/5] Running Data Validation and Preprocessing...")
    from src.preprocessing import load_raw_data, validate_data_quality, preprocess_data
    raw = load_raw_data()
    quality = validate_data_quality(raw)
    print(f"  - Raw Records: {quality['total_records']}, Duplicates Removed: {quality['exact_duplicates']}")
    print(f"  - Deduplicated Clean Records: {quality['unique_records']}")
    clean = preprocess_data(raw)
    clean.to_csv('data/diabetes_cleaned_preprocessed.csv', index=False)
    print("  -> Saved: data/diabetes_cleaned_preprocessed.csv")
    
    # Step 2: Feature Engineering
    print("\n[Step 2/5] Running Feature Engineering...")
    from src.feature_engineering import engineer_features, verify_feature_engineering_stats
    fe = engineer_features(clean)
    stats = verify_feature_engineering_stats(fe)
    for col, s in stats.items():
        print(f"  - {col}: min={s['min']}, max={s['max']}, mean={s['mean']}, median={s['median']}")
    fe.to_csv('data/diabetes_feature_engineered.csv', index=False)
    print("  -> Saved: data/diabetes_feature_engineered.csv")
    
    # Step 3: EDA & Figures
    print("\n[Step 3/5] Generating Review I Figures (01 to 08)...")
    from src.eda import generate_all_plots
    generate_all_plots(clean, fe)
    
    # Step 4: Excel Workbook Artifact
    print("\n[Step 4/5] Generating Review1_Completed_Data_Analysis.xlsx...")
    from generate_excel_artifact import generate_excel_report
    generate_excel_report()
    
    # Step 5: Model Training & CV
    print("\n[Step 5/5] Running Stratified CV across 8 Models & 6 Feature Sets...")
    from src.modeling import evaluate_models_cross_validation, train_and_save_best_model
    cv_df = evaluate_models_cross_validation(fe, n_splits=5)
    cv_df.to_csv('saved_models/cv_model_comparison.csv', index=False)
    best_row = cv_df.sort_values(by=['ROC_AUC', 'F1_Score'], ascending=[False, False]).iloc[0]
    best_fs = best_row['Feature_Set']
    best_m = best_row['Model']
    print(f"  - Top Performing Model: {best_m} on {best_fs} (ROC-AUC: {best_row['ROC_AUC']:.4f})")
    train_and_save_best_model(fe, feature_set_id=best_fs, model_name=best_m)
    
    print("\n" + "=" * 70)
    print("ALL PIPELINE STAGES COMPLETED SUCCESSFULLY!")
    print("Launch the interactive Web App with: streamlit run app.py")
    print("=" * 70)

if __name__ == '__main__':
    main()

