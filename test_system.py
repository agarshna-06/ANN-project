"""
Comprehensive System Verification Test
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import os
import sys
import json
import joblib
import pandas as pd
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.abspath('src'))
sys.path.insert(0, os.path.abspath('.'))

def test_all():
    print("=" * 70)
    print("COMPREHENSIVE PROJECT INTEGRITY & VERIFICATION AUDIT")
    print("=" * 70)

    # 1. Datasets
    print("\n1. Verifying Datasets...")
    datasets = [
        'data/diabetes_data_upload.csv',
        'data/diabetes_raw_copy.csv',
        'data/diabetes_cleaned_preprocessed.csv',
        'data/diabetes_feature_engineered.csv'
    ]
    for f in datasets:
        assert os.path.exists(f), f"Missing {f}"
        df = pd.read_csv(f)
        print(f"  [PASS] {f}: Shape={df.shape}, Size={os.path.getsize(f)} bytes")

    # 2. Excel Artifact
    print("\n2. Verifying Excel Technical Report Artifact...")
    excel_file = 'Review1_Completed_Data_Analysis.xlsx'
    assert os.path.exists(excel_file), f"Missing {excel_file}"
    xl = pd.ExcelFile(excel_file)
    print(f"  [PASS] {excel_file} loaded successfully with {len(xl.sheet_names)} sheets:")
    for s in xl.sheet_names:
        print(f"         - {s}")

    # 3. Figures
    print("\n3. Verifying All 8 EDA Figures...")
    for i in range(1, 9):
        matches = [f for f in os.listdir('figures') if f.startswith(f"0{i}")]
        assert len(matches) > 0, f"Missing Figure 0{i}"
        fig_path = os.path.join('figures', matches[0])
        print(f"  [PASS] Figure 0{i}: {matches[0]} ({os.path.getsize(fig_path)} bytes)")

    # 4. Saved Models & CV Results
    print("\n4. Verifying Trained Model Artifacts...")
    assert os.path.exists('saved_models/best_model.pkl')
    assert os.path.exists('saved_models/scaler.pkl')
    assert os.path.exists('saved_models/model_summary.json')
    assert os.path.exists('saved_models/cv_model_comparison.csv')
    cv_df = pd.read_csv('saved_models/cv_model_comparison.csv')
    print(f"  [PASS] Model comparison results verified ({len(cv_df)} model-feature configurations evaluated).")

    # 5. Model Inference, SHAP Attribution & What-If Simulation
    print("\n5. Verifying Model Inference, SHAP Explanations & What-If Engine...")
    from src.explainability import DiabetesExplainer
    explainer = DiabetesExplainer()
    test_patient = {
        'Age': 52, 'Gender': 1, 'Polyuria': 1, 'Polydipsia': 1,
        'sudden weight loss': 1, 'weakness': 1, 'Polyphagia': 1,
        'Genital thrush': 0, 'visual blurring': 1, 'Itching': 0,
        'Irritability': 1, 'delayed healing': 0, 'partial paresis': 1,
        'muscle stiffness': 0, 'Alopecia': 0, 'Obesity': 1
    }
    pred_cls, pred_prob = explainer.predict_patient_risk(test_patient)
    explanation = explainer.explain_patient(test_patient)
    whatif = explainer.simulate_what_if(test_patient, {'Polyuria': 0, 'Polydipsia': 0})
    
    print(f"  [PASS] Single Patient Risk Inference: {pred_prob*100:.1f}% ({'High Risk' if pred_cls==1 else 'Low Risk'})")
    print(f"  [PASS] Local Attribution Baseline Prior: {explanation['base_value']*100:.1f}%")
    print(f"  [PASS] Top Positive Contributor: {explanation['attributions'].iloc[0]['Feature']} (+{explanation['attributions'].iloc[0]['Attribution']:.3f})")
    print(f"  [PASS] What-If Counterfactual (Resolving Polyuria & Polydipsia): {pred_prob*100:.1f}% -> {whatif['modified_probability']*100:.1f}% (Delta: {whatif['delta_percent']:.1f}%)")

    # 6. Jupyter Notebook Verification
    print("\n6. Verifying Jupyter Notebook...")
    nb_path = 'notebooks/diabetes_prediction_complete.ipynb'
    assert os.path.exists(nb_path), f"Missing {nb_path}"
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb_json = json.load(f)
    print(f"  [PASS] {nb_path}: {len(nb_json.get('cells', []))} cells verified.")

    # 7. Web Application (Streamlit)
    print("\n7. Verifying Streamlit Web Application (app.py)...")
    from streamlit.testing.v1 import AppTest
    at = AppTest.from_file('app.py', default_timeout=30)
    at.run()
    assert not at.exception, f"Streamlit exception: {at.exception}"
    print(f"  [PASS] Streamlit app.py successfully rendered {len(at.tabs)} interactive tabs:")
    for idx, t in enumerate(at.tabs):
        print(f"         {idx+1}. {t.label}")

    print("\n" + "=" * 70)
    print("ALL 7 SYSTEM AUDIT CHECKS PASSED WITH 100% SUCCESS!")
    print("THE PROJECT IS FULLY OPERATIONAL AND READY FOR SUBMISSION!")
    print("=" * 70)

if __name__ == '__main__':
    test_all()

