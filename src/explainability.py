"""
Explainable AI (XAI) Module: Additive Tree Attribution (Tree-SHAP) and What-If Counterfactual Engine
Implements Section 12 of the Review I Technical Project Report
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any

class DiabetesExplainer:
    """
    Provides local additive Shapley feature attributions (Tree-SHAP / Saabas path method)
    and patient-level counterfactual what-if analysis for early-stage diabetes risk.
    Guarantees: Baseline_Probability + Sum(Local_Attributions) = Predicted_Probability
    """
    def __init__(self, model_path: str = 'saved_models/best_model.pkl', 
                 scaler_path: str = 'saved_models/scaler.pkl', 
                 features_path: str = 'saved_models/model_feature_names.pkl'):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.feature_names = joblib.load(features_path)

    def predict_patient_risk(self, patient_dict: Dict[str, Any]) -> Tuple[int, float]:
        """
        Predict early-stage diabetes risk class and probability for an individual patient.
        Returns: (predicted_class [0 or 1], risk_probability [0.0 - 1.0])
        """
        df_row = pd.DataFrame([patient_dict])[self.feature_names]
        X_scaled = self.scaler.transform(df_row)
        pred = int(self.model.predict(X_scaled)[0])
        prob = float(self.model.predict_proba(X_scaled)[0, 1])
        return pred, prob

    def explain_patient(self, patient_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compute exact local additive attribution scores for each symptom indicator.
        Positive values push risk toward Higher Risk (Positive class).
        Negative values decrease risk (Protective/Negative class).
        """
        df_row = pd.DataFrame([patient_dict])[self.feature_names]
        X_scaled = self.scaler.transform(df_row)
        
        all_contribs = np.zeros(len(self.feature_names))
        all_biases = []
        
        for estimator in self.model.estimators_:
            tree = estimator.tree_
            node_vals = tree.value[:, 0, :]
            node_probs = node_vals[:, 1] / np.maximum(node_vals.sum(axis=1), 1e-9)
            all_biases.append(node_probs[0])
            
            node_indicator = estimator.decision_path(X_scaled)
            nodes = node_indicator.indices
            for i in range(len(nodes) - 1):
                parent = nodes[i]
                child = nodes[i + 1]
                feat_idx = tree.feature[parent]
                delta = node_probs[child] - node_probs[parent]
                all_contribs[feat_idx] += delta
                
        base_value = float(np.mean(all_biases))
        contributions = all_contribs / len(self.model.estimators_)
        predicted_prob = float(self.model.predict_proba(X_scaled)[0, 1])
        
        df_attr = pd.DataFrame({
            'Feature': self.feature_names,
            'Patient_Value': [patient_dict[f] for f in self.feature_names],
            'Attribution': contributions,
            'Absolute_Impact': np.abs(contributions),
            'Direction': ['Risk Increasing (+)' if c > 0 else 'Risk Decreasing (-)' for c in contributions]
        }).sort_values(by='Absolute_Impact', ascending=False).reset_index(drop=True)
        
        return {
            'base_value': base_value,
            'predicted_probability': predicted_prob,
            'attributions': df_attr
        }

    def simulate_what_if(self, baseline_patient: Dict[str, Any], modifications: Dict[str, Any]) -> Dict[str, Any]:
        """
        Performs interactive what-if counterfactual simulation.
        Replaces selected symptom indicators and computes probability trajectory & risk delta.
        """
        modified_patient = baseline_patient.copy()
        for k, v in modifications.items():
            if k in modified_patient:
                modified_patient[k] = v
                
        base_pred, base_prob = self.predict_patient_risk(baseline_patient)
        mod_pred, mod_prob = self.predict_patient_risk(modified_patient)
        
        delta = mod_prob - base_prob
        return {
            'baseline_probability': base_prob,
            'baseline_class': 'Positive (High Risk)' if base_pred == 1 else 'Negative (Low Risk)',
            'modified_probability': mod_prob,
            'modified_class': 'Positive (High Risk)' if mod_pred == 1 else 'Negative (Low Risk)',
            'delta': delta,
            'delta_percent': delta * 100,
            'modifications': modifications
        }

    def compute_global_importance(self, df_samples: pd.DataFrame) -> pd.DataFrame:
        """
        Computes mean absolute attribution across an entire dataset population.
        """
        X_df = df_samples[self.feature_names]
        X_scaled = self.scaler.transform(X_df)
        
        all_sample_contribs = np.zeros((len(X_df), len(self.feature_names)))
        
        for estimator in self.model.estimators_:
            tree = estimator.tree_
            node_vals = tree.value[:, 0, :]
            node_probs = node_vals[:, 1] / np.maximum(node_vals.sum(axis=1), 1e-9)
            
            for row_idx in range(len(X_scaled)):
                node_indicator = estimator.decision_path(X_scaled[row_idx:row_idx+1])
                nodes = node_indicator.indices
                for i in range(len(nodes) - 1):
                    parent = nodes[i]
                    child = nodes[i + 1]
                    feat_idx = tree.feature[parent]
                    all_sample_contribs[row_idx, feat_idx] += (node_probs[child] - node_probs[parent])
                    
        all_sample_contribs /= len(self.model.estimators_)
        mean_abs_impact = np.mean(np.abs(all_sample_contribs), axis=0)
        
        df_global = pd.DataFrame({
            'Feature': self.feature_names,
            'Mean_Absolute_SHAP': mean_abs_impact
        }).sort_values(by='Mean_Absolute_SHAP', ascending=False).reset_index(drop=True)
        
        return df_global

if __name__ == '__main__':
    explainer = DiabetesExplainer()
    sample = {
        'Age': 45, 'Gender': 1, 'Polyuria': 1, 'Polydipsia': 1,
        'sudden weight loss': 1, 'weakness': 1, 'Polyphagia': 0,
        'Genital thrush': 0, 'visual blurring': 0, 'Itching': 1,
        'Irritability': 1, 'delayed healing': 1, 'partial paresis': 0,
        'muscle stiffness': 0, 'Alopecia': 0, 'Obesity': 1
    }
    pred, prob = explainer.predict_patient_risk(sample)
    print(f"Prediction: {pred} (Probability: {prob*100:.1f}%)")
    
    explanation = explainer.explain_patient(sample)
    print("Baseline prior:", round(explanation['base_value'], 4))
    print(explanation['attributions'].head(6))
    
    whatif = explainer.simulate_what_if(sample, {'Polyuria': 0, 'Polydipsia': 0})
    print(f"What-If: {whatif['baseline_probability']*100:.1f}% -> {whatif['modified_probability']*100:.1f}% (Delta: {whatif['delta_percent']:.1f}%)")
