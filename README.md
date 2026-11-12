# Diabetes Prediction System
### Machine Learning Based Early-Stage Diabetes Risk Prediction
**Review I & Review II Technical Project Implementation**

- **Student Name:** Agarshna R
- **Register Number:** RA2411026050061
- **Degree / Branch:** B.Tech Computer Science and Engineering – Artificial Intelligence & Machine Learning
- **Institution:** SRM Institute of Science and Technology, Tiruchirappalli
- **Academic Year:** 2026–2027

---

## 📋 Project Overview

Diabetes mellitus is a chronic metabolic condition in which persistent abnormalities in blood glucose can lead to serious complications. Early identification of individuals at risk supports timely clinical assessment and preventive lifestyle intervention.

This project delivers a **reproducible, leakage-safe, and explainable Machine Learning framework** for early-stage diabetes risk screening based on demographic and clinical questionnaire indicators:
1. **Methodological Rigor & Duplicate Handling:** 269 exact duplicates identified in the 520 raw records and eliminated to prevent performance inflation; zero conflicting predictor patterns observed.
2. **Clinical Feature Engineering:** Formulated three interpretable aggregate symptom burden metrics:
   - `Symptom_Count` (Sum of 14 symptom indicators, 0–14)
   - `Core_Symptom_Score` (Sum of 5 primary metabolic indicators: Polyuria, Polydipsia, sudden weight loss, Polyphagia, weakness)
   - `Associated_Symptom_Score` (Sum of 9 secondary indicators)
3. **Multi-Model Benchmarking:** 8 candidate supervised learning classifiers benchmarked across 6 experimental feature sets (48 cross-validation experiments) using Stratified 5-Fold Cross-Validation.
4. **Explainable AI (XAI) & Counterfactuals:** Tree-SHAP local additive attributions and an interactive **What-If Counterfactual Simulation Engine** that calculates predicted probability trajectories when symptoms are modified.
5. **Interactive Web Application:** Full-featured Streamlit web application with real-time risk screening, local SHAP waterfall/bar explanations, what-if counterfactual exploration, model benchmarking tables, EDA galleries, and dataset export.

---

## 📂 Project Directory Structure

```text
ann_project/
│
├── data/
│   ├── diabetes_data_upload.csv            # Original raw UCI dataset (520 rows, 17 cols)
│   ├── diabetes_raw_copy.csv               # Traceable unmodified raw backup
│   ├── diabetes_cleaned_preprocessed.csv   # Deduplicated (251 rows) & encoded dataset
│   └── diabetes_feature_engineered.csv     # Clean dataset + 3 engineered symptom scores
│
├── figures/                                # EDA plots matching Review I report
│   ├── 01_target_class_distribution.png    # Figure 1: Positive (173) vs Negative (78)
│   ├── 02_age_distribution.png             # Figure 2: Age histogram (16 to 90 years)
│   ├── 03_symptom_prevalence.png           # Figure 3: Prevalence of 14 binary symptoms
│   ├── 04_feature_target_association.png   # Figure 4: Cramer's V / Point-Biserial associations
│   ├── 05_correlation_matrix.png           # Figure 5: Full 17x17 encoded correlation matrix
│   ├── 06_engineered_features_distribution.png # Figure 6: Engineered scores distributions
│   ├── 07_mutual_information_ranking.png   # Figure 7: Mutual Information ranking
│   └── 08_random_forest_importance.png     # Figure 8: Random Forest Gini feature importance
│
├── notebooks/
│   └── diabetes_prediction_complete.ipynb  # End-to-end interactive Jupyter Notebook
│
├── saved_models/
│   ├── best_model.pkl                      # Serialized top model (Random Forest Classifier)
│   ├── scaler.pkl                          # Fitted StandardScaler (leakage-safe)
│   ├── model_feature_names.pkl             # Feature column names
│   ├── model_summary.json                  # Performance summary & calibration curve data
│   └── cv_model_comparison.csv             # 48-experiment benchmark metrics
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py                    # Data validation, deduplication, encoding
│   ├── feature_engineering.py              # Symptom score formulas & 6 feature set configs
│   ├── eda.py                              # Statistical associations & figure generators
│   ├── modeling.py                         # 8 classifiers, Stratified K-Fold CV, calibration
│   └── explainability.py                   # Tree-SHAP attributions & What-If engine
│
├── Review1_Completed_Data_Analysis.xlsx    # Comprehensive 8-sheet Excel technical workbook
├── app.py                                  # Interactive Streamlit Web Application
├── index.html                              # Modern Bootstrap 5.3 Web Dashboard
├── run_bootstrap_web.bat                   # 1-click launcher for Bootstrap Web App
├── run_pipeline.py                         # Automated master execution pipeline
├── run_app.bat                             # 1-click Windows launcher for Streamlit App
├── run_pipeline.bat                        # 1-click Windows launcher for Pipeline
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## 📊 Summary of Data Preprocessing & Verification (Review I)

| Dataset Property | Value / Verification Result |
| :--- | :--- |
| **Raw Records** | 520 records, 17 columns |
| **Missing Values** | 0 across all 520 × 17 entries |
| **Duplicate Rows Removed** | 269 exact duplicates |
| **Clean Deduplicated Records** | 251 unique observations |
| **Target Distribution (Clean)** | Positive: 173 (68.92%), Negative: 78 (31.08%) |
| **Conflicting Predictor Patterns** | 0 contradictory label patterns |
| **Age Range & Outliers** | Min: 16, Q1: 39.00, Median: 48.00, Q3: 58.00, Max: 90, IQR: 19.00. 1 flagged (Age 90 - clinically valid) |
| **Categorical Encoding** | Gender: Female=0, Male=1; Symptoms: No=0, Yes=1; Class: Negative=0, Positive=1 |

---

## ⚙️ Experimental Feature Sets (Section 10)

- **FS-1:** Original 16 predictors (Baseline)
- **FS-2:** Original + `Symptom_Count`
- **FS-3:** Original + `Core_Symptom_Score`
- **FS-4:** Original + `Associated_Symptom_Score`
- **FS-5:** Original + All 3 Engineered Features (19 predictors total)
- **FS-6:** Selected Subset (Top 9 predictors: Polyuria, Polydipsia, sudden weight loss, partial paresis, Gender, Polyphagia, Alopecia, Irritability, Age)

---

## 🏆 Model Benchmarking Results (5-Fold Stratified CV)

| Model Family | Feature Set | Accuracy | Sensitivity (Recall) | Specificity | F1-Score | ROC-AUC | Brier Score |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Random Forest** | **FS-1** | **90.4%** | **94.8%** | **80.8%** | **93.2%** | **0.9720** | **0.0708** |
| Random Forest | FS-2 | 89.6% | 94.2% | 79.5% | 92.6% | 0.9714 | 0.0711 |
| Support Vector Machine (RBF) | FS-1 | 91.2% | 93.6% | 85.8% | 93.6% | 0.9696 | 0.0663 |
| Support Vector Machine (RBF) | FS-3 | 91.2% | 93.6% | 85.8% | 93.6% | 0.9693 | 0.0655 |
| Random Forest | FS-4 | 90.0% | 94.2% | 80.8% | 92.9% | 0.9698 | 0.0725 |
| Gradient Boosting | FS-1 | 89.2% | 92.5% | 82.0% | 92.1% | 0.9570 | 0.0903 |
| Artificial Neural Network (MLP) | FS-1 | 91.2% | 93.6% | 85.8% | 93.6% | 0.9620 | 0.0690 |
| Logistic Regression | FS-1 | 89.6% | 91.9% | 84.5% | 92.3% | 0.9540 | 0.0754 |
| K-Nearest Neighbors | FS-1 | 89.2% | 93.1% | 80.8% | 92.3% | 0.9420 | 0.0820 |
| Decision Tree | FS-1 | 86.8% | 90.2% | 79.5% | 90.4% | 0.8870 | 0.1280 |
| Naive Bayes (Gaussian) | FS-1 | 87.2% | 89.6% | 82.0% | 90.5% | 0.9380 | 0.0960 |

---

## 🚀 How to Run the Project

### 1. Requirements & Setup
Ensure Python 3.11+ is installed. Clone or navigate to the project directory:
```powershell
cd e:\agarshan_anna\ann_project
pip install -r requirements.txt
```

### 2. Run the Full End-to-End Pipeline
To regenerate all processed datasets, 8 EDA figures, the Excel report, and re-train all models:
```powershell
python run_pipeline.py
```
*(Or simply double-click `run_pipeline.bat` on Windows)*

### 3. Launch the Interactive Web Application
Start the Streamlit web dashboard:
```powershell
streamlit run app.py
```
*(Or simply double-click `run_app.bat` on Windows)*

The application opens automatically in your browser at `http://localhost:8501`.

### 4. Open the Jupyter Notebook
To run the interactive analysis notebook cell-by-cell:
```powershell
jupyter notebook notebooks/diabetes_prediction_complete.ipynb
```

---

## 🔬 Clinical Scope & Ethical Disclaimer
This software is developed strictly as an **academic machine learning research prototype** for early-stage diabetes risk screening based on self-reported symptoms. It does **not** provide medical diagnoses and should never replace standard laboratory investigations such as fasting plasma glucose or HbA1c testing.

