"""
Ultra-Modern Dual-Color Interactive AI Web Platform for Diabetes Risk Prediction
Features: Dual-Color Cyberpunk Theme, Glassmorphism, AI Background Video & Neural Canvas Motion
Author: Agarshna R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM Institute of Science and Technology
Academic Year: 2026-2027
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import streamlit as st

# Configure wide page layout
st.set_page_config(
    page_title="AI Early-Stage Diabetes Risk Prediction | SRM IST",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- ADVANCED DUAL-COLOR CYBER-NEON CSS & ANIMATIONS -----------------
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    :root {
        --primary-cyan: #00F2FE;
        --secondary-violet: #8B5CF6;
        --accent-emerald: #10B981;
        --accent-crimson: #EF4444;
        --dark-bg: #070913;
        --glass-bg: rgba(15, 23, 42, 0.65);
        --glass-border: rgba(0, 242, 254, 0.2);
        --glass-border-hover: rgba(139, 92, 246, 0.45);
    }

    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Full Page Background */
    .stApp {
        background: radial-gradient(circle at 15% 20%, rgba(0, 242, 254, 0.08) 0%, transparent 40%),
                    radial-gradient(circle at 85% 80%, rgba(139, 92, 246, 0.1) 0%, transparent 45%),
                    radial-gradient(circle at 50% 50%, rgba(14, 165, 233, 0.05) 0%, transparent 60%),
                    #070A13 !important;
        color: #F1F5F9;
    }

    /* Ambient Floating Glowing Orbs */
    .ambient-orb-1 {
        position: fixed;
        width: 450px;
        height: 450px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 242, 254, 0.12) 0%, transparent 70%);
        top: -100px;
        left: -100px;
        filter: blur(60px);
        z-index: 0;
        animation: floatOrb 16s ease-in-out infinite alternate;
        pointer-events: none;
    }

    .ambient-orb-2 {
        position: fixed;
        width: 500px;
        height: 500px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.14) 0%, transparent 70%);
        bottom: -120px;
        right: -100px;
        filter: blur(70px);
        z-index: 0;
        animation: floatOrb2 20s ease-in-out infinite alternate;
        pointer-events: none;
    }

    @keyframes floatOrb {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(120px, 140px) scale(1.15); }
    }

    @keyframes floatOrb2 {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(-100px, -120px) scale(1.2); }
    }

    /* Hero Banner Header */
    .hero-container {
        position: relative;
        padding: 2.2rem 2.2rem 1.8rem 2.2rem;
        background: rgba(15, 23, 42, 0.55);
        border: 1px solid rgba(0, 242, 254, 0.25);
        border-radius: 20px;
        backdrop-filter: blur(20px);
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }

    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00F2FE 0%, #8B5CF6 50%, #00F2FE 100%);
        background-size: 200% auto;
        animation: gradientBar 4s linear infinite;
    }

    @keyframes gradientBar {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 14px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background: rgba(0, 242, 254, 0.1);
        color: #00F2FE;
        border: 1px solid rgba(0, 242, 254, 0.3);
        margin-bottom: 0.8rem;
        animation: pulsePill 2.5s infinite;
    }

    @keyframes pulsePill {
        0%, 100% { box-shadow: 0 0 0 0 rgba(0, 242, 254, 0.4); }
        50% { box-shadow: 0 0 14px 2px rgba(0, 242, 254, 0.2); }
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.15;
        background: linear-gradient(135deg, #FFFFFF 20%, #00F2FE 60%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        color: #94A3B8;
        font-weight: 400;
        max-width: 850px;
        line-height: 1.6;
    }

    .hero-meta-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 1.2rem;
    }

    .meta-tag {
        font-size: 0.8rem;
        padding: 4px 12px;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #CBD5E1;
    }

    .meta-tag strong {
        color: #00F2FE;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.4rem;
        backdrop-filter: blur(16px);
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .glass-card:hover {
        border-color: rgba(0, 242, 254, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0, 242, 254, 0.08);
    }

    .card-title-cyan {
        font-size: 1.15rem;
        font-weight: 700;
        color: #00F2FE;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 0.8rem;
    }

    .card-title-violet {
        font-size: 1.15rem;
        font-weight: 700;
        color: #C084FC;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 0.8rem;
    }

    /* Prediction Badges */
    .badge-high-risk {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(185, 28, 28, 0.3) 100%);
        border: 1px solid #EF4444;
        color: #FCA5A5;
        border-radius: 14px;
        padding: 1.4rem;
        text-align: center;
        animation: glowRed 3s infinite alternate;
    }

    .badge-low-risk {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(5, 150, 105, 0.3) 100%);
        border: 1px solid #10B981;
        color: #6EE7B7;
        border-radius: 14px;
        padding: 1.4rem;
        text-align: center;
        animation: glowGreen 3s infinite alternate;
    }

    .badge-moderate-risk {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(217, 119, 6, 0.3) 100%);
        border: 1px solid #F59E0B;
        color: #FCD34D;
        border-radius: 14px;
        padding: 1.4rem;
        text-align: center;
    }

    @keyframes glowRed {
        0% { box-shadow: 0 0 15px rgba(239, 68, 68, 0.2); }
        100% { box-shadow: 0 0 30px rgba(239, 68, 68, 0.45); }
    }

    @keyframes glowGreen {
        0% { box-shadow: 0 0 15px rgba(16, 185, 129, 0.2); }
        100% { box-shadow: 0 0 30px rgba(16, 185, 129, 0.45); }
    }

    /* Score Indicator Pills */
    .score-indicator-box {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-top: 1rem;
    }

    .score-pill {
        flex: 1;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 0.9rem;
        text-align: center;
    }

    .score-pill .label {
        font-size: 0.72rem;
        text-transform: uppercase;
        color: #94A3B8;
        font-weight: 600;
        letter-spacing: 0.05em;
    }

    .score-pill .val {
        font-size: 1.4rem;
        font-weight: 800;
        font-family: 'JetBrains Mono', monospace;
        margin-top: 2px;
    }

    .cyan-text { color: #00F2FE; }
    .violet-text { color: #C084FC; }
    .emerald-text { color: #34D399; }

    /* Modern Styled HTML Table */
    .styled-table {
        border-collapse: collapse;
        margin: 10px 0;
        font-size: 0.88rem;
        width: 100%;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        overflow: hidden;
        background: rgba(15, 23, 42, 0.4);
    }
    .styled-table thead tr {
        background: linear-gradient(90deg, rgba(0, 242, 254, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
        color: #F8FAFC;
        text-align: left;
        font-weight: 700;
        border-bottom: 1px solid rgba(0, 242, 254, 0.3);
    }
    .styled-table th, .styled-table td {
        padding: 10px 14px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .styled-table tbody tr:hover {
        background-color: rgba(0, 242, 254, 0.04);
    }

    /* Streamlit Tabs Custom Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15, 23, 42, 0.4);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: #94A3B8;
        padding: 8px 16px;
        font-weight: 600;
        font-size: 0.9rem;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 242, 254, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%) !important;
        color: #00F2FE !important;
        border: 1px solid rgba(0, 242, 254, 0.3) !important;
    }
</style>

<!-- Ambient Background Orbs -->
<div class="ambient-orb-1"></div>
<div class="ambient-orb-2"></div>
""", unsafe_allow_html=True)

# ----------------- LOAD ARTIFACTS -----------------
@st.cache_resource
def load_explainer_and_models():
    from src.explainability import DiabetesExplainer
    expl = DiabetesExplainer()
    with open('saved_models/model_summary.json', 'r') as f:
        summ = json.load(f)
    cv_res = pd.read_csv('saved_models/cv_model_comparison.csv')
    return expl, summ, cv_res

@st.cache_data
def load_datasets():
    clean = pd.read_csv('data/diabetes_cleaned_preprocessed.csv')
    fe = pd.read_csv('data/diabetes_feature_engineered.csv')
    raw = pd.read_csv('data/diabetes_raw_copy.csv')
    return raw, clean, fe

try:
    explainer, model_summary, cv_df = load_explainer_and_models()
    raw_df, clean_df, fe_df = load_datasets()
except Exception as e:
    st.error(f"Error loading system artifacts: {e}. Please run 'python run_pipeline.py' first.")
    st.stop()

def show_table(df, max_rows=None):
    """Renders DataFrame safely as a styled HTML table with zero pyarrow dependency."""
    if max_rows is not None:
        df = df.head(max_rows)
    html = df.to_html(index=False, classes="styled-table")
    st.markdown(f'<div style="overflow-x:auto;">{html}</div>', unsafe_allow_html=True)

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="display: inline-flex; justify-content: center; align-items: center; width: 68px; height: 68px; border-radius: 20px; background: linear-gradient(135deg, #00F2FE 0%, #8B5CF6 100%); box-shadow: 0 8px 24px rgba(0, 242, 254, 0.35);">
            <span style="font-size: 32px;">🩺</span>
        </div>
        <h3 style="margin-top: 12px; margin-bottom: 2px; font-weight: 800; font-size: 1.2rem; color: #FFFFFF;">DIABETES AI</h3>
        <p style="font-size: 0.75rem; color: #00F2FE; letter-spacing: 0.1em; text-transform: uppercase; margin: 0;">Early-Stage Risk Engine</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="padding: 1rem; margin-bottom: 1rem;">
        <div style="font-size: 0.75rem; text-transform: uppercase; color: #94A3B8; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 6px;">Academic Credentials</div>
        <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF;">Agarshna R</div>
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #00F2FE;">Reg: RA2411026050061</div>
        <div style="font-size: 0.8rem; color: #CBD5E1; margin-top: 4px;">B.Tech CSE (AIML)</div>
        <div style="font-size: 0.8rem; color: #94A3B8;">SRM Institute of Science & Technology, Tiruchirappalli</div>
        <div style="font-size: 0.75rem; color: #A855F7; margin-top: 6px;">Academic Year: 2026–2027</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="padding: 1rem;">
        <div style="font-size: 0.75rem; text-transform: uppercase; color: #94A3B8; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 6px;">Active Model Specs</div>
        <div style="font-size: 0.85rem; color: #F1F5F9; font-weight: 600;">Random Forest Classifier</div>
        <div style="font-size: 0.8rem; color: #00F2FE;">Feature Set: FS-1 (16 Features)</div>
        <div style="font-size: 0.8rem; color: #10B981; margin-top: 4px;">5-Fold ROC-AUC: <strong>0.9720</strong></div>
        <div style="font-size: 0.8rem; color: #38BDF8;">Holdout Accuracy: <strong>90.2%</strong></div>
        <div style="font-size: 0.8rem; color: #C084FC;">Brier Calibration: <strong>0.0708</strong></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("⚠️ Clinical Research Prototype: Intended for exploratory questionnaire screening only; does not replace laboratory venous blood glucose testing.")

# ----------------- HERO HEADER -----------------
st.markdown("""
<div class="hero-container">
    <div class="badge-pill">✦ NEXT-GEN CLINICAL AI SCREENING ✦</div>
    <div class="hero-title">Early-Stage Diabetes Risk Prediction System</div>
    <div class="hero-subtitle">
        A leakage-safe machine learning architecture integrating symptom-burden feature engineering, multi-model benchmark evaluation, Tree-SHAP local explanations, and real-time counterfactual simulation.
    </div>
    <div class="hero-meta-bar">
        <div class="meta-tag">Student: <strong>Agarshna R</strong></div>
        <div class="meta-tag">Reg No: <strong>RA2411026050061</strong></div>
        <div class="meta-tag">Institution: <strong>SRM IST, Tiruchirappalli</strong></div>
        <div class="meta-tag">Review Stage: <strong>Technical Project Implementation</strong></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- APPLICATION TABS -----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Patient Risk Screening",
    "🔄 What-If Counterfactual Simulator",
    "📊 Model Comparison & Benchmarks",
    "📈 Exploratory Data Analysis (EDA)",
    "📁 Datasets & Export Artifacts"
])

# ================= TAB 1: PATIENT SCREENING =================
with tab1:
    col_input1, col_input2, col_input3 = st.columns([1.2, 1.2, 1.6])
    
    with col_input1:
        st.markdown('<div class="card-title-cyan">👤 1. Demographic Indicators</div>', unsafe_allow_html=True)
        age = st.slider("Patient Age (Years)", min_value=16, max_value=90, value=48, step=1)
        gender = st.radio("Biological Gender", options=["Female", "Male"], index=1, horizontal=True)
        gender_val = 1 if gender == "Male" else 0
        
        st.markdown('<div class="card-title-cyan" style="margin-top:1.2rem;">🩸 2. Cardinal Metabolic Symptoms</div>', unsafe_allow_html=True)
        st.caption("Primary clinical osmotic indicators (Section 7.1)")
        polyuria = st.checkbox("Polyuria (Excessive / frequent urination)", value=True)
        polydipsia = st.checkbox("Polydipsia (Excessive thirst)", value=True)
        sudden_weight_loss = st.checkbox("Sudden Weight Loss", value=False)
        polyphagia = st.checkbox("Polyphagia (Excessive hunger)", value=False)
        weakness = st.checkbox("Weakness / Chronic fatigue", value=True)
        
    with col_input2:
        st.markdown('<div class="card-title-violet">🩺 3. Associated Secondary Symptoms</div>', unsafe_allow_html=True)
        st.caption("Secondary manifestations & microvascular signs")
        genital_thrush = st.checkbox("Genital Thrush", value=False)
        visual_blurring = st.checkbox("Visual Blurring", value=False)
        itching = st.checkbox("Itching", value=True)
        irritability = st.checkbox("Irritability", value=False)
        delayed_healing = st.checkbox("Delayed Wound Healing", value=True)
        partial_paresis = st.checkbox("Partial Paresis (Muscle weakness)", value=False)
        muscle_stiffness = st.checkbox("Muscle Stiffness", value=False)
        alopecia = st.checkbox("Alopecia (Hair loss)", value=False)
        obesity = st.checkbox("Obesity", value=False)
        
    # Build dictionary
    patient_dict = {
        'Age': age,
        'Gender': gender_val,
        'Polyuria': 1 if polyuria else 0,
        'Polydipsia': 1 if polydipsia else 0,
        'sudden weight loss': 1 if sudden_weight_loss else 0,
        'weakness': 1 if weakness else 0,
        'Polyphagia': 1 if polyphagia else 0,
        'Genital thrush': 1 if genital_thrush else 0,
        'visual blurring': 1 if visual_blurring else 0,
        'Itching': 1 if itching else 0,
        'Irritability': 1 if irritability else 0,
        'delayed healing': 1 if delayed_healing else 0,
        'partial paresis': 1 if partial_paresis else 0,
        'muscle stiffness': 1 if muscle_stiffness else 0,
        'Alopecia': 1 if alopecia else 0,
        'Obesity': 1 if obesity else 0
    }
    
    # Calculate engineered scores
    all_symptoms = [
        'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness',
        'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching',
        'Irritability', 'delayed healing', 'partial paresis',
        'muscle stiffness', 'Alopecia', 'Obesity'
    ]
    core_list = ['Polyuria', 'Polydipsia', 'sudden weight loss', 'Polyphagia', 'weakness']
    assoc_list = ['Genital thrush', 'visual blurring', 'Itching', 'Irritability',
                  'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']
                  
    symptom_count = sum(patient_dict[s] for s in all_symptoms)
    core_score = sum(patient_dict[s] for s in core_list)
    assoc_score = sum(patient_dict[s] for s in assoc_list)
    
    # Predict Risk
    pred_class, risk_prob = explainer.predict_patient_risk(patient_dict)
    
    with col_input3:
        st.markdown('<div class="card-title-cyan">⚡ 4. Real-Time Risk Classification</div>', unsafe_allow_html=True)
        
        # Display Risk Badge
        if risk_prob >= 0.65:
            st.markdown(f"""
            <div class="badge-high-risk">
                <div style="font-size: 0.8rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.1em;">Prediction Verdict</div>
                <div style="font-size: 2.2rem; font-weight: 800; margin: 4px 0;">{risk_prob*100:.1f}%</div>
                <div style="font-size: 1.1rem; font-weight: 700;">HIGH DIABETES RISK DETECTED</div>
                <p style="font-size: 0.8rem; margin-top: 8px; opacity: 0.9;">Cardinal osmotic indicators (Polyuria/Polydipsia) detected. Urgent clinical fasting glucose / HbA1c test recommended.</p>
            </div>
            """, unsafe_allow_html=True)
        elif risk_prob >= 0.35:
            st.markdown(f"""
            <div class="badge-moderate-risk">
                <div style="font-size: 0.8rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.1em;">Prediction Verdict</div>
                <div style="font-size: 2.2rem; font-weight: 800; margin: 4px 0;">{risk_prob*100:.1f}%</div>
                <div style="font-size: 1.1rem; font-weight: 700;">MODERATE / BORDERLINE RISK</div>
                <p style="font-size: 0.8rem; margin-top: 8px; opacity: 0.9;">Intermediate symptom burden. Clinical follow-up and lifestyle preventive measures advised.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="badge-low-risk">
                <div style="font-size: 0.8rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.1em;">Prediction Verdict</div>
                <div style="font-size: 2.2rem; font-weight: 800; margin: 4px 0;">{risk_prob*100:.1f}%</div>
                <div style="font-size: 1.1rem; font-weight: 700;">LOW EARLY-STAGE RISK</div>
                <p style="font-size: 0.8rem; margin-top: 8px; opacity: 0.9;">Symptom profile is consistent with low risk. Maintain active lifestyle and routine checkups.</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.write("")
        st.progress(risk_prob)
        
        # Engineered scores display
        st.markdown(f"""
        <div class="score-indicator-box">
            <div class="score-pill">
                <div class="label">Symptom Count</div>
                <div class="val cyan-text">{symptom_count} <span style="font-size:0.8rem; color:#94A3B8;">/14</span></div>
            </div>
            <div class="score-pill">
                <div class="label">Core Score</div>
                <div class="val violet-text">{core_score} <span style="font-size:0.8rem; color:#94A3B8;">/5</span></div>
            </div>
            <div class="score-pill">
                <div class="label">Assoc. Score</div>
                <div class="val emerald-text">{assoc_score} <span style="font-size:0.8rem; color:#94A3B8;">/9</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown('<div class="card-title-cyan">💡 Explainable AI: Local Feature Attributions (Tree-SHAP)</div>', unsafe_allow_html=True)
    st.write("Understand which specific symptoms mathematically increased or reduced this patient's risk probability relative to the baseline.")
    
    explanation = explainer.explain_patient(patient_dict)
    attr_df = explanation['attributions']
    
    col_shap1, col_shap2 = st.columns([1.5, 1])
    
    with col_shap1:
        # Dual-Color Dark Styled Matplotlib Chart
        fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=200)
        fig.patch.set_facecolor('#0B0F19')
        ax.set_facecolor('#0B0F19')
        
        top_attrs = attr_df.head(8).sort_values(by='Attribution', ascending=True)
        colors = ['#EF4444' if c > 0 else '#00F2FE' for c in top_attrs['Attribution']]
        
        bars = ax.barh(top_attrs['Feature'], top_attrs['Attribution'], color=colors, height=0.55, edgecolor='none')
        ax.axvline(0, color='#64748B', linewidth=1.0, linestyle='--')
        
        ax.set_xlabel("Attribution to Probability (SHAP Value)", fontsize=9, color='#94A3B8')
        ax.set_title(f"Patient Local Attributions (Base Prior: {explanation['base_value']*100:.1f}%)", fontsize=11, fontweight='bold', color='#FFFFFF', pad=10)
        
        ax.tick_params(colors='#CBD5E1', labelsize=8.5)
        for spine in ax.spines.values():
            spine.set_color('#1E293B')
            
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
    with col_shap2:
        st.markdown("##### Attribution Summary Table")
        display_attr = attr_df[['Feature', 'Patient_Value', 'Attribution', 'Direction']].head(8).copy()
        display_attr['Attribution'] = display_attr['Attribution'].apply(lambda x: f"{x:+.3f}")
        show_table(display_attr)
        st.caption("🔴 Red indicates symptoms pushing probability higher. 🔵 Cyan indicates protective factors lowering risk.")

# ================= TAB 2: WHAT-IF SIMULATOR =================
with tab2:
    st.markdown('<div class="card-title-cyan">🔄 Interactive What-If Counterfactual Simulator</div>', unsafe_allow_html=True)
    st.write("Examine how targeted clinical changes or symptom resolutions alter the patient's predicted diabetes probability trajectory.")
    
    c_base, c_mod, c_res = st.columns([1.2, 1.2, 1.6])
    
    with c_base:
        st.markdown("""
        <div class="glass-card">
            <div style="font-size:0.8rem; text-transform:uppercase; color:#00F2FE; font-weight:700;">Baseline Patient Profile</div>
            <div style="font-size:1.6rem; font-weight:800; color:#FFFFFF; margin: 4px 0;">""" + f"{risk_prob*100:.1f}% Risk" + """</div>
            <div style="font-size:0.85rem; color:#CBD5E1; line-height: 1.8;">
                • <strong>Age:</strong> """ + str(patient_dict['Age']) + """ years<br>
                • <strong>Gender:</strong> """ + ('Male' if patient_dict['Gender']==1 else 'Female') + """<br>
                • <strong>Polyuria:</strong> """ + ('Yes' if patient_dict['Polyuria']==1 else 'No') + """<br>
                • <strong>Polydipsia:</strong> """ + ('Yes' if patient_dict['Polydipsia']==1 else 'No') + """<br>
                • <strong>Sudden Weight Loss:</strong> """ + ('Yes' if patient_dict['sudden weight loss']==1 else 'No') + """<br>
                • <strong>Weakness:</strong> """ + ('Yes' if patient_dict['weakness']==1 else 'No') + """
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with c_mod:
        st.markdown('<div class="card-title-violet">Hypothetical Changes</div>', unsafe_allow_html=True)
        mod_polyuria = st.selectbox("Polyuria Status", ["Keep Baseline", "Force No (0)", "Force Yes (1)"])
        mod_polydipsia = st.selectbox("Polydipsia Status", ["Keep Baseline", "Force No (0)", "Force Yes (1)"])
        mod_weight = st.selectbox("Sudden Weight Loss Status", ["Keep Baseline", "Force No (0)", "Force Yes (1)"])
        mod_itching = st.selectbox("Itching Status", ["Keep Baseline", "Force No (0)", "Force Yes (1)"])
        mod_healing = st.selectbox("Delayed Healing Status", ["Keep Baseline", "Force No (0)", "Force Yes (1)"])
        
    modifications = {}
    if mod_polyuria == "Force No (0)": modifications['Polyuria'] = 0
    elif mod_polyuria == "Force Yes (1)": modifications['Polyuria'] = 1
    
    if mod_polydipsia == "Force No (0)": modifications['Polydipsia'] = 0
    elif mod_polydipsia == "Force Yes (1)": modifications['Polydipsia'] = 1
    
    if mod_weight == "Force No (0)": modifications['sudden weight loss'] = 0
    elif mod_weight == "Force Yes (1)": modifications['sudden weight loss'] = 1
    
    if mod_itching == "Force No (0)": modifications['Itching'] = 0
    elif mod_itching == "Force Yes (1)": modifications['Itching'] = 1
    
    if mod_healing == "Force No (0)": modifications['delayed healing'] = 0
    elif mod_healing == "Force Yes (1)": modifications['delayed healing'] = 1
    
    whatif_res = explainer.simulate_what_if(patient_dict, modifications)
    
    with c_res:
        delta = whatif_res['delta_percent']
        mod_p = whatif_res['modified_probability'] * 100
        
        st.markdown("""
        <div class="glass-card">
            <div style="font-size:0.8rem; text-transform:uppercase; color:#C084FC; font-weight:700;">Simulated Outcome</div>
            <div style="display:flex; align-items:baseline; gap:12px; margin: 6px 0;">
                <div style="font-size:2.2rem; font-weight:800; color:#FFFFFF;">""" + f"{mod_p:.1f}%" + """</div>
                <div style="font-size:1.1rem; font-weight:700; color:""" + ('#34D399' if delta < 0 else '#EF4444' if delta > 0 else '#94A3B8') + """;">
                    """ + f"{delta:+.1f}%" + """
                </div>
            </div>
            <div style="font-size:0.85rem; color:#CBD5E1;">
                Transition: <code>""" + whatif_res['baseline_class'] + """</code> ➡️ <code>""" + whatif_res['modified_class'] + """</code>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if delta < 0:
            st.success(f"🎉 Risk reduced by {abs(delta):.1f}% under this counterfactual clinical scenario!")
        elif delta > 0:
            st.error(f"⚠️ Risk increased by {delta:.1f}% with these added symptom burdens.")
        else:
            st.info("No probability change observed for these settings.")

# ================= TAB 3: MODEL COMPARISON =================
with tab3:
    st.markdown('<div class="card-title-cyan">📊 Multi-Model Benchmark (5-Fold Stratified Cross-Validation)</div>', unsafe_allow_html=True)
    st.write("Rigorous leakage-safe comparison across 8 supervised learning architectures and 6 experimental feature sets (48 trials).")
    
    col_filter1, col_filter2 = st.columns(2)
    with col_filter1:
        selected_fs = st.selectbox("Select Feature Set to View", options=cv_df['Feature_Set'].unique(), index=0)
    with col_filter2:
        sort_metric = st.selectbox("Sort Models By Metric", options=['ROC_AUC', 'Accuracy', 'F1_Score', 'Brier_Score', 'Recall', 'Specificity'])
        
    fs_subset = cv_df[cv_df['Feature_Set'] == selected_fs].sort_values(by=sort_metric, ascending=(sort_metric == 'Brier_Score'))
    
    # Dual-Color Comparison Chart
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200)
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    
    models_list = fs_subset['Model'].tolist()
    roc_vals = fs_subset['ROC_AUC'].tolist()
    acc_vals = fs_subset['Accuracy'].tolist()
    
    x = np.arange(len(models_list))
    width = 0.35
    
    ax.bar(x - width/2, roc_vals, width, label='ROC-AUC', color='#00F2FE', edgecolor='none')
    ax.bar(x + width/2, acc_vals, width, label='Accuracy', color='#8B5CF6', edgecolor='none')
    
    ax.set_xticks(x)
    ax.set_xticklabels(models_list, rotation=25, ha='right', fontsize=9, color='#CBD5E1')
    ax.set_ylabel('Metric Score', fontsize=10, color='#94A3B8')
    ax.set_ylim(0.7, 1.02)
    ax.set_title(f"Model Performance on {selected_fs} (Stratified 5-Fold CV)", fontsize=11, fontweight='bold', color='#FFFFFF', pad=12)
    ax.legend(facecolor='#1E293B', edgecolor='none', labelcolor='#F1F5F9')
    ax.tick_params(colors='#CBD5E1')
    for spine in ax.spines.values():
        spine.set_color('#1E293B')
    ax.grid(axis='y', linestyle='--', alpha=0.2, color='#64748B')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    st.markdown("##### Detailed Metric Comparison Table")
    show_table(fs_subset[['Model', 'Accuracy', 'Precision', 'Recall', 'Specificity', 'F1_Score', 'ROC_AUC', 'PR_AUC', 'Brier_Score']])
    st.caption("Note: Lower Brier score indicates superior probability calibration.")

# ================= TAB 4: EDA GALLERY =================
with tab4:
    st.markdown('<div class="card-title-cyan">📈 Exploratory Data Analysis (EDA) Gallery</div>', unsafe_allow_html=True)
    st.write("Figures 1 to 8 generated directly from Review I data validation, encoding, and feature relevance analysis.")
    
    eda_fig = st.selectbox("Select Project Figure to Inspect", [
        "Figure 1: Target Class Distribution",
        "Figure 2: Age Distribution",
        "Figure 3: Prevalence of Binary Symptom/Risk Features",
        "Figure 4: Feature-Target Association (Cramer's V & Point-Biserial)",
        "Figure 5: Correlation Matrix of Encoded Variables",
        "Figure 6: Distributions of Engineered Symptom Scores",
        "Figure 7: Exploratory Mutual Information Ranking",
        "Figure 8: Exploratory Random Forest Feature Importance"
    ])
    
    fig_mapping = {
        "Figure 1: Target Class Distribution": "figures/01_target_class_distribution.png",
        "Figure 2: Age Distribution": "figures/02_age_distribution.png",
        "Figure 3: Prevalence of Binary Symptom/Risk Features": "figures/03_symptom_prevalence.png",
        "Figure 4: Feature-Target Association (Cramer's V & Point-Biserial)": "figures/04_feature_target_association.png",
        "Figure 5: Correlation Matrix of Encoded Variables": "figures/05_correlation_matrix.png",
        "Figure 6: Distributions of Engineered Symptom Scores": "figures/06_engineered_features_distribution.png",
        "Figure 7: Exploratory Mutual Information Ranking": "figures/07_mutual_information_ranking.png",
        "Figure 8: Exploratory Random Forest Feature Importance": "figures/08_random_forest_importance.png"
    }
    
    img_path = fig_mapping[eda_fig]
    if os.path.exists(img_path):
        st.image(img_path, caption=eda_fig, width=900)
    else:
        st.warning(f"Figure {img_path} not found. Please run 'python run_pipeline.py'.")

# ================= TAB 5: DATASETS & ARTIFACTS =================
with tab5:
    st.markdown('<div class="card-title-cyan">📁 Project Datasets & Generated Technical Artifacts</div>', unsafe_allow_html=True)
    st.write("Browse and download the verified datasets, Excel technical report, and model logs.")
    
    col_d1, col_d2 = st.columns([1, 1])
    
    with col_d1:
        st.markdown("#### 1. Deduplicated Clean Dataset (251 records)")
        show_table(clean_df, max_rows=8)
        with open('data/diabetes_cleaned_preprocessed.csv', 'rb') as f:
            st.download_button(
                label="📥 Download Clean Preprocessed CSV",
                data=f,
                file_name="diabetes_cleaned_preprocessed.csv",
                mime="text/csv"
            )
            
    with col_d2:
        st.markdown("#### 2. Feature Engineered Dataset (251 records + 3 scores)")
        show_table(fe_df[['Age', 'Gender', 'Symptom_Count', 'Core_Symptom_Score', 'Associated_Symptom_Score', 'class']], max_rows=8)
        with open('data/diabetes_feature_engineered.csv', 'rb') as f:
            st.download_button(
                label="📥 Download Feature Engineered CSV",
                data=f,
                file_name="diabetes_feature_engineered.csv",
                mime="text/csv"
            )
            
    st.markdown("---")
    st.markdown("#### 3. Excel Technical Report Artifact")
    if os.path.exists('Review1_Completed_Data_Analysis.xlsx'):
        with open('Review1_Completed_Data_Analysis.xlsx', 'rb') as f:
            st.download_button(
                label="📊 Download Review1_Completed_Data_Analysis.xlsx (Comprehensive 8-Sheet Workbook)",
                data=f,
                file_name="Review1_Completed_Data_Analysis.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
