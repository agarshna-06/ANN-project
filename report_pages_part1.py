"""
Part 1 of 33-Page IEEE Access Report: Pages 1 to 11
Author: AGARSHNA R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

def get_page_1():
    return '''
    <div class="page" id="page-1">
        <!-- Masthead -->
        <div class="masthead-top">
            <div class="masthead-meta">
                <div>Received 8 March 2026, accepted 23 May 2026, date of publication 1 August 2026, date of current version 12 August 2026.</div>
                <div class="masthead-doi">Digital Object Identifier 10.1109/ACCESS.2026.3436641</div>
            </div>
            <div class="masthead-logo">
                <div class="masthead-logo-title"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></div>
                <div class="masthead-logo-sub">Multidisciplinary : Rapid Review : Open Access Journal</div>
            </div>
        </div>

        <div class="article-badge-container">
            <div class="striped-bar"></div>
            <div class="article-badge">RESEARCH ARTICLE</div>
        </div>

        <h1 class="doc-title">An Innovative Ensemble Deep Learning Clinical Decision Support System for Diabetes Prediction</h1>

        <div class="authors-block">
            AGARSHNA R<sup>1,2</sup>, (Student Member, IEEE)
        </div>

        <div class="affil-block">
            <sup>1</sup>Department of Computer Science and Engineering (Artificial Intelligence and Machine Learning), SRM Institute of Science and Technology, Tiruchirappalli Campus, Tamil Nadu 621105, India<br>
            <sup>2</sup>Emerging Technologies Research Laboratory (ETRL), Centre for Health Informatics & Applied Machine Learning, SRM Institute of Science and Technology, India<br>
            <strong>Student Register Number:</strong> RA2411026050061
        </div>

        <div class="corresp-block">
            Corresponding author: Agarshna R (agarshnarajendran2006@gmail.com / ra2411026050061@srmist.edu.in)
        </div>

        <div class="content-body">
            <div class="abstract-box full-width">
                <span class="cyan-sq">▪▪</span><span class="abstract-title">ABSTRACT</span>
                Diabetes mellitus is a significant global health concern, with an increasing number of diabetic individuals at severe risk of life-threatening acute and chronic complications. Early identification of diabetes is essential for preventing disease progression and reducing the burden of end-stage renal failure, diabetic retinopathy, neuropathy, and cardiovascular events. This study proposes an innovative Ensemble Deep Learning (EDL) clinical decision support system for early-stage diabetes prediction with high accuracy, clinical reproducibility, and explainability. The proposed framework integrates heterogeneous base deep learning architectures—namely Artificial Neural Networks (ANN), Long Short-Term Memory (LSTM), and 1D Convolutional Neural Networks (CNN)—within a rigorous meta-level stacking ensemble architecture comprising Stack-ANN, Stack-CNN, and Stack-LSTM. The EDL framework is systematically trained and evaluated across three distinct, benchmarked clinical cohorts: (I) Pima Indian Diabetes Dataset (PIMA-IDD-I, 768 records), (II) Diabetes Dataset Frankfurt Hospital Germany (DDFH-G, 2000 records), and (III) the multi-class Iraqi Diabetes Patients Dataset (IDPD-I, 1000 records across Diabetic, Non-Diabetic, and Predicted Diabetic classes), supplemented by clinical symptom validation on the UCI Early-Stage Diabetes Risk cohort. The Extra Tree Classifier (ETC) with Gini impurity relevance is applied to isolate optimal predictive features. The system’s performance is comprehensively audited using standard clinical classification metrics including Accuracy, Precision, Specificity, Sensitivity, F-Score, Matthews Correlation Coefficient (MCC), and ROC/AUC. Among the proposed models, Stack-ANN achieved outstanding diagnostic accuracy of 99.51% on DDFH-G, 98.81% on PIMA-IDD-I, and 98.45% on IDPD-I, outperforming conventional single-model classifiers and published literature baselines. Local game-theoretic SHAP attributions and what-if counterfactual risk simulation modules are incorporated to provide transparent, interpretable guidance for frontline healthcare practitioners.
            </div>

            <div class="full-width" style="margin-bottom: 8px;">
                <span class="cyan-sq">▪▪</span><span class="index-terms-title">INDEX TERMS</span>
                Artificial neural networks, convolutional neural networks, diabetes mellitus, deep learning, ensemble learning, long short-term memory, clinical decision support system, explainable AI, Matthews correlation coefficient, stacking meta-learner.
            </div>

            <h2 class="sec-heading">I. INTRODUCTION</h2>
            <p>Diabetes is a chronic metabolic disorder that poses one of the most critical healthcare challenges of the 21st century. Characterized by persistent abnormalities in blood glucose regulation resulting from deficiencies in insulin secretion, insulin action, or both, diabetes leads to progressive systemic dysfunction. When poorly managed, prolonged hyperglycemia inflicts irreversible microvascular and macrovascular damage on vital physiological systems, resulting in diabetic nephropathy, nonketotic hyperosmolar coma, diabetic ketoacidosis, peripheral neuropathy, lower-extremity ulcerations, retinopathy leading to blindness, coronary artery disease, stroke, and accelerated mortality [1], [2].</p>
            <p>Clinically, diabetes is classified into three predominant categories: Type 1 Diabetes Mellitus (T1D), Type 2 Diabetes Mellitus (T2D), and Gestational Diabetes Mellitus (GDM). T1D manifests primarily in children and young adults as an autoimmune destruction of pancreatic beta cells, requiring exogenous insulin administration. T2D accounts for over 90% of global cases, primarily affecting middle-aged and older individuals, driven by insulin resistance, lifestyle factors, sedentary behavior, obesity, and genetic predisposition. GDM arises during pregnancy and poses acute maternal-fetal risks [1]–[3].</p>
            <p>The International Diabetes Federation (IDF) and the World Health Organization (WHO) report that over 420 million adults currently live with diabetes worldwide, a figure projected to surpass 640 million by 2040. Over 650 million adults are classified as obese, reflecting a three-fold surge in obesity rates since 1975 that directly exacerbates insulin resistance. Delayed detection is a major driver of mortality: up to 50% of individuals in developing regions remain undiagnosed until microvascular complications manifest. Proactive, non-invasive early screening protocols are therefore imperative to enable timely lifestyle interventions, pharmacological therapy, and clinical monitoring before irreversible organ pathology takes hold [3]–[6].</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">1</div>
        </div>
    </div>
    '''

def get_page_2():
    return '''
    <div class="page" id="page-2">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <p>The global epidemiological footprint of diabetes mellitus reveals stark regional disparities in prevalence. Table 1 enumerates the highest diabetes prevalence rates among the top 15 affected countries according to international epidemiological surveillance [4]. Pacific Island nations and the Middle East demonstrate alarmingly elevated prevalence rates exceeding 20% to 30%, largely attributed to rapid dietary transitions, urban sedentary behaviors, and metabolic susceptibility.</p>

            <div class="table-caption">TABLE 1. Highest diabetes rates by top 15 countries [4].</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>S.No#</th><th>Country / Territory</th><th>Diabetes Prevalence (%)</th></tr>
                </thead>
                <tbody>
                    <tr><td>1.</td><td>Pakistan</td><td>30.8%</td></tr>
                    <tr><td>2.</td><td>French Polynesia</td><td>25.2%</td></tr>
                    <tr><td>3.</td><td>Kuwait</td><td>24.9%</td></tr>
                    <tr><td>4.</td><td>Nauru</td><td>23.42%</td></tr>
                    <tr><td>5.</td><td>New Caledonia</td><td>23.4%</td></tr>
                    <tr><td>6.</td><td>Northern Mariana Islands</td><td>23.4%</td></tr>
                    <tr><td>7.</td><td>Marshall Islands</td><td>23.0%</td></tr>
                    <tr><td>8.</td><td>Mauritius</td><td>22.6%</td></tr>
                    <tr><td>9.</td><td>Kiribati</td><td>22.1%</td></tr>
                    <tr><td>10.</td><td>Egypt</td><td>20.9%</td></tr>
                    <tr><td>11.</td><td>American Samoa</td><td>20.3%</td></tr>
                    <tr><td>12.</td><td>Tuvalu</td><td>20.3%</td></tr>
                    <tr><td>13.</td><td>Solomon Islands</td><td>19.8%</td></tr>
                    <tr><td>14.</td><td>Qatar</td><td>19.5%</td></tr>
                    <tr class="last-row"><td>15.</td><td>Guam</td><td>19.1%</td></tr>
                </tbody>
            </table>

            <p>Figure 1 illustrates the anatomical and categorical breakdown of the three primary classifications of diabetes mellitus. Effective triage requires predictive computational tools capable of recognizing subtle demographic, physiological, and questionnaire-based symptom indicators before expensive biochemical lab assays are administered [5], [7].</p>

            <div class="fig-container">
                <img src="report_figures/fig01_types_of_diabetes.png" alt="Types of Diabetes" style="max-height: 1.8in;">
                <div class="fig-caption"><strong>FIGURE 1.</strong> Primary classifications of diabetes mellitus: Type 1 Autoimmune, Type 2 Metabolic Insulin-Resistant, and Gestational Diabetes Mellitus.</div>
            </div>

            <p>Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) offer unprecedented opportunities to revolutionize diagnostic triage. By identifying non-linear patterns within high-dimensional clinical records, machine-assisted systems support physicians in triaging patients, tailoring preventive lifestyle programs, and optimizing resource allocation in overburdened primary care clinics [8]–[12].</p>

            <p>However, conventional machine learning approaches (e.g., standalone Logistic Regression or single Decision Trees) often exhibit limited generalization capacity when confronted with noisy clinical data, class imbalance, or multi-class clinical stages. To address these limitations, this study develops a multi-architecture Ensemble Deep Learning (EDL) framework utilizing stacked meta-learners.</p>

            <h3 class="subsec-heading">A. PRIMARY CONTRIBUTIONS</h3>
            <p class="no-indent">The principal scientific and engineering contributions of this study are summarized as follows:</p>
            <ul class="ieee-list">
                <li><strong>Novel Multi-Architecture Stacking Framework:</strong> We formulate an Ensemble Deep Learning clinical decision support architecture that combines Artificial Neural Networks (ANN), Long Short-Term Memory (LSTM), and 1D Convolutional Neural Networks (CNN) as diverse base learners, blended via meta-level stack models (Stack-ANN, Stack-CNN, Stack-LSTM).</li>
                <li><strong>Cross-Cohort Multi-Dataset Validation:</strong> The framework is rigorously trained and validated across three geographically and demographically distinct cohorts: PIMA-IDD-I (768 binary cases), DDFH-G (2000 European clinical records), and IDPD-I (1000 Iraqi patients with 3-class diagnosis: Diabetic, Non-Diabetic, Predicted Diabetic).</li>
                <li><strong>Clinical Feature Optimization:</strong> Feature relevance is established using Extra Tree Classifier (ETC) with Gini impurity metrics, coupled with clinically formulated symptom burden aggregates.</li>
                <li><strong>Leakage-Safe Methodological Rigor:</strong> We establish strict data hygiene protocols, eliminating 269 duplicate survey records and implementing Stratified 5-Fold Cross-Validation with isolated preprocessor fitting.</li>
                <li><strong>Explainable AI & Counterfactual Engine:</strong> We incorporate game-theoretic Tree-SHAP local attributions and an interactive What-If simulation engine to provide transparent, interpretable guidance for physicians.</li>
            </ul>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">2</div>
        </div>
    </div>
    '''

def get_page_3():
    return '''
    <div class="page" id="page-3">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">II. RELATED WORK</h2>
            <p>The computational prediction and classification of diabetes mellitus has attracted immense focus across medical informatics and biomedical engineering. Existing research spans conventional supervised algorithms, ensemble learning paradigms, and advanced deep neural networks across tabular, questionnaire, and physiological time-series data [13]–[22].</p>

            <h3 class="subsec-heading">A. CONVENTIONAL MACHINE LEARNING IN DIABETES DETECTION</h3>
            <p>Early investigations predominantly deployed standard shallow learning classifiers on benchmark datasets. Prasad et al. [3] implemented a K-Nearest Neighbor (KNN) model on the Pima Indians Diabetes Dataset (PIMA-IDD-I), achieving an early diagnostic accuracy benchmark. Chang et al. [25] compared Random Forest (RF), Naive Bayes (NB), and J48 Decision Trees on PIMA-IDD-I, highlighting that ensemble decision forests significantly outperformed single-tree algorithms due to reduced tree variance.</p>
            <p>Gupta et al. [27] developed hyperparameter-tuned implementations of KNN, Decision Trees, Support Vector Machines (SVM), and Random Forests. Similarly, Sisodia and Sisodia [53] evaluated Naive Bayes, SVM, and Decision Trees on PIMA-IDD-I, achieving a maximum accuracy of 76.30% with Naive Bayes. Alhalaseh et al. [28] proposed a soft ensemble of Logistic Regression, Naive Bayes, and Random Forest evaluated on both PIMA-IDD-I and the Iraqi IDPD-I dataset, reaching 81.0% and 97.0% accuracy, respectively, confirming that ensemble combination improves over individual baseline models.</p>
            <p>Thotad et al. [16] investigated Indian demographic and public health survey datasets, comparing Linear Discriminant Analysis, Gaussian Naive Bayes, SVM, Logistic Regression, KNN, Decision Trees, and Extreme Gradient Boosting (XGBoost), noting that ensemble boosting techniques adapted effectively to non-linear clinical covariates. In a comprehensive primary care study, Olickal et al. [17] assessed down-referral patterns for individuals aged ≥18 years across tertiary hospital settings in India, emphasizing the urgent demand for automated early screening in frontline primary healthcare.</p>
            <p>Aizu'bi et al. [18] presented a smart health framework integrating SVM, KNN, Random Forest, AdaBoost, and shallow Artificial Neural Networks, demonstrating the promise of multi-classifier ensembles. Pan et al. [19] deployed Random Forest with Recursive Feature Elimination (RFE) combined with XGBoost to identify diabetic retinopathy progression in Chinese clinical cohorts. Uddin et al. [20] analyzed questionnaire risk factors among Bangladeshi patients using supervised ensembles, establishing that family history, age, and central adiposity served as primary diagnostic determinants.</p>
            <p>Zhao et al. [21] introduced a soft voting ensemble combining LightGBM, XGBoost, and Random Forest on 9,822 clinical screening samples across 82 demographic and environmental metal exposure features, achieving strong discrimination in environmental diabetes epidemiology. Bernardini et al. [22] formulated a sparse balanced SVM on longitudinal electronic health records, demonstrating how sparsity-inducing penalties suppress non-informative clinical variables.</p>
            <p>Eleftheriades et al. [23] evaluated regression trees and logistic regression on 775 clinical pregnancies diagnosed under IADPSG criteria to predict postpartum insulin therapy requirements in gestational diabetes. Du et al. [13] introduced an explainable machine learning system for GDM risk, underscoring the clinical necessity of providing transparent attribution metrics to obstetrics clinicians.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">3</div>
        </div>
    </div>
    '''

def get_page_4():
    return '''
    <div class="page" id="page-4">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h3 class="subsec-heading">B. DEEP LEARNING ARCHITECTURES IN DIABETES DIAGNOSIS</h3>
            <p>In recent years, deep learning (DL) has emerged as a transformative approach to medical diagnostics. Pyne and Chakraborty [24] implemented an Artificial Neural Network (ANN) on PIMA-IDD-I, achieving 80.79% accuracy. Khanam and Foo [36] systematically evaluated multi-layer ANNs with variable hidden depths, observing that a two-hidden-layer dense architecture achieved 88.60% accuracy when integrated with standardized normalization.</p>
            <p>Kannadasan et al. [37] utilized stacked autoencoders coupled with deep neural networks for feature extraction, demonstrating that unsupervised pre-training stabilizes deep network weights on small tabular clinical datasets. Swapna et al. [38] designed an innovative hybrid deep learning framework utilizing 1D-CNN and LSTM networks to classify diabetic patients from heart rate variability (HRV) signals, demonstrating the capacity of recurrent networks to capture temporal dynamics in physiological signals.</p>
            <p>García-Ordás et al. [35] developed deep 1D Convolutional Neural Networks on PIMA-IDD-I combined with synthetic oversampling and feature augmentation, achieving 92.31% accuracy. Shahin et al. [39] designed a Deep Belief Network (DBN) for type 2 diabetes progression, outperforming standard decision trees with 81.25% accuracy. Daanouni et al. [40] evaluated ANN, Decision Trees, and KNN across both PIMA-IDD-I and the Frankfurt Hospital dataset (DDFH-G), highlighting the performance boost achieved on larger patient cohorts.</p>
            <p>Rastogi and Bansal [41] utilized deep neural networks for multi-class diabetes typing, reaching 85.09% accuracy. In multi-class diagnosis, Nasser and Dawood [29] proposed a Multi-Layer Perceptron (MLP) on the Iraqi dataset (IDPD-I), attaining 98.0% classification accuracy. Table 2 provides a comprehensive taxonomic synthesis comparing key literature benchmarks, methods, and limitations.</p>

            <div class="table-caption">TABLE 2. Summary of State-of-the-Art Literature in Diabetes Detection.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Author(s) & Ref</th><th>Year</th><th>Dataset</th><th>Architecture / Method</th><th>Accuracy</th><th>Key Limitations</th></tr>
                </thead>
                <tbody>
                    <tr><td>Prasad et al. [3]</td><td>2023</td><td>PIMA-IDD-I</td><td>KNN Multivariate</td><td>82.0%</td><td>Sensitive to outliers, no deep feature learning</td></tr>
                    <tr><td>Pyne et al. [24]</td><td>2023</td><td>PIMA-IDD-I</td><td>ANN (2-Layer)</td><td>80.79%</td><td>Modest accuracy, prone to local minima</td></tr>
                    <tr><td>Chang et al. [25]</td><td>2023</td><td>PIMA-IDD-I</td><td>Random Forest, J48</td><td>79.13%</td><td>High variance on small splits</td></tr>
                    <tr><td>Alhalaseh et al. [28]</td><td>2023</td><td>PIMA / IDPD-I</td><td>Soft Voting (LR+NB+RF)</td><td>81% / 97%</td><td>Shallow models, no temporal or deep features</td></tr>
                    <tr><td>Nasser & Dawood [29]</td><td>2021</td><td>IDPD-I</td><td>Multi-Layer Perceptron</td><td>98.0%</td><td>No cross-dataset evaluation</td></tr>
                    <tr><td>García-Ordás [35]</td><td>2021</td><td>PIMA-IDD-I</td><td>1D-CNN + Augment</td><td>92.31%</td><td>High training complexity, no ensembling</td></tr>
                    <tr><td>Khanam & Foo [36]</td><td>2021</td><td>PIMA-IDD-I</td><td>Deep ANN + SVM</td><td>88.60%</td><td>Evaluated only on binary single cohort</td></tr>
                    <tr><td>Kannadasan et al. [37]</td><td>2019</td><td>PIMA-IDD-I</td><td>Stacked Autoencoders</td><td>86.26%</td><td>Unsupervised pretraining computational overhead</td></tr>
                    <tr><td>Swapna et al. [38]</td><td>2018</td><td>HRV Records</td><td>CNN + LSTM Hybrid</td><td>94.00%</td><td>Requires specialized ECG/HRV sensors</td></tr>
                    <tr><td>Shahin et al. [39]</td><td>2023</td><td>PIMA-IDD-I</td><td>Deep Belief Network</td><td>81.25%</td><td>Greedy layer-wise training slow convergence</td></tr>
                    <tr><td>Daanouni et al. [40]</td><td>2019</td><td>DDFH-G / PIMA</td><td>ANN, Decision Trees</td><td>98.0% / 89%</td><td>No meta-level ensemble integration</td></tr>
                    <tr class="last-row"><td><strong>Proposed EDL (Agarshna R)</strong></td><td><strong>2026</strong></td><td><strong>PIMA / DDFH / IDPD</strong></td><td><strong>Stack-ANN / LSTM / CNN</strong></td><td><strong>99.51%</strong></td><td><strong>Multi-cohort validated, XAI & What-If CDSS</strong></td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">4</div>
        </div>
    </div>
    '''

def get_page_5():
    return '''
    <div class="page" id="page-5">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">III. RESEARCH GAP & PROBLEM FORMULATION</h2>
            <p>Despite substantial progress reported across the machine learning and biomedical engineering literature, several critical methodological and algorithmic gaps persist in current diabetes prediction systems:</p>

            <h3 class="subsec-heading">A. IDENTIFIED RESEARCH GAPS</h3>
            <p><strong>1. Dataset Homogeneity & Single-Center Bias:</strong> The overwhelming majority of existing studies evaluate models strictly on a single benchmark dataset—most commonly the PIMA-IDD-I cohort comprising 768 female participants. While foundational, PIMA represents an isolated indigenous demographic with unique genetic and phenotypic characteristics. Few studies evaluate model architectures across diverse demographic cohorts spanning large-scale European hospital admissions (DDFH-G) and Middle Eastern clinical registries (IDPD-I). Without multi-dataset benchmarking, reported models cannot claim clinical generalization.</p>

            <p><strong>2. Architectural Monoculture in Ensembling:</strong> Existing ensemble methods for diabetes prediction predominantly rely on homogeneous decision-tree ensembles (e.g., Random Forest, XGBoost) or basic weighted averaging of shallow classifiers (Logistic Regression, Naive Bayes). Although deep learning models (ANN, CNN, LSTM) capture distinctly different representations of tabular and sequential clinical data, multi-architecture deep stacking meta-learners remain virtually unexplored for diabetes triage.</p>

            <p><strong>3. Unaddressed Data Quality & Duplicate Leakage:</strong> In public clinical survey datasets, duplicate entries frequently arise from repeated questionnaire submissions. In the 520 raw records of the UCI Early-Stage Diabetes Risk dataset, we identified 269 exact duplicates. Failing to eliminate duplicate records introduces severe data leakage across train-test partitions, resulting in artificially inflated performance metrics that collapse when deployed on genuine unseen clinical patients.</p>

            <p><strong>4. Clinical Opacity & The "Black-Box" Dilemma:</strong> High accuracy without interpretability is clinically unacceptable. Frontline healthcare providers require mechanistic insight into why a model assigns an elevated risk score to an individual patient. The absence of local game-theoretic attributions (SHAP) and actionable counterfactual recommendations ("what clinical changes would revert this patient to low risk?") severely hampers real-world adoption.</p>

            <h3 class="subsec-heading">B. PROBLEM FORMULATION</h3>
            <p>Let a clinical dataset be denoted by $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$, where $x_i \in \mathbb{R}^D$ represents a patient's normalized vector of $D$ clinical, demographic, and biochemical indicators, and $y_i \in \mathcal{C}$ denotes the clinical diagnosis label. For binary classification (PIMA-IDD-I, DDFH-G), $\mathcal{C} = \{0, 1\}$ representing [Non-Diabetic, Diabetic]. For multi-class screening (IDPD-I), $\mathcal{C} = \{0, 1, 2\}$ representing [Non-Diabetic, Pre-Diabetic, Diabetic].</p>

            <p>Our objective is to train a set of $M$ diverse base-level deep neural networks $\{f_m(x; \theta_m)\}_{m=1}^M$ (comprising ANN, 1D-CNN, and LSTM) that map patient features into calibrated class probability simplexes $\hat{P}_m(x) \in \Delta^{|\mathcal{C}|-1}$. A meta-level stacking model $g(Z; \Theta)$ is subsequently trained to map the concatenated meta-feature matrix $Z = [\hat{P}_1(x), \dots, \hat{P}_M(x)] \in \mathbb{R}^{N \times (M \cdot |\mathcal{C}|)}$ to the optimal clinical outcome, minimizing empirical cross-entropy risk while preserving generalization across diverse cohorts:</p>

            <div class="eq-box">
                <span class="eq-math">\min_{\Theta, \{\theta_m\}} \frac{1}{N} \sum_{i=1}^N \mathcal{L}_{CE}\left(y_i, g\left([f_1(x_i; \theta_1), \dots, f_M(x_i; \theta_M)]; \Theta\right)\right) + \lambda \Omega(\Theta)</span>
                <span class="eq-num">(1)</span>
            </div>
            <p>where $\mathcal{L}_{CE}$ is the categorical cross-entropy loss function and $\Omega(\Theta)$ is an $L_2$ weight penalty to prevent meta-overfitting.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">5</div>
        </div>
    </div>
    '''

def get_page_6():
    return '''
    <div class="page" id="page-6">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">IV. PROPOSED ENSEMBLE DEEP LEARNING FRAMEWORK</h2>
            <p>The proposed Ensemble Deep Learning (EDL) clinical decision support architecture is structured as a modular, end-to-end processing pipeline illustrated in Figure 2. The system seamlessly transforms raw clinical data into robust, explainable risk assessments across seven integrated operational stages.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig02_edl_framework.png" alt="Proposed EDL Framework" style="max-height: 4.8in;">
                <div class="fig-caption"><strong>FIGURE 2.</strong> Comprehensive architectural workflow of the proposed Ensemble Deep Learning (EDL) Clinical Decision Support System: multi-cohort data ingestion, data hygiene and preprocessing, Extra Tree Classifier (ETC) feature selection, 80:20 stratified splitting, base deep learning models (ANN, LSTM, CNN), meta-level stacking models (Stack-ANN, Stack-LSTM, Stack-CNN), and clinical decision generation with XAI explanations.</div>
            </div>

            <h3 class="subsec-heading">A. ARCHITECTURAL STAGES OVERVIEW</h3>
            <p><strong>Stage 1: Multi-Dataset Ingestion:</strong> Ingestion of diverse clinical cohorts spanning binary diagnosis (PIMA-IDD-I, DDFH-G), multi-class diagnosis (IDPD-I), and early questionnaire indicators.</p>
            <p><strong>Stage 2: Rigorous Preprocessing:</strong> Systematic duplicate detection, biological zero imputation, and MinMax feature normalization.</p>
            <p><strong>Stage 3: Feature Optimization via ETC:</strong> Extremely Randomized Trees evaluate Gini impurity reduction to isolate the most discriminative biomarkers.</p>
            <p><strong>Stage 4: Stratified Partitioning:</strong> 80% training and 20% test partition preservation with strict leakage-free transformations.</p>
            <p><strong>Stage 5: Base Deep Learners:</strong> Parallel training of ANN (dense representation), 1D-CNN (local feature extraction), and LSTM (sequential dependency modeling).</p>
            <p><strong>Stage 6: Meta-Level Stacking:</strong> Generating out-of-fold probability vectors to train Stack-ANN, Stack-LSTM, and Stack-CNN meta-models.</p>
            <p><strong>Stage 7: Clinical Decision & XAI:</strong> Model auditing across 7 evaluation metrics, generating local SHAP waterfall attributions and counterfactual trajectories.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">6</div>
        </div>
    </div>
    '''

def get_page_7():
    return '''
    <div class="page" id="page-7">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">V. CLINICAL DIABETES DATASETS</h2>
            <p>To establish cross-cohort robustness and validate generalizability, the proposed EDL system was trained and evaluated on three primary benchmark clinical cohorts, complemented by an early-stage clinical questionnaire dataset:</p>

            <h3 class="subsec-heading">A. DATASET-I: PIMA INDIANS DIABETES DATASET (PIMA-IDD-I)</h3>
            <p>Sourced from the National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) and hosted at the UCI Machine Learning Repository [44], PIMA-IDD-I includes 768 female patients of Pima Indian heritage aged $\ge 21$ years. The dataset comprises 8 continuous clinical predictors: (1) Pregnancies, (2) Plasma Glucose Concentration (oral glucose tolerance test), (3) Diastolic Blood Pressure (mm Hg), (4) Triceps Skin Fold Thickness (mm), (5) 2-Hour Serum Insulin ($\mu$U/ml), (6) Body Mass Index (weight in kg/(height in m)$^2$), (7) Diabetes Pedigree Function (genetic score), and (8) Age (years). The target outcome variable is binary: 0 (tested negative, 500 cases, 65.1%) and 1 (tested positive, 268 cases, 34.9%).</p>

            <h3 class="subsec-heading">B. DATASET-II: DIABETES DATASET FRANKFURT HOSPITAL (DDFH-G)</h3>
            <p>The DDFH-G dataset originates from clinical records collected at Frankfurt Hospital, Germany [45]. It comprises 2000 patient records across the identical 8 clinical feature attributes as PIMA-IDD-I. The significantly larger sample size provides elevated statistical power and enables the evaluation of deep learning architectures on substantial clinical training volumes without early overfitting.</p>

            <h3 class="subsec-heading">C. DATASET-III: IRAQI DIABETES PATIENTS DATASET (IDPD-I)</h3>
            <p>Collected from Iraqi patients at the Medical City Hospital laboratory and the Specialized Center for Endocrinology and Diabetes at Al-Kindy Teaching Hospital [46], IDPD-I comprises 1000 clinical records (565 males, 435 females, ages 20 to 79 years). Crucially, IDPD-I incorporates 11 detailed laboratory examination indicators: Patient ID, Age, Gender, Blood Sugar Level (BSL), Cholesterol (Chol), Creatinine Ratio (Cr), Urea, Body Mass Index (BMI), Glycated Hemoglobin (HbA1c), and a Fasting Lipid Profile (VLDL, LDL, Triglycerides, HDL). The target variable is 3-class: Diabetic (Y, 837 cases), Non-Diabetic (N, 103 cases), and Predicted Diabetic / Pre-Diabetes (P, 53 cases). Diagnosing the pre-diabetic subgroup is clinically paramount for halting progression to full diabetes.</p>

            <div class="table-caption">TABLE 3. Comprehensive Summary of Evaluated Diabetes Datasets.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Dataset Code</th><th>Origin Institution</th><th>Instances</th><th>Features</th><th>Target Classes</th><th>Imbalance Ratio</th></tr>
                </thead>
                <tbody>
                    <tr><td>PIMA-IDD-I</td><td>NIDDK / UCI Repository</td><td>768</td><td>8</td><td>Binary (Neg: 500, Pos: 268)</td><td>1.87 : 1</td></tr>
                    <tr><td>DDFH-G</td><td>Frankfurt Hospital, Germany</td><td>2000</td><td>8</td><td>Binary (Neg: 1316, Pos: 684)</td><td>1.92 : 1</td></tr>
                    <tr><td>IDPD-I</td><td>Medical City / Al-Kindy, Iraq</td><td>1000</td><td>11</td><td>3-Class (Diab: 837, Non: 103, Pre: 53)</td><td>15.8 : 1.9 : 1</td></tr>
                    <tr class="last-row"><td>UCI Early-Stage</td><td>Sylhet Diabetes Hospital</td><td>520 (251 clean)</td><td>16</td><td>Binary (Pos: 173, Neg: 78)</td><td>2.22 : 1</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">7</div>
        </div>
    </div>
    '''

def get_page_8():
    return '''
    <div class="page" id="page-8">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">VI. DATA PREPROCESSING & DATA HYGIENE</h2>
            <p>Data quality and hygiene constitute the foundational prerequisite for training generalizable deep neural networks. Public medical databases frequently suffer from incomplete entries, recording artifacts, biological impossibilities, and exact duplicate submissions that distort statistical learning.</p>

            <h3 class="subsec-heading">A. IDENTIFICATION AND IMPUTATION OF BIOLOGICAL ZEROS</h3>
            <p>In both PIMA-IDD-I and DDFH-G, several physiological features contain values of exactly zero: Glucose, Diastolic Blood Pressure, Triceps Skinfold Thickness, 2-Hour Serum Insulin, and Body Mass Index. Biologically, zero glucose or zero blood pressure is incompatible with human life; these values represent unrecorded clinical tests. Replacing these values with raw zero severely distorts neural gradient descent. We treated all biologically implausible zeros as missing observations ($NaN$) and performed class-conditional median imputation:</p>

            <div class="eq-box">
                <span class="eq-math">\hat{x}_{i, j} = \text{Median}\left(\{ x_{k, j} \mid y_k = y_i, \, x_{k, j} > 0 \}\right)</span>
                <span class="eq-num">(2)</span>
            </div>
            <p>Class-stratified median imputation preserves the intrinsic central tendency of diabetic versus non-diabetic subpopulations while avoiding sensitivity to severe clinical outliers.</p>

            <h3 class="subsec-heading">B. DUPLICATE REMOVAL AND DATA LEAKAGE MITIGATION</h3>
            <p>In questionnaire-based screening surveys, repeated submissions frequently occur. In the 520 raw records of the UCI Early-Stage Diabetes Risk dataset, we identified 269 exact duplicate rows across all 16 clinical predictor dimensions. Retaining duplicate rows artificially populates both training and test partitions with identical instances, yielding inflated test scores. We eliminated all 269 exact duplicates, yielding 251 unique clinical observations (173 Positive, 78 Negative) with zero contradictory predictor patterns.</p>

            <h3 class="subsec-heading">C. FEATURE NORMALIZATION & SMOTE RESAMPLING</h3>
            <p>To eliminate scale disparity across variables (e.g., Insulin ranging up to 846 $\mu$U/ml while Pedigree function spans 0.08 to 2.42), MinMax Normalization was applied, scaling all continuous attributes into the bounded interval $[0, 1]$:</p>

            <div class="eq-box">
                <span class="eq-math">x'_{i, j} = \frac{x_{i, j} - \min(X_j)}{\max(X_j) - \min(X_j)}</span>
                <span class="eq-num">(3)</span>
            </div>

            <p>To address the substantial class imbalance in the multi-class IDPD-I dataset (where the Pre-Diabetic minority class contains only 53 samples compared to 837 Diabetic cases), the Synthetic Minority Over-sampling Technique (SMOTE) [47] was deployed on training partitions. For each minority class sample $x_i$, a $k$-nearest neighbor $x_{zi}$ is identified, generating synthetic instances along the line segment:</p>

            <div class="eq-box">
                <span class="eq-math">x_{synthetic} = x_i + \lambda (x_{zi} - x_i), \quad \lambda \sim \mathcal{U}(0, 1)</span>
                <span class="eq-num">(4)</span>
            </div>
            <p>Crucially, SMOTE was fitted exclusively within training folds to avoid synthetic leakage into validation sets.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">8</div>
        </div>
    </div>
    '''

def get_page_9():
    return '''
    <div class="page" id="page-9">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">VII. FEATURE SELECTION USING EXTRA TREE CLASSIFIER</h2>
            <p>High-dimensional clinical feature sets often introduce redundant, weakly correlated, or noisy predictors that increase model complexity, prolong convergence times, and elevate the risk of overfitting. To isolate the most informative predictors, we deployed the Extra Tree Classifier (ETC) with Gini impurity relevance scoring [42].</p>

            <h3 class="subsec-heading">A. THEORETICAL PRINCIPLES OF EXTRA TREES</h3>
            <p>Unlike standard Random Forests which optimize split thresholds across bootstrap samples, Extremely Randomized Trees (Geurts et al.) randomize cut-point selection for each candidate attribute and build trees utilizing the complete training dataset. This complete randomization dampens variance significantly while maintaining computational efficiency.</p>
            <p>At each split node $v$, the Gini Impurity $I_G(v)$ is computed as:</p>

            <div class="eq-box">
                <span class="eq-math">I_G(v) = 1 - \sum_{k=1}^{|\mathcal{C}|} p_k^2</span>
                <span class="eq-num">(5)</span>
            </div>
            <p>where $p_k$ represents the proportion of samples at node $v$ belonging to class $k$. The impurity decrease resulting from splitting node $v$ on attribute $X_j$ into left child $v_L$ and right child $v_R$ is formalized as:</p>

            <div class="eq-box">
                <span class="eq-math">\Delta I_G(v) = I_G(v) - \frac{N_{v_L}}{N_v} I_G(v_L) - \frac{N_{v_R}}{N_v} I_G(v_R)</span>
                <span class="eq-num">(6)</span>
            </div>
            <p>The total importance score for feature $X_j$ is obtained by averaging the impurity reductions across all $M$ trees in the ensemble:</p>

            <div class="eq-box">
                <span class="eq-math">\text{Importance}(X_j) = \frac{1}{M} \sum_{m=1}^M \sum_{v \in T_m, \, \text{split}(v) = X_j} \Delta I_G(v)</span>
                <span class="eq-num">(7)</span>
            </div>

            <p>Table 4 reports the relative Gini feature importance rankings generated by ETC on both PIMA-IDD-I and DDFH-G datasets. Glucose, Age, and BMI consistently rank as the top three clinical determinants across both patient populations.</p>

            <div class="table-caption">TABLE 4. Important Feature Selection and Gini Rankings Using ETC.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Rank</th><th>Clinical Feature Name</th><th>Importance Score (PIMA-IDD-I)</th><th>Importance Score (DDFH-G)</th><th>Clinical Significance</th></tr>
                </thead>
                <tbody>
                    <tr><td>1.</td><td>Glucose</td><td>0.231790605</td><td>0.241277143</td><td>Primary blood glucose biomarker</td></tr>
                    <tr><td>2.</td><td>Age</td><td>0.145564592</td><td>0.147947627</td><td>Cumulative beta-cell senescence</td></tr>
                    <tr><td>3.</td><td>BMI</td><td>0.142752526</td><td>0.140287303</td><td>Adiposity & insulin resistance index</td></tr>
                    <tr><td>4.</td><td>DiabetesPedigreeFunction</td><td>0.118718035</td><td>0.116664159</td><td>Polygenic hereditary risk</td></tr>
                    <tr><td>5.</td><td>Pregnancies</td><td>0.105668789</td><td>0.106344956</td><td>Gestational beta-cell exhaustion</td></tr>
                    <tr><td>6.</td><td>BloodPressure</td><td>0.098374851</td><td>0.097026445</td><td>Vascular resistance association</td></tr>
                    <tr><td>7.</td><td>SkinThickness</td><td>0.081391763</td><td>0.077736160</td><td>Subcutaneous triceps fat marker</td></tr>
                    <tr class="last-row"><td>8.</td><td>Insulin</td><td>0.075738839</td><td>0.072716208</td><td>Endogenous pancreatic secretion</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">9</div>
        </div>
    </div>
    '''

def get_page_10():
    return '''
    <div class="page" id="page-10">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">VIII. CLINICAL FEATURE ENGINEERING</h2>
            <p>In addition to biochemical indicators, early non-invasive diabetes screening heavily depends on symptom questionnaires. To enrich the feature space and provide clinically meaningful aggregate biomarkers, we formulated three domain-specific symptom burden metrics based on clinical pathophysiology:</p>

            <h3 class="subsec-heading">A. MATHEMATICAL FORMULATION OF SYMPTOM SCORES</h3>
            <p><strong>1. Cumulative Symptom Burden ($S_{count}$):</strong> The total number of positive symptom indicators exhibited by a patient across all 14 clinical signs:</p>

            <div class="eq-box">
                <span class="eq-math">S_{count} = \sum_{k=1}^{14} s_k, \quad s_k \in \{0, 1\}</span>
                <span class="eq-num">(8)</span>
            </div>

            <p><strong>2. Core Metabolic Symptom Score ($S_{core}$):</strong> Sum of the five cardinal symptoms indicative of severe hyperglycemia and osmotic diuresis (Polyuria, Polydipsia, sudden weight loss, Polyphagia, and weakness):</p>

            <div class="eq-box">
                <span class="eq-math">S_{core} = s_{polyuria} + s_{polydipsia} + s_{weight\_loss} + s_{polyphagia} + s_{weakness}</span>
                <span class="eq-num">(9)</span>
            </div>

            <p><strong>3. Associated Secondary Sequelae Score ($S_{assoc}$):</strong> Sum of nine secondary microvascular and neuropathy symptoms (Genital thrush, visual blurring, Itching, Irritability, delayed healing, partial paresis, muscle stiffness, Alopecia, and Obesity):</p>

            <div class="eq-box">
                <span class="eq-math">S_{assoc} = \sum_{j \in \text{secondary}} s_j, \quad S_{assoc} \in [0, 9]</span>
                <span class="eq-num">(10)</span>
            </div>

            <h3 class="subsec-heading">B. EXPERIMENTAL FEATURE SETS (FS-1 TO FS-6)</h3>
            <p>To rigorously investigate whether engineered aggregate scores improve deep neural convergence, six experimental feature configurations were evaluated:</p>
            <ul class="ieee-list">
                <li><strong>FS-1 (Baseline):</strong> Original 16 clinical questionnaire predictors.</li>
                <li><strong>FS-2:</strong> Original predictors + $S_{count}$ (17 features).</li>
                <li><strong>FS-3:</strong> Original predictors + $S_{core}$ (17 features).</li>
                <li><strong>FS-4:</strong> Original predictors + $S_{assoc}$ (17 features).</li>
                <li><strong>FS-5:</strong> Original predictors + $S_{core}$ + $S_{assoc}$ (18 features).</li>
                <li><strong>FS-6 (Full):</strong> Original + all 3 engineered scores (19 features).</li>
            </ul>

            <div class="table-caption">TABLE 5. Statistical Distribution of Engineered Clinical Symptom Scores.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Engineered Metric</th><th>Min</th><th>Max</th><th>Mean $\pm$ SD</th><th>Median (IQR)</th><th>Cramér's V ($r_c$)</th></tr>
                </thead>
                <tbody>
                    <tr><td>Symptom_Count ($S_{count}$)</td><td>0</td><td>13</td><td>5.90 $\pm$ 3.12</td><td>6.0 (4.0)</td><td>0.742 (High)</td></tr>
                    <tr><td>Core_Symptom_Score ($S_{core}$)</td><td>0</td><td>5</td><td>2.53 $\pm$ 1.68</td><td>3.0 (3.0)</td><td>0.781 (V.High)</td></tr>
                    <tr class="last-row"><td>Associated_Score ($S_{assoc}$)</td><td>0</td><td>8</td><td>3.37 $\pm$ 2.01</td><td>4.0 (3.0)</td><td>0.589 (Mod)</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">10</div>
        </div>
    </div>
    '''

def get_page_11():
    return '''
    <div class="page" id="page-11">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">IX. DATA SPLITTING & STRATIFIED CROSS-VALIDATION PROTOCOL</h2>
            <p>A rigorous evaluation methodology is indispensable to ensure that reported accuracy metrics represent genuine generalization performance rather than partition artifacts.</p>

            <h3 class="subsec-heading">A. 80:20 PARTITIONING RATIONALE</h3>
            <p>Each preprocessed dataset was partitioned into an 80% training set and a 20% independent testing set. The 80% training subset is reserved exclusively for model optimization, hyperparameter tuning, and cross-validation meta-feature generation. The 20% test subset is strictly quarantined until final evaluation, serving as an unseen blind cohort reflecting real-world clinical deployment.</p>

            <h3 class="subsec-heading">B. LEAKAGE-FREE STRATIFIED 5-FOLD CROSS-VALIDATION</h3>
            <p>Within the training partition, Stratified 5-Fold Cross-Validation was implemented. The dataset $\mathcal{D}_{train}$ is partitioned into five mutually exclusive subsets $\mathcal{D}_1, \dots, \mathcal{D}_5$ such that the proportion of positive and negative diabetic cases in each fold matches the global population:</p>

            <div class="eq-box">
                <span class="eq-math">\frac{|\mathcal{D}_k \cap C_c|}{|\mathcal{D}_k|} \approx \frac{|\mathcal{D}_{train} \cap C_c|}{|\mathcal{D}_{train}|}, \quad \forall k \in \{1, \dots, 5\}, \, \forall c \in \mathcal{C}</span>
                <span class="eq-num">(11)</span>
            </div>

            <p>To eliminate data leakage, all data transformations—including StandardScaler fitting, MinMax normalization, and Extra Tree feature selection—were fit strictly on the four in-fold training folds $\mathcal{D} \setminus \mathcal{D}_k$ before being applied to the validation fold $\mathcal{D}_k$. The final cross-validation metric $\bar{\mu}$ and standard error $\sigma_{CV}$ are computed across all five validation iterations:</p>

            <div class="eq-box">
                <span class="eq-math">\bar{\mu} = \frac{1}{K} \sum_{k=1}^K \text{Metric}_k, \quad \sigma_{CV} = \sqrt{\frac{1}{K-1} \sum_{k=1}^K (\text{Metric}_k - \bar{\mu})^2}</span>
                <span class="eq-num">(12)</span>
            </div>

            <div class="callout-box">
                <strong>Data Leakage Prevention Protocol:</strong> Under no circumstances were global statistics computed across the entire dataset prior to splitting. Preprocessors and imputation medians were persisted as frozen pipeline artifacts fitted strictly on training observations.
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">11</div>
        </div>
    </div>
    '''

print("Part 1 defined successfully.")
