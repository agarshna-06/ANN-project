import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

os.makedirs('report_figures', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# Figure 2: Proposed EDL Framework
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Box helper
def draw_box(x, y, w, h, text, bg, border='#002855', fontsize=9, bold=True):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=bg, ec=border, lw=1.5)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, fontweight='bold' if bold else 'normal', color='#000000')

# Left Column: Datasets
draw_box(0.5, 7.8, 3.8, 1.8, "Diabetes Datasets\n\n• Dataset I: PIMA-IDD-I (768)\n• Dataset II: DDFH-G (2000)\n• Dataset III: IDPD-I (1000)\n• Dataset IV: UCI Early-Stage (520)", "#bbf7d0", "#16a34a", 8.5)

# Right Column: Data Preprocessing
draw_box(5.5, 7.8, 4.0, 1.8, "Data Preprocessing\n\n• Duplicate Elimination & Quality Check\n• Imputation of Biological Zeros\n• MinMax / StandardScaler Normalization\n• SMOTE Synthetic Minority Balancing", "#bae6fd", "#0284c7", 8.5)

# Middle: Feature Selection
draw_box(2.8, 6.3, 4.4, 0.9, "Feature Selection via Extra Tree Classifier (ETC)\n(Gini Relevance & Clinical Feature Scoring)", "#fef08a", "#ca8a04", 9)

# Data Splitting
draw_box(2.0, 4.9, 2.8, 0.8, "Training Data (80%)\n(Stratified 5-Fold CV)", "#fed7aa", "#ea580c", 8.5)
draw_box(5.2, 4.9, 2.8, 0.8, "Testing Data (20%)\n(Unseen Blind Evaluation)", "#fecdd3", "#e11d48", 8.5)

# Base Models
draw_box(1.0, 3.2, 8.0, 1.1, "Base-Level Deep Learning Models\n\nANN (Multilayer Dense)  |  LSTM (Sequential Recurrent)  |  1D-CNN (Local Feature Convolution)", "#e9d5ff", "#9333ea", 9)

# Meta Stacking
draw_box(1.0, 1.6, 8.0, 1.1, "Meta-Level Stacking Ensemble Models (EDL)\n\nStack-ANN (Dense Meta)  |  Stack-LSTM (Sequential Meta)  |  Stack-CNN (Conv Meta)", "#fed7aa", "#c2410c", 9)

# Final Prediction & Metrics
draw_box(1.0, 0.2, 3.8, 1.0, "Model Evaluation Metrics\nAccuracy, Precision, Specificity,\nSensitivity, F1-Score, MCC, ROC/AUC", "#ddd6fe", "#7c3aed", 8)
draw_box(5.2, 0.2, 3.8, 1.0, "Final Clinical Decision Output\nEarly Diabetes Risk Assessment\n(Diabetic / Non-Diabetic / Pre-Diabetic)", "#a7f3d0", "#059669", 8.5)

# Connecting Arrows
arrows = [
    ((4.3, 8.7), (5.5, 8.7)),
    ((7.5, 7.8), (6.0, 7.2)),
    ((5.0, 6.3), (5.0, 5.7)),
    ((3.4, 4.9), (3.4, 4.3)),
    ((5.0, 3.2), (5.0, 2.7)),
    ((5.0, 1.6), (5.0, 1.2))
]
for p1, p2 in arrows:
    ax.annotate('', xy=p2, xytext=p1, arrowprops=dict(facecolor='#002855', edgecolor='#002855', width=1.5, headwidth=6))

plt.title("FIGURE 2. Proposed Ensemble Deep Learning (EDL) Framework", fontsize=11, fontweight='bold', pad=10, color='#002855')
plt.tight_layout()
plt.savefig('report_figures/fig02_edl_framework.png', dpi=200)
plt.close()

# Figure 3: Stack-ANN Framework
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')
draw_box(0.5, 3.5, 2.5, 1.0, "Clinical Indicators\nInput Vector (X)", "#e0f2fe", "#0284c7", 8.5)
draw_box(3.5, 3.7, 1.8, 0.6, "Base ANN", "#f3e8ff", "#9333ea", 8)
draw_box(3.5, 2.9, 1.8, 0.6, "Base LSTM", "#f3e8ff", "#9333ea", 8)
draw_box(3.5, 2.1, 1.8, 0.6, "Base 1D-CNN", "#f3e8ff", "#9333ea", 8)
draw_box(5.8, 2.3, 1.8, 2.0, "Stack-ANN Meta Model\n\n• Dense (32, ReLU)\n• Dropout (0.5)\n• Dense (1 / 3, Sigm/SM)", "#ffedd5", "#ea580c", 8)
draw_box(8.0, 2.8, 1.7, 1.0, "Final Risk\nPrediction", "#dcfce7", "#16a34a", 8.5)

ax.annotate('', xy=(3.5, 4.0), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(3.5, 3.2), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(3.5, 2.4), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 3.2), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 2.4), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(8.0, 3.3), xytext=(7.6, 3.3), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))

plt.title("FIGURE 3. Proposed EDL-Based Stack-ANN Architecture", fontsize=10.5, fontweight='bold', pad=8, color='#002855')
plt.tight_layout()
plt.savefig('report_figures/fig03_stack_ann.png', dpi=200)
plt.close()

# Figure 4: Stack-LSTM Framework
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')
draw_box(0.5, 3.5, 2.5, 1.0, "Clinical Indicators\nInput Vector (X)", "#e0f2fe", "#0284c7", 8.5)
draw_box(3.5, 3.7, 1.8, 0.6, "Base ANN", "#f3e8ff", "#9333ea", 8)
draw_box(3.5, 2.9, 1.8, 0.6, "Base LSTM", "#f3e8ff", "#9333ea", 8)
draw_box(3.5, 2.1, 1.8, 0.6, "Base 1D-CNN", "#f3e8ff", "#9333ea", 8)
draw_box(5.8, 2.1, 1.9, 2.4, "Stack-LSTM Meta Model\n\n• Reshape (Time Steps)\n• LSTM (64, ReLU)\n• Dense (32, ReLU)\n• Dense (Sigmoid/SM)", "#ffedd5", "#ea580c", 8)
draw_box(8.1, 2.8, 1.6, 1.0, "Final Risk\nPrediction", "#dcfce7", "#16a34a", 8.5)

ax.annotate('', xy=(3.5, 4.0), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(3.5, 3.2), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(3.5, 2.4), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 3.2), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 2.4), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(8.1, 3.3), xytext=(7.7, 3.3), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))

plt.title("FIGURE 4. Proposed EDL-Based Stack-LSTM Architecture", fontsize=10.5, fontweight='bold', pad=8, color='#002855')
plt.tight_layout()
plt.savefig('report_figures/fig04_stack_lstm.png', dpi=200)
plt.close()

# Figure 5: Stack-CNN Framework
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')
draw_box(0.5, 3.5, 2.5, 1.0, "Clinical Indicators\nInput Vector (X)", "#e0f2fe", "#0284c7", 8.5)
draw_box(3.5, 3.7, 1.8, 0.6, "Base ANN", "#f3e8ff", "#9333ea", 8)
draw_box(3.5, 2.9, 1.8, 0.6, "Base LSTM", "#f3e8ff", "#9333ea", 8)
draw_box(3.5, 2.1, 1.8, 0.6, "Base 1D-CNN", "#f3e8ff", "#9333ea", 8)
draw_box(5.8, 2.0, 1.9, 2.6, "Stack-CNN Meta Model\n\n• Conv1D (32, K=3)\n• MaxPooling1D (P=2)\n• Flatten()\n• Dense (64, ReLU)\n• Dense (Sigmoid/SM)", "#ffedd5", "#ea580c", 7.5)
draw_box(8.1, 2.8, 1.6, 1.0, "Final Risk\nPrediction", "#dcfce7", "#16a34a", 8.5)

ax.annotate('', xy=(3.5, 4.0), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(3.5, 3.2), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(3.5, 2.4), xytext=(3.0, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 4.0), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 3.2), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(5.8, 3.3), xytext=(5.3, 2.4), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))
ax.annotate('', xy=(8.1, 3.3), xytext=(7.7, 3.3), arrowprops=dict(facecolor='#002855', width=1.2, headwidth=5))

plt.title("FIGURE 5. Proposed EDL-Based Stack-CNN Architecture", fontsize=10.5, fontweight='bold', pad=8, color='#002855')
plt.tight_layout()
plt.savefig('report_figures/fig05_stack_cnn.png', dpi=200)
plt.close()

# Figure 19: CDSS Web Deployment Architecture
fig, ax = plt.subplots(figsize=(9.5, 4.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.5)
ax.axis('off')

draw_box(0.3, 1.5, 2.0, 1.8, "Client Layer\n\n• Web Browser UI\n• Streamlit Dashboard\n• Bootstrap 5.3 Portal\n• Mobile Responsive", "#e0f2fe", "#0284c7", 8)
draw_box(2.7, 1.5, 2.2, 1.8, "Application Engine\n\n• Python Fast Inference\n• Feature Preprocessor\n• MinMax / Scaler Engine\n• XAI SHAP Explainer", "#fef3c7", "#d97706", 8)
draw_box(5.3, 1.5, 2.2, 1.8, "Inference Core\n\n• Stacking Ensemble\n• Base ANN/LSTM/CNN\n• Meta Stack-ANN\n• What-If Counterfactual", "#f3e8ff", "#9333ea", 8)
draw_box(7.9, 1.5, 1.8, 1.8, "Output & Logs\n\n• Risk Score Meter\n• SHAP Attribution\n• Clinical Audit Log\n• Excel / PDF Export", "#dcfce7", "#16a34a", 8)

ax.annotate('', xy=(2.7, 2.4), xytext=(2.3, 2.4), arrowprops=dict(facecolor='#002855', width=1.5, headwidth=6))
ax.annotate('', xy=(5.3, 2.4), xytext=(4.9, 2.4), arrowprops=dict(facecolor='#002855', width=1.5, headwidth=6))
ax.annotate('', xy=(7.9, 2.4), xytext=(7.5, 2.4), arrowprops=dict(facecolor='#002855', width=1.5, headwidth=6))

plt.title("FIGURE 19. Clinical Decision Support System (CDSS) End-to-End Deployment Architecture", fontsize=10.5, fontweight='bold', pad=8, color='#002855')
plt.tight_layout()
plt.savefig('report_figures/fig19_cdss_architecture.png', dpi=200)
plt.close()

print('Architectural figures generated!')
