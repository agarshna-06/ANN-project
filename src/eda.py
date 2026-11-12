"""
Exploratory Data Analysis and Figure Generation Module
Reproduces Figures 1-8 and Tables 7.1 & 9.1 from Review I Report
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, pointbiserialr
from sklearn.feature_selection import mutual_info_classif
from sklearn.ensemble import RandomForestClassifier

# Set clean matplotlib style
plt.style.use('default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.autolayout'] = True

FIG_DIR = 'figures'

def compute_associations(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Compute Cramer's V with Yates' continuity correction for binary indicators and point-biserial for Age."""
    records = []
    n = len(df_clean)
    y = df_clean['class']
    
    # 1. Age (point-biserial)
    pb_corr, pb_p = pointbiserialr(df_clean['Age'], y)
    records.append({
        'Feature': 'Age',
        'Measure': 'Point-Biserial',
        'Association': abs(pb_corr),
        'Signed_Value': pb_corr,
        'p_value': pb_p
    })
    
    # 2. Categorical features (Cramer's V)
    cat_cols = [c for c in df_clean.columns if c not in ['Age', 'class', 'Symptom_Count', 'Core_Symptom_Score', 'Associated_Symptom_Score']]
    for col in cat_cols:
        cm = pd.crosstab(df_clean[col], y)
        chi2, p, _, _ = chi2_contingency(cm, correction=True)
        v = np.sqrt(chi2 / n)
        records.append({
            'Feature': col,
            'Measure': "Cramer's V",
            'Association': v,
            'Signed_Value': v,
            'p_value': p
        })
        
    res = pd.DataFrame(records).sort_values(by='Association', ascending=False).reset_index(drop=True)
    return res

def compute_mutual_information(df_clean: pd.DataFrame, random_state: int = 42) -> pd.Series:
    """Compute mutual information between predictors and binary target."""
    feature_cols = [c for c in df_clean.columns if c not in ['class', 'Symptom_Count', 'Core_Symptom_Score', 'Associated_Symptom_Score']]
    X = df_clean[feature_cols]
    y = df_clean['class']
    mi = mutual_info_classif(X, y, random_state=random_state)
    return pd.Series(mi, index=feature_cols).sort_values(ascending=False)

def compute_rf_importance(df_clean: pd.DataFrame, random_state: int = 42) -> pd.Series:
    """Compute Gini feature importance using Random Forest."""
    feature_cols = [c for c in df_clean.columns if c not in ['class', 'Symptom_Count', 'Core_Symptom_Score', 'Associated_Symptom_Score']]
    X = df_clean[feature_cols]
    y = df_clean['class']
    rf = RandomForestClassifier(n_estimators=100, random_state=random_state)
    rf.fit(X, y)
    return pd.Series(rf.feature_importances_, index=feature_cols).sort_values(ascending=False)

def compute_combined_ranking(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Generate Table 9.1 Combined Exploratory Ranking."""
    assoc_df = compute_associations(df_clean).set_index('Feature')
    mi_s = compute_mutual_information(df_clean)
    rf_s = compute_rf_importance(df_clean)
    
    features = mi_s.index.tolist()
    records = []
    for f in features:
        a_val = assoc_df.loc[f, 'Association']
        mi_val = mi_s[f]
        rf_val = rf_s[f]
        records.append({
            'Feature': f,
            'Association': a_val,
            'Mutual_Information': mi_val,
            'RF_Importance': rf_val
        })
    df_rank = pd.DataFrame(records)
    
    # Ranks (1 = best)
    df_rank['Rank_Assoc'] = df_rank['Association'].rank(ascending=False)
    df_rank['Rank_MI'] = df_rank['Mutual_Information'].rank(ascending=False)
    df_rank['Rank_RF'] = df_rank['RF_Importance'].rank(ascending=False)
    df_rank['Mean_Rank'] = (df_rank['Rank_Assoc'] + df_rank['Rank_MI'] + df_rank['Rank_RF']) / 3.0
    
    return df_rank.sort_values(by='Mean_Rank').reset_index(drop=True)

# ----------------- PLOT GENERATION FUNCTIONS -----------------

def plot_fig1_target_distribution(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/01_target_class_distribution.png'):
    """Figure 1: Target Class Distribution."""
    counts = df_clean['class'].value_counts()
    labels = ['Negative', 'Positive']
    values = [counts.get(0, 0), counts.get(1, 0)]
    
    fig, ax = plt.subplots(figsize=(7, 5.5), dpi=300)
    bars = ax.bar(labels, values, width=0.45, color='#1f77b4', edgecolor='none')
    ax.set_ylabel('Number of records', fontsize=12)
    ax.set_xlabel('Class', fontsize=12)
    ax.set_title('Target Class Distribution', fontsize=14, pad=12)
    ax.set_ylim(0, 180)
    for b in bars:
        height = b.get_height()
        ax.annotate(f'{height}',
                    xy=(b.get_x() + b.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig2_age_distribution(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/02_age_distribution.png'):
    """Figure 2: Distribution of Participant Age."""
    fig, ax = plt.subplots(figsize=(7.5, 6), dpi=300)
    ax.hist(df_clean['Age'], bins=15, color='#1f77b4', edgecolor='#1f77b4')
    ax.set_xlabel('Age', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Age Distribution', fontsize=14, pad=12)
    ax.set_xlim(13, 93)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig3_symptom_prevalence(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/03_symptom_prevalence.png'):
    """Figure 3: Overall Prevalence of Symptom/Risk Indicators."""
    binary_cols = [
        'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness',
        'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching',
        'Irritability', 'delayed healing', 'partial paresis',
        'muscle stiffness', 'Alopecia', 'Obesity'
    ]
    prevalences = {col: (df_clean[col].mean() * 100) for col in binary_cols}
    s = pd.Series(prevalences).sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    ax.barh(s.index, s.values, height=0.5, color='#1f77b4')
    ax.set_xlabel('Percentage of records with Yes (%)', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.set_title('Prevalence of Binary Symptom/Risk Features', fontsize=14, pad=12)
    ax.set_xlim(0, 67)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig4_feature_associations(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/04_feature_target_association.png'):
    """Figure 4: Exploratory Feature-Target Association."""
    assoc_df = compute_associations(df_clean)
    # Sort ascending for horizontal bar chart
    s = assoc_df.sort_values(by='Association', ascending=True)
    
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    ax.barh(s['Feature'], s['Association'], height=0.6, color='#1f77b4')
    ax.set_xlabel('Association magnitude / signed coefficient', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.set_title('Feature-Target Association', fontsize=14, pad=12)
    ax.set_xlim(0.0, 0.65)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig5_correlation_matrix(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/05_correlation_matrix.png'):
    """Figure 5: Correlation Matrix of Encoded Variables."""
    base_cols = [
        'Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
        'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
        'Itching', 'Irritability', 'delayed healing', 'partial paresis',
        'muscle stiffness', 'Alopecia', 'Obesity', 'class'
    ]
    corr = df_clean[base_cols].corr()
    
    fig, ax = plt.subplots(figsize=(9, 8), dpi=300)
    cax = ax.matshow(corr, cmap='viridis', vmin=-0.3, vmax=1.0)
    fig.colorbar(cax, label='Correlation', fraction=0.046, pad=0.04)
    
    ax.set_xticks(range(len(base_cols)))
    ax.set_yticks(range(len(base_cols)))
    ax.set_xticklabels(base_cols, rotation=90, fontsize=8)
    ax.set_yticklabels(base_cols, fontsize=8)
    ax.set_title('Correlation Matrix of Encoded Variables', fontsize=13, pad=20)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig6_engineered_features(df_fe: pd.DataFrame, save_path: str = f'{FIG_DIR}/06_engineered_features_distribution.png'):
    """Figure 6: Distributions of Engineered Symptom Scores."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), dpi=300)
    
    # 1. Symptom_Count
    axes[0].hist(df_fe['Symptom_Count'], bins=range(0, 16), align='left', color='#1f77b4', edgecolor='#1f77b4')
    axes[0].set_title('Symptom_Count', fontsize=12)
    axes[0].set_xlabel('Score', fontsize=10)
    axes[0].set_ylabel('Frequency', fontsize=10)
    
    # 2. Core_Symptom_Score
    axes[1].hist(df_fe['Core_Symptom_Score'], bins=range(0, 7), align='left', color='#1f77b4', edgecolor='#1f77b4')
    axes[1].set_title('Core_Symptom_Score', fontsize=12)
    axes[1].set_xlabel('Score', fontsize=10)
    axes[1].set_ylabel('Frequency', fontsize=10)
    
    # 3. Associated_Symptom_Score
    axes[2].hist(df_fe['Associated_Symptom_Score'], bins=range(0, 10), align='left', color='#1f77b4', edgecolor='#1f77b4')
    axes[2].set_title('Associated_Symptom_Score', fontsize=12)
    axes[2].set_xlabel('Score', fontsize=10)
    axes[2].set_ylabel('Frequency', fontsize=10)
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig7_mutual_information(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/07_mutual_information_ranking.png'):
    """Figure 7: Exploratory Mutual Information Ranking."""
    mi = compute_mutual_information(df_clean).sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    ax.barh(mi.index, mi.values, height=0.6, color='#1f77b4')
    ax.set_xlabel('Mutual information', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.set_title('Exploratory Mutual Information Ranking', fontsize=14, pad=12)
    ax.set_xlim(0.0, 0.27)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_fig8_rf_importance(df_clean: pd.DataFrame, save_path: str = f'{FIG_DIR}/08_random_forest_importance.png'):
    """Figure 8: Exploratory Random Forest Feature Importance."""
    rf_imp = compute_rf_importance(df_clean).sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    ax.barh(rf_imp.index, rf_imp.values, height=0.6, color='#1f77b4')
    ax.set_xlabel('Random Forest importance', fontsize=12)
    ax.set_ylabel('Feature', fontsize=12)
    ax.set_title('Exploratory Random Forest Feature Importance', fontsize=14, pad=12)
    ax.set_xlim(0.0, 0.26)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def generate_all_plots(df_clean: pd.DataFrame, df_fe: pd.DataFrame):
    """Generate all 8 project figures matching Review I report."""
    os.makedirs(FIG_DIR, exist_ok=True)
    print("Generating Figure 1: Target Class Distribution...")
    plot_fig1_target_distribution(df_clean)
    print("Generating Figure 2: Age Distribution...")
    plot_fig2_age_distribution(df_clean)
    print("Generating Figure 3: Symptom Prevalence...")
    plot_fig3_symptom_prevalence(df_clean)
    print("Generating Figure 4: Feature-Target Associations...")
    plot_fig4_feature_associations(df_clean)
    print("Generating Figure 5: Correlation Matrix...")
    plot_fig5_correlation_matrix(df_clean)
    print("Generating Figure 6: Engineered Features Distribution...")
    plot_fig6_engineered_features(df_fe)
    print("Generating Figure 7: Mutual Information...")
    plot_fig7_mutual_information(df_clean)
    print("Generating Figure 8: Random Forest Importance...")
    plot_fig8_rf_importance(df_clean)
    print("All figures successfully saved in figures/ directory!")

if __name__ == '__main__':
    from preprocessing import load_raw_data, preprocess_data
    from feature_engineering import engineer_features
    
    raw = load_raw_data()
    clean = preprocess_data(raw)
    fe = engineer_features(clean)
    generate_all_plots(clean, fe)

