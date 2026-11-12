"""
Machine Learning Modeling, Cross-Validation, and Evaluation Module
Implements all 8 model families across 6 experimental feature sets (FS-1 to FS-6)
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import json
import joblib
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Any

from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.calibration import calibration_curve

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

# Metrics
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix, brier_score_loss
)

from src.feature_engineering import get_feature_sets

def get_model_catalog(random_state: int = 42) -> Dict[str, Any]:
    """Returns the 8 candidate supervised learning models described in Section 11."""
    return {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=random_state),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
        'Naive Bayes': GaussianNB(),
        'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=random_state),
        'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=6, random_state=random_state),
        'Support Vector Machine': SVC(probability=True, kernel='rbf', C=1.0, random_state=random_state),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=random_state),
        'Artificial Neural Network': MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=800, alpha=0.01, random_state=random_state)
    }

def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray) -> Dict[str, float]:
    """Calculate all 9 clinical evaluation metrics from Section 11.1."""
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred, zero_division=0) # Sensitivity
    spec = tn / (tn + fp) if (tn + fp) > 0 else 0.0     # Specificity
    f1 = f1_score(y_true, y_pred, zero_division=0)
    
    try:
        roc_auc = roc_auc_score(y_true, y_prob)
    except Exception:
        roc_auc = 0.5
        
    try:
        pr_auc = average_precision_score(y_true, y_prob)
    except Exception:
        pr_auc = 0.5
        
    brier = brier_score_loss(y_true, y_prob)
    
    return {
        'Accuracy': float(acc),
        'Precision': float(prec),
        'Recall': float(rec),
        'Specificity': float(spec),
        'F1_Score': float(f1),
        'ROC_AUC': float(roc_auc),
        'PR_AUC': float(pr_auc),
        'Brier_Score': float(brier),
        'TN': int(tn),
        'FP': int(fp),
        'FN': int(fn),
        'TP': int(tp)
    }

def evaluate_models_cross_validation(df_fe: pd.DataFrame, n_splits: int = 5, random_state: int = 42) -> pd.DataFrame:
    """
    Run leakage-safe Stratified K-Fold cross validation across all 8 models and all 6 feature sets.
    StandardScaler is fitted strictly inside each training fold.
    """
    feature_sets = get_feature_sets()
    models = get_model_catalog(random_state)
    y = df_fe['class'].values
    
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    
    results = []
    
    for fs_id, fs_info in feature_sets.items():
        feat_cols = fs_info['features']
        X = df_fe[feat_cols].values
        
        for model_name, model_inst in models.items():
            fold_metrics = []
            
            for train_idx, val_idx in skf.split(X, y):
                X_train, X_val = X[train_idx], X[val_idx]
                y_train, y_val = y[train_idx], y[val_idx]
                
                # Strict leakage control: Fit scaler on training fold only
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_val_scaled = scaler.transform(X_val)
                
                # Clone/fit model
                from sklearn.base import clone
                clf = clone(model_inst)
                clf.fit(X_train_scaled, y_train)
                
                y_pred = clf.predict(X_val_scaled)
                if hasattr(clf, "predict_proba"):
                    y_prob = clf.predict_proba(X_val_scaled)[:, 1]
                else:
                    y_prob = clf.decision_function(X_val_scaled)
                    y_prob = 1 / (1 + np.exp(-y_prob))
                    
                m = calculate_metrics(y_val, y_pred, y_prob)
                fold_metrics.append(m)
                
            # Average across folds
            avg_m = {k: np.mean([fm[k] for fm in fold_metrics]) for k in fold_metrics[0]}
            std_acc = np.std([fm['Accuracy'] for fm in fold_metrics])
            std_f1 = np.std([fm['F1_Score'] for fm in fold_metrics])
            std_roc = np.std([fm['ROC_AUC'] for fm in fold_metrics])
            
            results.append({
                'Feature_Set': fs_id,
                'Feature_Set_Name': fs_info['name'],
                'Num_Features': len(feat_cols),
                'Model': model_name,
                'Accuracy': round(avg_m['Accuracy'], 4),
                'Accuracy_Std': round(std_acc, 4),
                'Precision': round(avg_m['Precision'], 4),
                'Recall': round(avg_m['Recall'], 4),
                'Specificity': round(avg_m['Specificity'], 4),
                'F1_Score': round(avg_m['F1_Score'], 4),
                'F1_Std': round(std_f1, 4),
                'ROC_AUC': round(avg_m['ROC_AUC'], 4),
                'ROC_AUC_Std': round(std_roc, 4),
                'PR_AUC': round(avg_m['PR_AUC'], 4),
                'Brier_Score': round(avg_m['Brier_Score'], 4)
            })
            
    return pd.DataFrame(results)

def train_and_save_best_model(df_fe: pd.DataFrame, feature_set_id: str = 'FS-5', model_name: str = 'Random Forest', random_state: int = 42) -> Dict[str, Any]:
    """
    Trains the optimal selected model with leakage-safe holdout split, saves artifacts to saved_models/.
    """
    feature_sets = get_feature_sets()
    feat_cols = feature_sets[feature_set_id]['features']
    
    X = df_fe[feat_cols]
    y = df_fe['class']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, stratify=y, random_state=random_state
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    models = get_model_catalog(random_state)
    clf = models[model_name]
    clf.fit(X_train_scaled, y_train)
    
    y_pred = clf.predict(X_test_scaled)
    y_prob = clf.predict_proba(X_test_scaled)[:, 1]
    
    test_metrics = calculate_metrics(y_test.values, y_pred, y_prob)
    
    # Save model and artifacts
    joblib.dump(clf, 'saved_models/best_model.pkl')
    joblib.dump(scaler, 'saved_models/scaler.pkl')
    joblib.dump(feat_cols, 'saved_models/model_feature_names.pkl')
    
    # Calibration curve data
    prob_true, prob_pred = calibration_curve(y_test, y_prob, n_bins=5)
    calibration_data = {
        'prob_true': prob_true.tolist(),
        'prob_pred': prob_pred.tolist()
    }
    
    summary = {
        'model_name': model_name,
        'feature_set_id': feature_set_id,
        'feature_set_name': feature_sets[feature_set_id]['name'],
        'feature_names': feat_cols,
        'num_features': len(feat_cols),
        'test_metrics': test_metrics,
        'calibration_data': calibration_data
    }
    
    with open('saved_models/model_summary.json', 'w') as f:
        json.dump(summary, f, indent=4)
        
    print(f"Trained & Saved Best Model: {model_name} on {feature_set_id}")
    print(f"Test Accuracy: {test_metrics['Accuracy']:.4f}, ROC-AUC: {test_metrics['ROC_AUC']:.4f}, F1: {test_metrics['F1_Score']:.4f}")
    
    return summary

if __name__ == '__main__':
    from preprocessing import load_raw_data, preprocess_data
    from feature_engineering import engineer_features
    
    raw = load_raw_data()
    clean = preprocess_data(raw)
    fe = engineer_features(clean)
    
    print("Running Stratified 5-Fold Cross-Validation across 8 models and 6 feature sets (48 experiments)...")
    cv_df = evaluate_models_cross_validation(fe, n_splits=5)
    cv_df.to_csv('saved_models/cv_model_comparison.csv', index=False)
    print("Top 10 Models by ROC-AUC:")
    print(cv_df.sort_values(by='ROC_AUC', ascending=False)[['Feature_Set', 'Model', 'Accuracy', 'Recall', 'Specificity', 'F1_Score', 'ROC_AUC', 'Brier_Score']].head(10))
    
    # Train and save the best model
    best_row = cv_df.sort_values(by=['ROC_AUC', 'F1_Score'], ascending=[False, False]).iloc[0]
    best_fs = best_row['Feature_Set']
    best_m = best_row['Model']
    train_and_save_best_model(fe, feature_set_id=best_fs, model_name=best_m)

