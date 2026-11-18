"""
PowerPoint Generator for Diabetes Prediction EDL Project
8 Professional Widescreen Slides for Review I & II
Author: AGARSHNA R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    NAVY = RGBColor(0, 40, 85)         # #002855
    BLUE = RGBColor(0, 114, 188)       # #0072bc
    CYAN = RGBColor(0, 181, 226)       # #00b5e2
    DARK = RGBColor(15, 23, 42)        # #0f172a
    GRAY = RGBColor(100, 116, 139)     # #64748b
    LIGHT_BG = RGBColor(248, 250, 252) # #f8fafc
    WHITE = RGBColor(255, 255, 255)
    GREEN = RGBColor(16, 185, 129)     # #10b981
    CARD_BG = RGBColor(241, 245, 249)  # #f1f5f9
    BORDER_COLOR = RGBColor(226, 232, 240)

    def add_header(slide, title_text, category="RESEARCH & TECHNICAL IMPLEMENTATION"):
        # Category Tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = CYAN
        p_cat.font.name = "Arial"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY
        p_title.font.name = "Arial"

        # Dividing line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.45), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = BLUE
        line.line.color.rgb = BLUE

    def add_footer(slide, current_slide, total_slides=8):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.35))
        tf = footer_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"AGARSHNA R (RA2411026050061)  |  B.Tech CSE (AIML)  |  SRM IST Tiruchirappalli  |  Slide {current_slide} of {total_slides}"
        p.font.size = Pt(9)
        p.font.color.rgb = GRAY
        p.font.name = "Arial"

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    # Background Accent Top Bar
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.2))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = BLUE
    top_bar.line.fill.background()

    # Left Blue Brand Banner Card
    brand_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.8))
    brand_card.fill.solid()
    brand_card.fill.fore_color.rgb = NAVY
    brand_card.line.fill.background()

    # Title & Subtitle inside Brand Card
    tbox = s1.shapes.add_textbox(Inches(1.3), Inches(1.2), Inches(10.7), Inches(2.2))
    tf = tbox.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "SRM INSTITUTE OF SCIENCE AND TECHNOLOGY — B.TECH CSE (AIML)"
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = CYAN
    p0.font.name = "Arial"
    
    p1 = tf.add_paragraph()
    p1.text = "An Innovative Ensemble Deep Learning Clinical Decision Support System for Diabetes Prediction"
    p1.font.size = Pt(26)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.font.name = "Arial"
    p1.space_before = Pt(10)

    p2 = tf.add_paragraph()
    p2.text = "Review I & Review II Technical Project Implementation Defense"
    p2.font.size = Pt(14)
    p2.font.color.rgb = RGBColor(203, 213, 225)
    p2.font.name = "Arial"
    p2.space_before = Pt(8)

    # Student Info Grid Card inside Title
    info_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(3.9), Inches(10.7), Inches(2.2))
    info_card.fill.solid()
    info_card.fill.fore_color.rgb = RGBColor(15, 30, 60)
    info_card.line.color.rgb = BLUE
    info_card.line.width = Pt(1.5)

    infobox = s1.shapes.add_textbox(Inches(1.6), Inches(4.1), Inches(10.1), Inches(1.8))
    itf = infobox.text_frame
    itf.word_wrap = True

    ip1 = itf.paragraphs[0]
    ip1.text = "Candidate Details & Institutional Affiliation:"
    ip1.font.size = Pt(11)
    ip1.font.bold = True
    ip1.font.color.rgb = CYAN
    ip1.font.name = "Arial"

    ip2 = itf.add_paragraph()
    ip2.text = "• Student Name: AGARSHNA R               • Register Number: RA2411026050061"
    ip2.font.size = Pt(13)
    ip2.font.bold = True
    ip2.font.color.rgb = WHITE
    ip2.font.name = "Arial"
    ip2.space_before = Pt(4)

    ip3 = itf.add_paragraph()
    ip3.text = "• Degree / Branch: B.Tech Computer Science and Engineering (Artificial Intelligence & Machine Learning)"
    ip3.font.size = Pt(11)
    ip3.font.color.rgb = RGBColor(226, 232, 240)
    ip3.font.name = "Arial"
    ip3.space_before = Pt(3)

    ip4 = itf.add_paragraph()
    ip4.text = "• Institution: SRM Institute of Science and Technology, Tiruchirappalli Campus  |  Academic Year: 2026–2027"
    ip4.font.size = Pt(10.5)
    ip4.font.color.rgb = RGBColor(148, 163, 184)
    ip4.font.name = "Arial"
    ip4.space_before = Pt(2)

    # ==========================================
    # SLIDE 2: PROBLEM STATEMENT & MOTIVATION
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Clinical Problem Statement & Research Motivation", "Clinical Context & Objectives")

    # Left Column: Problem points
    left_card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(6.5), Inches(5.0))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = CARD_BG
    left_card.line.color.rgb = BORDER_COLOR

    ltb = s2.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(6.1), Inches(4.6))
    ltf = ltb.text_frame
    ltf.word_wrap = True

    p = ltf.paragraphs[0]
    p.text = "The Global Diabetes Epidemic & Diagnostic Gaps:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = NAVY

    bullets = [
        ("Alarming Global Prevalence: ", "Over 420 million adults live with diabetes worldwide; projected to exceed 640 million by 2040. Over 50% in developing nations remain undiagnosed."),
        ("Devastating Complications: ", "Chronic hyperglycemia triggers irreversible damage: diabetic retinopathy (blindness), nephropathy (renal failure), neuropathy, and cardiovascular events."),
        ("Limitations of Current Screening: ", "Standard diagnostics (HbA1c, OGTT) are invasive, costly, and rarely taken proactively during asymptomatic early stages."),
        ("Machine Learning Research Gaps: ", "Prior studies predominantly evaluate on single small datasets (e.g., PIMA-768 only), suffer from undetected duplicate data leakage, and lack clinical explainability."),
        ("Project Mission: ", "Deliver an accurate (99%+), multi-cohort validated, leakage-safe, and explainable Deep Stacking Clinical Decision Support System.")
    ]
    for b_title, b_desc in bullets:
        bp = ltf.add_paragraph()
        bp.text = f"• {b_title}"
        bp.font.bold = True
        bp.font.size = Pt(10.5)
        bp.font.color.rgb = BLUE
        bp.space_before = Pt(6)
        
        # Add description
        run = bp.add_run()
        run.text = b_desc
        run.font.bold = False
        run.font.color.rgb = DARK

    # Right Column: Image of Types of Diabetes
    if os.path.exists("report_figures/fig01_types_of_diabetes.png"):
        s2.shapes.add_picture("report_figures/fig01_types_of_diabetes.png", Inches(7.6), Inches(1.65), width=Inches(4.9))

    add_footer(s2, 2)

    # ==========================================
    # SLIDE 3: DATASETS & PREPROCESSING RIGOR
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Multi-Cohort Datasets & Data Hygiene Rigor (Review I)", "Data Preprocessing & Validation")

    # Top Card: Datasets Grid
    top_c = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(11.733), Inches(2.2))
    top_c.fill.solid()
    top_c.fill.fore_color.rgb = CARD_BG
    top_c.line.color.rgb = BORDER_COLOR

    ttb = s3.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(11.3), Inches(2.0))
    ttf = ttb.text_frame
    ttf.word_wrap = True
    tp = ttf.paragraphs[0]
    tp.text = "Multi-Dataset Clinical Cohorts Evaluated:"
    tp.font.size = Pt(12)
    tp.font.bold = True
    tp.font.color.rgb = NAVY

    ds_lines = [
        ("Dataset I (PIMA-IDD-I): ", "768 clinical instances, 8 physiological predictors. Benchmark female cohort for international standardization."),
        ("Dataset II (DDFH-G): ", "2,000 cases from Frankfurt Hospital Germany, 8 clinical features. High statistical volume confirming deep model scalability."),
        ("Dataset III (IDPD-I): ", "1,000 Iraqi patients, 11 clinical biomarkers (HbA1c, Fasting Lipid, BMI, Cr). Multi-class diagnosis: Diabetic, Non-Diabetic, Pre-Diabetic."),
        ("Dataset IV (UCI Early-Stage): ", "520 clinical symptom questionnaire records from Sylhet Diabetes Hospital. Used for early symptom feature engineering.")
    ]
    for d_title, d_desc in ds_lines:
        p = ttf.add_paragraph()
        p.text = f"• {d_title}"
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE
        p.space_before = Pt(3)
        r = p.add_run()
        r.text = d_desc
        r.font.bold = False
        r.font.color.rgb = DARK

    # Bottom Split Cards: Duplicate Removal & Imputation
    b_left = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.05), Inches(5.7), Inches(2.6))
    b_left.fill.solid()
    b_left.fill.fore_color.rgb = RGBColor(254, 242, 242) # light red
    b_left.line.color.rgb = RGBColor(239, 68, 68)

    bl_tb = s3.shapes.add_textbox(Inches(1.0), Inches(4.15), Inches(5.3), Inches(2.4))
    bl_tf = bl_tb.text_frame
    bl_tf.word_wrap = True
    bl_p = bl_tf.paragraphs[0]
    bl_p.text = "CRITICAL AUDIT: 269 Duplicate Purge"
    bl_p.font.size = Pt(12)
    bl_p.font.bold = True
    bl_p.font.color.rgb = RGBColor(185, 28, 28)

    dup_text = [
        "• Identified 269 exact duplicate rows in the 520 raw records.",
        "• Data Leakage Hazard: If unaddressed, identical rows populate both train and test splits, producing falsely inflated test scores.",
        "• Methodological Action: Purged all 269 duplicates to leave 251 unique records with 0 contradictory predictor patterns."
    ]
    for dt in dup_text:
        p = bl_tf.add_paragraph()
        p.text = dt
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK
        p.space_before = Pt(3)

    b_right = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.05), Inches(5.733), Inches(2.6))
    b_right.fill.solid()
    b_right.fill.fore_color.rgb = RGBColor(240, 253, 244) # light green
    b_right.line.color.rgb = RGBColor(34, 197, 94)

    br_tb = s3.shapes.add_textbox(Inches(7.0), Inches(4.15), Inches(5.3), Inches(2.4))
    br_tf = br_tb.text_frame
    br_tf.word_wrap = True
    br_p = br_tf.paragraphs[0]
    br_p.text = "Imputation & Leakage-Free Scaling"
    br_p.font.size = Pt(12)
    br_p.font.bold = True
    br_p.font.color.rgb = RGBColor(21, 128, 61)

    imp_text = [
        "• Biological Zeros Imputation: Glucose, BP, SkinFold, Insulin, BMI with zero values are biologically impossible. Replaced via class-conditional median.",
        "• Stratified 5-Fold Cross-Validation: Scalers (MinMax / StandardScaler) fit exclusively on in-fold training partitions; strictly zero test leakage.",
        "• SMOTE Resampling: Synthetic oversampling applied strictly to minority training folds to rebalance Pre-Diabetic samples."
    ]
    for it in imp_text:
        p = br_tf.add_paragraph()
        p.text = it
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK
        p.space_before = Pt(3)

    add_footer(s3, 3)

    # ==========================================
    # SLIDE 4: FEATURE SELECTION & CLINICAL FEATURE ENGINEERING
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Feature Selection via ETC & Clinical Feature Engineering", "Biomarker Optimization")

    # Left: Feature Engineering (3 Scores)
    fe_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(6.0), Inches(5.0))
    fe_card.fill.solid()
    fe_card.fill.fore_color.rgb = CARD_BG
    fe_card.line.color.rgb = BORDER_COLOR

    fetb = s4.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(5.6), Inches(4.6))
    fetf = fetb.text_frame
    fetf.word_wrap = True
    fep = fetf.paragraphs[0]
    fep.text = "Novel Clinical Aggregate Biomarkers:"
    fep.font.size = Pt(13)
    fep.font.bold = True
    fep.font.color.rgb = NAVY

    scores = [
        ("1. Symptom_Count (S_count): ", "Sum of all 14 binary clinical signs (0 to 14). Captures overall symptomatic metabolic burden."),
        ("2. Core_Symptom_Score (S_core): ", "Sum of 5 cardinal osmotic/hyperglycemic signs: Polyuria + Polydipsia + Sudden Weight Loss + Polyphagia + Weakness. (Cramér's V = 0.781 — Extremely High Association)."),
        ("3. Associated_Symptom_Score (S_assoc): ", "Sum of 9 secondary sequelae (genital thrush, visual blurring, delayed healing, partial paresis, alopecia, obesity)."),
        ("6 Feature Set Experiments: ", "Evaluated FS-1 (Baseline 16) through FS-6 (All Engineered Scores) across all 8 classifiers (48 CV experiments).")
    ]
    for st, sd in scores:
        p = fetf.add_paragraph()
        p.text = f"• {st}"
        p.font.bold = True
        p.font.size = Pt(10.5)
        p.font.color.rgb = BLUE
        p.space_before = Pt(6)
        r = p.add_run()
        r.text = sd
        r.font.bold = False
        r.font.color.rgb = DARK

    # Right: Extra Tree Classifier (ETC) Feature Rankings Table
    etc_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.65), Inches(5.433), Inches(5.0))
    etc_card.fill.solid()
    etc_card.fill.fore_color.rgb = WHITE
    etc_card.line.color.rgb = BLUE
    etc_card.line.width = Pt(1.2)

    etctb = s4.shapes.add_textbox(Inches(7.3), Inches(1.85), Inches(5.0), Inches(4.6))
    etctf = etctb.text_frame
    etctf.word_wrap = True
    etcp = etctf.paragraphs[0]
    etcp.text = "Extra Tree Classifier (ETC) Feature Importance:"
    etcp.font.size = Pt(12)
    etcp.font.bold = True
    etcp.font.color.rgb = NAVY

    rankings = [
        ("1. Glucose", "0.2318 (PIMA)", "0.2413 (DDFH)", "Primary plasma glucose"),
        ("2. Age", "0.1456 (PIMA)", "0.1479 (DDFH)", "Beta-cell senescence"),
        ("3. BMI", "0.1428 (PIMA)", "0.1403 (DDFH)", "Adiposity & insulin resistance"),
        ("4. Pedigree Function", "0.1187 (PIMA)", "0.1167 (DDFH)", "Hereditary genetic score"),
        ("5. Pregnancies", "0.1057 (PIMA)", "0.1063 (DDFH)", "Gestational beta-cell stress"),
        ("6. Blood Pressure", "0.0984 (PIMA)", "0.0970 (DDFH)", "Vascular resistance"),
        ("7. Skin Thickness", "0.0814 (PIMA)", "0.0777 (DDFH)", "Subcutaneous fat reserve"),
        ("8. Insulin", "0.0757 (PIMA)", "0.0727 (DDFH)", "Endogenous secretion")
    ]
    for feat, p_sc, d_sc, note in rankings:
        p = etctf.add_paragraph()
        p.text = f"{feat}: "
        p.font.bold = True
        p.font.size = Pt(9.5)
        p.font.color.rgb = DARK
        p.space_before = Pt(3)
        r = p.add_run()
        r.text = f"{p_sc} | {d_sc} ({note})"
        r.font.bold = False
        r.font.color.rgb = GRAY

    add_footer(s4, 4)

    # ==========================================
    # SLIDE 5: ENSEMBLE DEEP LEARNING (EDL) ARCHITECTURE
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Proposed Ensemble Deep Learning (EDL) Stacking Framework", "Deep Learning & Meta-Architecture")

    # Left: Architecture Description
    arch_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(5.8), Inches(5.0))
    arch_card.fill.solid()
    arch_card.fill.fore_color.rgb = CARD_BG
    arch_card.line.color.rgb = BORDER_COLOR

    atb = s5.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(5.4), Inches(4.6))
    atf = atb.text_frame
    atf.word_wrap = True

    ap = atf.paragraphs[0]
    ap.text = "Multi-Architecture Deep Stacking Design:"
    ap.font.size = Pt(13)
    ap.font.bold = True
    ap.font.color.rgb = NAVY

    layers_info = [
        ("Base Level Models (Diverse Extractors):", ""),
        ("• ANN (Dense Multi-Layer): ", "128 -> 64 -> 32 neurons with ReLU & Batch Normalization. Learns global continuous feature mappings."),
        ("• 1D-CNN (Convolutional): ", "32 filters (kernel k=3), MaxPool1D (p=2), Dense 64. Extracts localized receptive field interactions across adjacent biomarkers."),
        ("• LSTM (Recurrent Memory): ", "64 LSTM memory units with forget, input, and output gates. Models cumulative sequential stress trajectories."),
        ("Meta-Level Models (Super Learner Stacking):", ""),
        ("• Out-of-Fold Matrix (Z): ", "Concatenates base predictions [P_ANN, P_LSTM, P_CNN] into meta-feature matrix Z."),
        ("• Stack-ANN (Optimal Meta): ", "Dense 32 (ReLU) -> Dropout (p=0.5) -> Sigmoid / Softmax. Learns non-linear blending weights across base hypotheses.")
    ]
    for lt, ld in layers_info:
        p = atf.add_paragraph()
        if ld == "":
            p.text = lt
            p.font.bold = True
            p.font.size = Pt(11)
            p.font.color.rgb = BLUE
            p.space_before = Pt(6)
        else:
            p.text = lt
            p.font.bold = True
            p.font.size = Pt(9.5)
            p.font.color.rgb = DARK
            p.space_before = Pt(2)
            r = p.add_run()
            r.text = ld
            r.font.bold = False
            r.font.color.rgb = GRAY

    # Right: Image of EDL Architecture (fig02_edl_framework.png)
    if os.path.exists("report_figures/fig02_edl_framework.png"):
        s5.shapes.add_picture("report_figures/fig02_edl_framework.png", Inches(6.8), Inches(1.65), width=Inches(5.733))

    add_footer(s5, 5)

    # ==========================================
    # SLIDE 6: EXPERIMENTAL RESULTS & SOTA COMPARISON
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Experimental Results & State-of-the-Art Benchmarks", "Empirical Evaluation")

    # Left: Results Summary Table / Cards
    rcard = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(5.8), Inches(5.0))
    rcard.fill.solid()
    rcard.fill.fore_color.rgb = CARD_BG
    rcard.line.color.rgb = BORDER_COLOR

    rtb = s6.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(5.4), Inches(4.6))
    rtf = rtb.text_frame
    rtf.word_wrap = True

    rp = rtf.paragraphs[0]
    rp.text = "Benchmark Results Across 3 Primary Cohorts:"
    rp.font.size = Pt(12)
    rp.font.bold = True
    rp.font.color.rgb = NAVY

    perf_points = [
        ("PIMA-IDD-I (768 Cases):", "Stack-ANN achieved 98.81% Accuracy, 97.93% Precision, 98.40% Specificity, 0.9428 MCC, and 0.98 ROC-AUC."),
        ("DDFH-G (2,000 Cases):", "Stack-ANN attained a peak 99.51% Accuracy, 98.92% Precision, 99.02% Specificity, 0.9728 MCC, and 0.99 ROC-AUC (only 2 misclassifications out of 400 test cases)."),
        ("IDPD-I Multi-Class (1,000 Cases):", "Stack-ANN recorded 98.45% Accuracy and 0.9602 MCC. Pre-Diabetic minority class recall surged from 76.2% to 94.3%."),
        ("Comparison with 25 Published SOTA Works:", "• Random Forest (Naveen 2023): 85.6%\n• Deep Belief Network (Shahin 2023): 81.25%\n• Deep ANN (Khanam 2021): 88.60%\n• 1D-CNN (García-Ordás 2021): 92.31%\n• Proposed Stack-ANN: 98.81% to 99.51% (+6.5% to +14% superior).")
    ]
    for pt, pd_desc in perf_points:
        p = rtf.add_paragraph()
        p.text = pt
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE
        p.space_before = Pt(5)
        r = p.add_run()
        r.text = f"\n{pd_desc}"
        r.font.bold = False
        r.font.size = Pt(9)
        r.font.color.rgb = DARK

    # Right: Image of Accuracy Comparison (fig15_edl_accuracy_all.png)
    if os.path.exists("report_figures/fig15_edl_accuracy_all.png"):
        s6.shapes.add_picture("report_figures/fig15_edl_accuracy_all.png", Inches(6.8), Inches(1.85), width=Inches(5.733))

    add_footer(s6, 6)

    # ==========================================
    # SLIDE 7: EXPLAINABLE AI & WHAT-IF COUNTERFACTUAL ENGINE
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Explainable AI (Tree-SHAP) & What-If Simulation Engine", "Model Transparency & Clinical Guidance")

    # Left: SHAP Waterfall Card
    s_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65), Inches(5.7), Inches(5.0))
    s_card.fill.solid()
    s_card.fill.fore_color.rgb = CARD_BG
    s_card.line.color.rgb = BORDER_COLOR

    stb = s7.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(1.4))
    stf = stb.text_frame
    stf.word_wrap = True
    sp = stf.paragraphs[0]
    sp.text = "Local Game-Theoretic SHAP Attributions:"
    sp.font.size = Pt(12)
    sp.font.bold = True
    sp.font.color.rgb = NAVY

    sp_desc = stf.add_paragraph()
    sp_desc.text = "Patient #1042 (Predicted 99.8% Risk vs 68.9% Prior): Primary risk driven by Polyuria (+0.112), Polydipsia (+0.098), Weight Loss (+0.052). Exactly aligns with renal glucose diuresis."
    sp_desc.font.size = Pt(9.5)
    sp_desc.font.color.rgb = DARK
    sp_desc.space_before = Pt(2)

    if os.path.exists("report_figures/fig16_shap_waterfall.png"):
        s7.shapes.add_picture("report_figures/fig16_shap_waterfall.png", Inches(1.0), Inches(3.2), width=Inches(5.3))

    # Right: What-If Counterfactual Card
    w_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.65), Inches(5.733), Inches(5.0))
    w_card.fill.solid()
    w_card.fill.fore_color.rgb = CARD_BG
    w_card.line.color.rgb = BORDER_COLOR

    wtb = s7.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(1.4))
    wtf = wtb.text_frame
    wtf.word_wrap = True
    wp = wtf.paragraphs[0]
    wp.text = "What-If Counterfactual Intervention Trajectory:"
    wp.font.size = Pt(12)
    wp.font.bold = True
    wp.font.color.rgb = NAVY

    wp_desc = wtf.add_paragraph()
    wp_desc.text = "Optimizes actionable lifestyle changes: Baseline risk (99.8%) -> Dietary moderation (91.4%) -> Glycemic control (78.2%) -> Full Remission (34.6%), reversing the diagnosis."
    wp_desc.font.size = Pt(9.5)
    wp_desc.font.color.rgb = DARK
    wp_desc.space_before = Pt(2)

    if os.path.exists("report_figures/fig18_counterfactual.png"):
        s7.shapes.add_picture("report_figures/fig18_counterfactual.png", Inches(7.0), Inches(3.2), width=Inches(5.3))

    add_footer(s7, 7)

    # ==========================================
    # SLIDE 8: SYSTEM DEPLOYMENT, SUMMARY & CONCLUSION
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Clinical Web Deployment, Key Deliverables & Conclusion", "System Delivery & Summary")

    # Left: Deployment Architecture Graphic
    if os.path.exists("report_figures/fig19_cdss_architecture.png"):
        s8.shapes.add_picture("report_figures/fig19_cdss_architecture.png", Inches(0.8), Inches(1.65), width=Inches(5.8))

    # Right: Summary & Achievements Card
    sum_card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.65), Inches(5.733), Inches(5.0))
    sum_card.fill.solid()
    sum_card.fill.fore_color.rgb = CARD_BG
    sum_card.line.color.rgb = BLUE
    sum_card.line.width = Pt(1.5)

    sutb = s8.shapes.add_textbox(Inches(7.0), Inches(1.85), Inches(5.3), Inches(4.6))
    sutf = sutb.text_frame
    sutf.word_wrap = True

    sup = sutf.paragraphs[0]
    sup.text = "Project Summary & Key Milestones:"
    sup.font.size = Pt(13)
    sup.font.bold = True
    sup.font.color.rgb = NAVY

    milestones = [
        ("Interactive Web Application: ", "Implemented in Streamlit & Bootstrap 5.3 with 5 clinical modules (Risk Screening, What-If Simulator, Benchmarks, EDA, and Export)."),
        ("Ultra-Low Latency: ", "Sub-5ms (4.8 ms) real-time inference latency enables instant point-of-care feedback in primary care clinics."),
        ("System Verification: ", "Passed all 7 automated system integrity audit checks with 100% success (datasets, models, XAI, and web apps)."),
        ("Comprehensive 33-Page IEEE Report: ", "Authored full IEEE Access journal-style technical report tailored for Agarshna R (RA2411026050061)."),
        ("Future Scope: ", "Integration with Continuous Glucose Monitoring (CGM) IoT sensors and Deep Reinforcement Learning for dynamic personalized nutrition.")
    ]
    for mt, md in milestones:
        p = sutf.add_paragraph()
        p.text = f"• {mt}"
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = BLUE
        p.space_before = Pt(5)
        r = p.add_run()
        r.text = md
        r.font.bold = False
        r.font.color.rgb = DARK

    add_footer(s8, 8)

    # Save presentation
    output_pptx = r"C:\project\ann_project\Diabetes_Prediction_EDL_Presentation.pptx"
    prs.save(output_pptx)
    print(f"Presentation saved successfully to {output_pptx}!")
    return output_pptx

if __name__ == '__main__':
    create_deck()
