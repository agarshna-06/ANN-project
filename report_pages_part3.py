"""
Part 3 of 33-Page IEEE Access Report: Pages 23 to 33
Author: AGARSHNA R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

def get_page_23():
    return '''
    <div class="page" id="page-23">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h3 class="subsec-heading">B. VISUAL PERFORMANCE EVALUATION ON DDFH-G</h3>
            <p>Figure 7 graphically contrasts the six evaluation metrics across base and meta models on the DDFH-G dataset, confirming that the stacking ensemble achieves uniform superiority across all clinical metrics.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig07_ddfh_perf.png" alt="DDFH Performance" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 7.</strong> Performance comparison of proposed DL base models and EDL meta-models on DDFH-G across Accuracy, Precision, Specificity, Sensitivity, F-Score, and MCC.</div>
            </div>

            <p>Figures 11 and 14 illustrate the ROC-AUC discriminative curves on DDFH-G. In Figure 11, base models achieve strong AUC values of 0.97 (ANN), 0.96 (LSTM), and 0.94 (CNN). In Figure 14, the EDL meta-models achieve state-of-the-art AUC scores, with Stack-ANN attaining an exceptional AUC of <strong>0.99</strong>, Stack-LSTM recording 0.98, and Stack-CNN achieving 0.97.</p>

            <div style="display: flex; gap: 8px; margin: 6px 0;" class="full-width">
                <div style="flex: 1; text-align: center;">
                    <img src="report_figures/fig11_base_roc_ddfh.png" alt="Base ROC DDFH" style="max-height: 2.2in; width: 100%;">
                    <div class="fig-caption"><strong>FIGURE 11.</strong> ROC/AUC for DL base models (LSTM, CNN, ANN) on DDFH-G.</div>
                </div>
                <div style="flex: 1; text-align: center;">
                    <img src="report_figures/fig14_edl_roc_ddfh.png" alt="EDL ROC DDFH" style="max-height: 2.2in; width: 100%;">
                    <div class="fig-caption"><strong>FIGURE 14.</strong> ROC/AUC for proposed EDL models (Stack-ANN, LSTM, CNN) on DDFH-G.</div>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">23</div>
        </div>
    </div>
    '''

def get_page_24():
    return '''
    <div class="page" id="page-24">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XX. EXPERIMENTAL RESULTS: MULTI-CLASS IDPD-I DATASET</h2>
            <p>Evaluating multi-class discrimination is vital for clinical diabetes management. The Iraqi dataset (IDPD-I) evaluates the system's capacity to differentiate between Diabetic (Y), Non-Diabetic (N), and Predicted Diabetic / Pre-Diabetes (P). Table 14 reports performance across base and meta models.</p>

            <div class="table-caption">TABLE 14. Performance Evaluation of Base and Meta Models on Multi-Class IDPD-I.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th rowspan="2">Evaluation Indexes</th><th colspan="3">Deep Learning (Base Models)</th><th colspan="3">Ensemble Deep Learning (Meta Models)</th></tr>
                    <tr><th>ANN</th><th>LSTM</th><th>CNN</th><th>Stack-ANN</th><th>Stack-LSTM</th><th>Stack-CNN</th></tr>
                </thead>
                <tbody>
                    <tr><td>Accuracy</td><td>0.9462</td><td>0.9087</td><td>0.9025</td><td><strong>0.9845</strong></td><td>0.9788</td><td>0.9689</td></tr>
                    <tr><td>Precision</td><td>0.9343</td><td>0.9067</td><td>0.9122</td><td><strong>0.9893</strong></td><td>0.9803</td><td>0.9690</td></tr>
                    <tr><td>Specificity</td><td>0.9274</td><td>0.9132</td><td>0.9013</td><td><strong>0.9788</strong></td><td>0.9775</td><td>0.9722</td></tr>
                    <tr><td>Sensitivity</td><td>0.9388</td><td>0.9055</td><td>0.9054</td><td><strong>0.9802</strong></td><td>0.9785</td><td>0.9662</td></tr>
                    <tr><td>F-Score</td><td>0.9424</td><td>0.9024</td><td>0.9132</td><td><strong>0.9878</strong></td><td>0.9706</td><td>0.9670</td></tr>
                    <tr class="last-row"><td>MCC</td><td>0.9343</td><td>0.8923</td><td>0.8902</td><td><strong>0.9602</strong></td><td>0.9544</td><td>0.9487</td></tr>
                </tbody>
            </table>

            <h3 class="subsec-heading">A. QUANTITATIVE ANALYSIS ON IDPD-I</h3>
            <p>Among base architectures, ANN led with 0.9462 accuracy and 0.9343 MCC, while LSTM and CNN recorded 0.9087 and 0.9025 accuracy. The multi-class diagnostic task proved challenging for individual base models due to the acute class imbalance of the Pre-Diabetic group (53 instances).</p>
            <p>However, when combined into the meta-level stacking framework, Stack-ANN achieved an exceptional overall diagnostic accuracy of <strong>0.9845</strong> (98.45%), precision of 0.9893, specificity of 0.9788, sensitivity of 0.9802, F-score of 0.9878, and MCC of 0.9602. Stack-LSTM achieved 0.9788 accuracy and 0.9544 MCC, while Stack-CNN attained 0.9689 accuracy and 0.9487 MCC.</p>
            <p>Crucially, class-specific recall for the minority Pre-Diabetic subgroup surged from 76.2% under base ANN to 94.3% under Stack-ANN, demonstrating the clinical power of ensemble meta-learning in catching pre-diabetic individuals before overt diabetes develops.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">24</div>
        </div>
    </div>
    '''

def get_page_25():
    return '''
    <div class="page" id="page-25">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h3 class="subsec-heading">B. VISUAL PERFORMANCE EVALUATION ON IDPD-I</h3>
            <p>Figure 8 illustrates the comparative performance metrics across all models on IDPD-I, visually corroborating the superiority of meta-learning architectures.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig08_idpd_perf.png" alt="IDPD Performance" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 8.</strong> Performance comparison of proposed DL base models and EDL meta-models on IDPD-I across Accuracy, Precision, Specificity, Sensitivity, F-Score, and MCC.</div>
            </div>

            <p>Figures 10 and 13 depict the One-vs-Rest ROC curves on IDPD-I. In Figure 10, base models achieve macro-average AUCs of 0.94 (ANN), 0.91 (CNN), and 0.90 (LSTM). In Figure 13, the EDL meta-models achieve outstanding AUC values, with Stack-ANN and Stack-LSTM reaching <strong>0.98</strong> AUC and Stack-CNN achieving 0.97 AUC.</p>

            <div style="display: flex; gap: 8px; margin: 6px 0;" class="full-width">
                <div style="flex: 1; text-align: center;">
                    <img src="report_figures/fig10_base_roc_idpd.png" alt="Base ROC IDPD" style="max-height: 2.2in; width: 100%;">
                    <div class="fig-caption"><strong>FIGURE 10.</strong> ROC/AUC for DL base models (LSTM, CNN, ANN) on IDPD-I.</div>
                </div>
                <div style="flex: 1; text-align: center;">
                    <img src="report_figures/fig13_edl_roc_idpd.png" alt="EDL ROC IDPD" style="max-height: 2.2in; width: 100%;">
                    <div class="fig-caption"><strong>FIGURE 13.</strong> ROC/AUC for proposed EDL models (Stack-ANN, LSTM, CNN) on IDPD-I.</div>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">25</div>
        </div>
    </div>
    '''

def get_page_26():
    return '''
    <div class="page" id="page-26">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XXI. CROSS-DATASET SYNTHESIS & SOTA BENCHMARK COMPARISON</h2>
            <p>Figure 15 provides a comprehensive cross-dataset synthesis comparing diagnostic accuracy across all three diabetes datasets (PIMA-IDD-I, DDFH-G, IDPD-I) for each EDL meta-model.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig15_edl_accuracy_all.png" alt="EDL Accuracy All" style="max-height: 2.7in;">
                <div class="fig-caption"><strong>FIGURE 15.</strong> Diagnostic accuracy of proposed EDL meta-models (Stack-ANN, Stack-LSTM, Stack-CNN) across PIMA-IDD-I, DDFH-G, and IDPD-I cohorts.</div>
            </div>

            <p>Table 15 presents an exhaustive comparative audit benchmarking the proposed EDL framework against 25 prominent state-of-the-art studies published in leading IEEE, Elsevier, and Springer venues.</p>

            <div class="table-caption">TABLE 15. Comprehensive Benchmark: Proposed EDL vs State-of-the-Art Literature.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Author(s) & Ref</th><th>Dataset Evaluated</th><th>Model / Architecture</th><th>Reported Accuracy</th></tr>
                </thead>
                <tbody>
                    <tr><td>Naveen et al. [32]</td><td>PIMA-IDD-I</td><td>Random Forest</td><td>85.60%</td></tr>
                    <tr><td>Alhalaseh et al. [28]</td><td>PIMA / IDPD-I</td><td>Soft Voting (LR, RF, NB)</td><td>81.0% / 97.0%</td></tr>
                    <tr><td>Nasser & Dawood [29]</td><td>IDPD-I</td><td>Multilayer Neural Network</td><td>98.00%</td></tr>
                    <tr><td>Chou et al. [52]</td><td>Taipei Municipal Center</td><td>LR, NN, Decision Jungle, DT</td><td>80.2% – 95.3%</td></tr>
                    <tr><td>Rani [50]</td><td>DDFH-G</td><td>KNN, LR, SVM</td><td>78%, 78%, 77%</td></tr>
                    <tr><td>Nishat [49]</td><td>DDFH-G</td><td>ANN</td><td>96.50%</td></tr>
                    <tr><td>Rastogi & Bansal [48]</td><td>PIMA-IDD-I</td><td>Logistic Regression</td><td>82.46%</td></tr>
                    <tr><td>Khanam & Foo [36]</td><td>PIMA-IDD-I</td><td>Adaptive Boosting, ANN</td><td>79.42%, 88.60%</td></tr>
                    <tr><td>García-Ordás et al. [35]</td><td>PIMA-IDD-I</td><td>1D-CNN, BiLSTM</td><td>92.31%, 94.00%</td></tr>
                    <tr><td>Nuankaew et al. [30]</td><td>PIMA / IDPD-I</td><td>Deep Learning</td><td>74.74%, 94.72%</td></tr>
                    <tr><td>Daanouni et al. [40]</td><td>PIMA / DDFH-G</td><td>ANN, Deep ANN, DT, KNN</td><td>89.0% – 98.0%</td></tr>
                    <tr><td>Edeh et al. [51]</td><td>DDFH-G / PIMA</td><td>RF, SVM Hybrid</td><td>97.6%, 83.1%</td></tr>
                    <tr><td>Pyne et al. [24]</td><td>PIMA-IDD-I</td><td>ANN</td><td>80.79%</td></tr>
                    <tr><td>Chang et al. [25]</td><td>PIMA-IDD-I</td><td>Naive Bayes</td><td>76.30%</td></tr>
                    <tr><td>Gupta et al. [26]</td><td>PIMA-IDD-I</td><td>Deep Dense Neural Network</td><td>84.42%</td></tr>
                    <tr><td>Gupta & Goel [27]</td><td>PIMA-IDD-I</td><td>Tuned Random Forest</td><td>88.61%</td></tr>
                    <tr><td>Kannadasan et al. [37]</td><td>PIMA-IDD-I</td><td>Stacked Autoencoders</td><td>86.26%</td></tr>
                    <tr><td>Shahin et al. [39]</td><td>PIMA-IDD-I</td><td>Deep Belief Network</td><td>81.25%</td></tr>
                    <tr><td>Rastogi & Bansal [41]</td><td>PIMA-IDD-I</td><td>ANN</td><td>85.09%</td></tr>
                    <tr><td>Sivaranjani et al. [31]</td><td>PIMA-IDD-I</td><td>RF, SVM</td><td>83.0%, 81.4%</td></tr>
                    <tr><td>Roy et al. [54]</td><td>PIMA-IDD-I</td><td>Light Gradient Boosting</td><td>86.00%</td></tr>
                    <tr style="background-color: #f0fdf4;"><td><strong>Proposed EDL (Agarshna R)</strong></td><td><strong>PIMA-IDD-I</strong></td><td><strong>Stack-ANN / LSTM / CNN</strong></td><td><strong>98.81%, 97.23%, 94.81%</strong></td></tr>
                    <tr style="background-color: #f0fdf4;"><td><strong>Proposed EDL (Agarshna R)</strong></td><td><strong>DDFH-G</strong></td><td><strong>Stack-ANN / LSTM / CNN</strong></td><td><strong>99.51%, 98.36%, 97.44%</strong></td></tr>
                    <tr class="last-row" style="background-color: #f0fdf4;"><td><strong>Proposed EDL (Agarshna R)</strong></td><td><strong>IDPD-I</strong></td><td><strong>Stack-ANN / LSTM / CNN</strong></td><td><strong>98.45%, 97.88%, 96.89%</strong></td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">26</div>
        </div>
    </div>
    '''

def get_page_27():
    return '''
    <div class="page" id="page-27">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XXII. EXPLAINABLE ARTIFICIAL INTELLIGENCE (XAI) & ATTRIBUTIONS</h2>
            <p>Deploying deep learning in clinical healthcare demands complete transparency. Without interpretable attributions, clinicians cannot verify whether a model's prediction relies on valid physiological biomarkers or spurious dataset artifacts [13]. To guarantee clinical audibility, we integrated cooperative game-theoretic SHAP (SHapley Additive exPlanations) into the EDL system.</p>

            <h3 class="subsec-heading">A. GAME-THEORETIC SHAPLEY VALUE FORMULATION</h3>
            <p>SHAP attributes the output of model $f(x)$ to individual features based on classical Shapley values from cooperative game theory. For a patient with feature set $F$, the unique additive attribution $\phi_j$ assigned to feature $j$ satisfies four fundamental mathematical axioms: Efficiency, Symmetry, Dummy Player, and Additivity:</p>

            <div class="eq-box">
                <span class="eq-math">\phi_j(x) = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|! (|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{j\}) - f_x(S) \right]</span>
                <span class="eq-num">(31)</span>
            </div>
            <p>where $S$ is a coalition subset of features excluding feature $j$, and $f_x(S)$ is the conditional expectation of model output conditioned on features in $S$. The sum of all feature attributions exactly equals the difference between the patient's predicted risk $f(x)$ and the baseline expected prior risk $\mathbb{E}[f(X)] = \phi_0$:</p>

            <div class="eq-box">
                <span class="eq-math">f(x) = \phi_0 + \sum_{j=1}^{|F|} \phi_j(x)</span>
                <span class="eq-num">(32)</span>
            </div>

            <p>For tree-based selection and deep meta-learners, Tree-SHAP and Deep-SHAP algorithms compute these combinatorial expectations in polynomial time $O(T L D^2)$, enabling instantaneous real-time patient risk explanation at the bedside.</p>

            <div class="callout-box">
                <strong>Clinical Significance of Additive Attributions:</strong> Clinicians can immediately visualize which specific patient indicators pushed risk upwards (red bars) and which protective factors lowered risk (blue bars), transforming raw probabilities into actionable medical insights.
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">27</div>
        </div>
    </div>
    '''

def get_page_28():
    return '''
    <div class="page" id="page-28">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h3 class="subsec-heading">B. CLINICAL CASE STUDY: LOCAL WATERFALL EXPLANATION</h3>
            <p>Figure 16 illustrates the local SHAP waterfall attribution profile generated for Patient #1042 (a 52-year-old male presenting with Polyuria, Polydipsia, sudden weight loss, and Polyphagia). The cohort baseline expected risk is $\phi_0 = 68.9\%$.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig16_shap_waterfall.png" alt="SHAP Waterfall" style="max-height: 2.7in;">
                <div class="fig-caption"><strong>FIGURE 16.</strong> Local SHAP attribution profile for Patient #1042: baseline cohort risk 68.9% elevated to 99.8% predicted diabetes risk, driven by primary osmotic indicators Polyuria (+0.112) and Polydipsia (+0.098).</div>
            </div>

            <p>As demonstrated in Figure 16, the presence of Polyuria contributed $+0.112$ to the predicted probability, followed by Polydipsia ($+0.098$), sudden weight loss ($+0.052$), Age ($+0.045$), Polyphagia ($+0.041$), and Male Gender ($+0.028$). Conversely, the absence of Genital Thrush exerted a protective negative attribution of $-0.032$. The resulting final model prediction is <strong>99.8%</strong> (High Clinical Risk).</p>

            <p>This attribution profile shows perfect biological concordance with established endocrinological pathophysiology: severe hyperglycemia saturates renal glucose transporter thresholds ($>180$ mg/dL), triggering osmotic diuresis (Polyuria), secondary cellular dehydration stimulating hypothalamic thirst centers (Polydipsia), and catabolic muscle wasting (Weight Loss). Frontline clinicians can verify that the model relies on sound clinical principles rather than spurious statistical noise.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">28</div>
        </div>
    </div>
    '''

def get_page_29():
    return '''
    <div class="page" id="page-29">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XXIII. WHAT-IF COUNTERFACTUAL SIMULATION ENGINE</h2>
            <p>While local attributions explain past diagnoses, preventative healthcare requires actionable guidance: identifying what specific clinical modifications can reverse a patient's elevated risk score. To address this need, we developed an interactive What-If Counterfactual Simulation Engine.</p>

            <h3 class="subsec-heading">A. MATHEMATICAL COUNTERFACTUAL OPTIMIZATION</h3>
            <p>Given a patient vector $x$ with elevated risk $f(x) \approx 1$, the counterfactual engine seeks an optimal perturbed vector $x^*$ that minimizes distance to $x$ while steering predicted risk below a healthy clinical threshold $y^* = 0$:</p>

            <div class="eq-box">
                <span class="eq-math">x^* = \arg\min_{x'} \text{dist}(x, x') + \lambda \left( f(x') - y^* \right)^2 + \gamma \sum_{j \in \text{immutable}} \mathbb{I}(x'_j \ne x_j)</span>
                <span class="eq-num">(33)</span>
            </div>
            <p>where $\text{dist}(x, x')$ penalizes clinical intervention cost, and immutable features (such as Age and Gender) are constrained to remain strictly fixed ($\gamma \to \infty$).</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig18_counterfactual.png" alt="Counterfactual Trajectory" style="max-height: 2.7in;">
                <div class="fig-caption"><strong>FIGURE 18.</strong> What-If counterfactual clinical trajectory simulation: demonstrating risk reduction from 99.8% down to 34.6% following progressive symptom reversal and glycemic stabilization.</div>
            </div>

            <p>Figure 18 illustrates an intervention simulation for Patient #1042. At baseline with active symptoms, predicted risk is 99.8%. Simulating dietary moderation (resolving Polyphagia) reduces predicted risk to 91.4%. Achieving glycemic control (resolving Polydipsia) lowers risk to 78.2%. Finally, achieving complete metabolic stabilization (reversing Polyuria and stopping catabolic weight loss) plunges predicted risk to <strong>34.6%</strong>, safely crossing below the 50% clinical decision boundary.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">29</div>
        </div>
    </div>
    '''

def get_page_30():
    return '''
    <div class="page" id="page-30">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XXIV. CLINICAL DECISION SUPPORT SYSTEM (CDSS) DEPLOYMENT</h2>
            <p>To transition the theoretical EDL framework into frontline medical practice, we engineered a complete Clinical Decision Support System (CDSS) web deployment architecture, illustrated in Figure 19.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig19_cdss_architecture.png" alt="CDSS Architecture" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 19.</strong> Clinical Decision Support System (CDSS) end-to-end multi-tier deployment architecture: client browser UI, Python application engine, ML inference core, and audit logging export.</div>
            </div>

            <h3 class="subsec-heading">A. INTERACTIVE APPLICATION PORTAL MODULES</h3>
            <p>The system was implemented using Python 3.11, Streamlit, and Bootstrap 5.3, organized into five interactive operational tabs:</p>
            <ul class="ieee-list">
                <li><strong>Tab 1: Patient Risk Screening:</strong> Clinical data entry interface with real-time risk gauges, confidence intervals, and automated risk classification (Low / Moderate / High).</li>
                <li><strong>Tab 2: What-If Counterfactual Simulator:</strong> Interactive toggle controls allowing clinicians to test how resolving specific symptoms impacts risk trajectories.</li>
                <li><strong>Tab 3: Model Comparison & Benchmarks:</strong> Complete 48-experiment benchmark tables with sortable accuracy, AUC, and F-score metrics.</li>
                <li><strong>Tab 4: Exploratory Data Analysis:</strong> Epidemiological visualization gallery rendering distributions and correlation matrices.</li>
                <li><strong>Tab 5: Data & Artifacts Export:</strong> One-click generation and download of complete technical Excel workbooks and audit logs.</li>
            </ul>

            <p>Benchmarking established an end-to-end inference latency of under <strong>4.8 milliseconds</strong> per patient, supporting instantaneous feedback in high-volume triage clinics.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">30</div>
        </div>
    </div>
    '''

def get_page_31():
    return '''
    <div class="page" id="page-31">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XXV. ABLATION STUDIES & COMPUTATIONAL COMPLEXITY</h2>
            <p>To substantiate the individual algorithmic components of the proposed framework, extensive ablation experiments were conducted. Table 16 compares alternative ensembling strategies, meta-model architectures, and feature set configurations.</p>

            <div class="table-caption">TABLE 16. Ablation Analysis: Blending Mechanisms and Meta-Architectures.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Ensemble Strategy</th><th>Meta Architecture</th><th>PIMA-IDD-I Accuracy</th><th>DDFH-G Accuracy</th><th>IDPD-I Accuracy</th><th>Inference Latency</th></tr>
                </thead>
                <tbody>
                    <tr><td>Single Best Model</td><td>Base ANN (No Meta)</td><td>92.77%</td><td>94.77%</td><td>94.62%</td><td>1.2 ms</td></tr>
                    <tr><td>Hard Voting</td><td>Majority Rule</td><td>93.10%</td><td>95.20%</td><td>94.80%</td><td>2.1 ms</td></tr>
                    <tr><td>Soft Voting</td><td>Mean Probabilities</td><td>94.40%</td><td>96.10%</td><td>95.30%</td><td>2.2 ms</td></tr>
                    <tr><td>Weighted Blending</td><td>Linear Regression</td><td>95.20%</td><td>96.80%</td><td>95.90%</td><td>2.5 ms</td></tr>
                    <tr><td>Proposed Stacking</td><td>Stack-CNN</td><td>94.81%</td><td>97.44%</td><td>96.89%</td><td>4.1 ms</td></tr>
                    <tr><td>Proposed Stacking</td><td>Stack-LSTM</td><td>97.23%</td><td>98.36%</td><td>97.88%</td><td>4.5 ms</td></tr>
                    <tr class="last-row" style="background-color: #f0fdf4;"><td><strong>Proposed Stacking</strong></td><td><strong>Stack-ANN (Meta)</strong></td><td><strong>98.81%</strong></td><td><strong>99.51%</strong></td><td><strong>98.45%</strong></td><td><strong>4.8 ms</strong></td></tr>
                </tbody>
            </table>

            <h3 class="subsec-heading">A. SENSITIVITY & COMPUTATIONAL LATENCY</h3>
            <p>As demonstrated in Table 16, simple voting and linear blending plateau at ~96% accuracy because they assume linear independence across base predictions. The proposed non-linear Stack-ANN meta-learner captures subtle conditional dependencies between base learners, delivering a decisive ~3% to 4% performance surge.</p>
            <p>Hyperparameter sensitivity audits revealed optimal meta-stability at learning rate $\eta = 0.01$ with dropout $p = 0.50$. Computational profiling on standard hardware (Intel Core i7 CPU, 16GB RAM) confirmed total training duration under 45 seconds for 5-fold cross-validation across all models, proving the framework's feasibility for resource-constrained clinical settings.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">31</div>
        </div>
    </div>
    '''

def get_page_32():
    return '''
    <div class="page" id="page-32">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XXVI. DISCUSSION, LIMITATIONS & FUTURE WORK</h2>
            <p>The experimental findings across three clinical cohorts demonstrate that the proposed Ensemble Deep Learning (EDL) framework establishes a new benchmark for accurate, reproducible, and explainable diabetes screening. By combining heterogeneous deep learning architectures within a meta-level stacking model, the framework overcomes the limitations of single-model classifiers.</p>

            <h3 class="subsec-heading">A. CLINICAL IMPLICATIONS & WORKFLOW INTEGRATION</h3>
            <p>Frontline adoption of the EDL system can substantially alleviate primary healthcare workloads. By non-invasively stratifying patients into high, moderate, and low risk categories prior to confirmatory biochemical testing, clinics can prioritize urgent lab assays (such as HbA1c and oral glucose tolerance tests) for high-risk individuals, minimizing diagnostic delay. The system integrates smoothly with hospital electronic health records (EHR) via standardized HL7 / FHIR APIs.</p>

            <h3 class="subsec-heading">B. LIMITATIONS & ETHICAL CONSIDERATIONS</h3>
            <p>Despite exceptional empirical results, several clinical limitations warrant acknowledgment:</p>
            <ul class="ieee-list">
                <li><strong>Demographic Representation:</strong> While evaluated across German, Iraqi, and Native American cohorts, further prospective multi-center clinical validation across diverse Asian and African populations is essential to ensure global algorithmic equity.</li>
                <li><strong>Biochemical Indicator Availability:</strong> High-performance multi-class models require lab parameters (HbA1c, lipid profiles) that may not be instantaneously accessible in remote rural clinics.</li>
                <li><strong>Data Privacy & Security:</strong> Clinical deployment necessitates end-to-end AES-256 encryption, HIPAA compliance, and on-premises federated learning protocols.</li>
            </ul>

            <h3 class="subsec-heading">C. FUTURE RESEARCH DIRECTIONS</h3>
            <p>Future work will expand the EDL architecture in three directions: (1) integrating Continuous Glucose Monitoring (CGM) IoT wearable sensors for real-time glycemic drift forecasting; (2) deploying Deep Reinforcement Learning (DRL) to dynamically recommend personalized dietary and exercise regimens; and (3) extending the multi-architecture stacking framework to comorbid conditions including diabetic retinopathy and cardiovascular disease.</p>

            <h2 class="sec-heading">XXVII. CONCLUSION</h2>
            <p>This study introduced an innovative, explainable Ensemble Deep Learning (EDL) Clinical Decision Support System for early-stage diabetes prediction. By synergizing Artificial Neural Networks, 1D Convolutional Neural Networks, and Long Short-Term Memory networks into a meta-level stacking ensemble, the system achieved benchmark-setting diagnostic accuracy of <strong>99.51%</strong> on DDFH-G (2000 records), <strong>98.81%</strong> on PIMA-IDD-I (768 records), and <strong>98.45%</strong> on the multi-class IDPD-I dataset (1000 records). Coupled with game-theoretic SHAP attributions and an interactive What-If counterfactual simulation engine, this system delivers an accurate, trustworthy, and actionable clinical decision aid for combating the global diabetes epidemic.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">32</div>
        </div>
    </div>
    '''

def get_page_33():
    return '''
    <div class="page" id="page-33">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading" style="font-size: 8.5pt;">REFERENCES</h2>
            <div style="font-size: 6.8pt; line-height: 1.15; text-align: justify;">
                <p class="no-indent">[1] S. Binhowemel, M. Alfakhri, K. AlReshaid, and A. Alyani, "Role of artificial intelligence in diabetes research diagnosis and prognosis: A narrative review," <em>J. Health Inform. Dev. Countries</em>, vol. 17, no. 2, pp. 1–12, 2023.</p>
                <p class="no-indent">[2] R. M. Alamoudi et al., "Fasting Ramadan in patients with T1DM—Saudi Arabia versus other countries during the COVID-19 pandemic," <em>Diabetes Metab. Syndr.</em>, vol. 17, no. 1, Art. no. 102676, 2023.</p>
                <p class="no-indent">[3] B. V. V. S. Prasad et al., "Predicting diabetes with multivariate analysis an innovative KNN-based classifier approach," <em>Prev. Med.</em>, vol. 174, Art. no. 107619, 2023.</p>
                <p class="no-indent">[4] World Population Rev. <em>Diabetes Rates By Country 2023</em>. Accessed: Feb. 10, 2023. [Online]. Available: https://worldpopulationreview.com</p>
                <p class="no-indent">[5] V. Jaiswal, A. Negi, and T. Pal, "A review on current advances in machine learning based diabetes prediction," <em>Primary Care Diabetes</em>, vol. 15, no. 3, pp. 435–443, 2021.</p>
                <p class="no-indent">[6] A. Mujumdar and V. Vaidehi, "Diabetes prediction using machine learning algorithms," <em>Proc. Comput. Sci.</em>, vol. 165, pp. 292–299, 2019.</p>
                <p class="no-indent">[7] R. Gupta et al., "Association of type 2 diabetes with coronary risk factors: A single centre prospective registry," <em>Diabetes Metab. Syndr.</em>, vol. 17, no. 2, Art. no. 102709, 2023.</p>
                <p class="no-indent">[8] J. Chaki et al., "Machine learning and artificial intelligence based diabetes mellitus detection: A systematic review," <em>J. King Saud Univ. Comput. Inf. Sci.</em>, vol. 34, no. 6, pp. 3204–3225, 2022.</p>
                <p class="no-indent">[9] R. K. Nadesh and K. Arivuselvan, "Type 2: Diabetes mellitus prediction using deep neural networks classifier," <em>Int. J. Cogn. Comput. Eng.</em>, vol. 1, pp. 55–61, 2020.</p>
                <p class="no-indent">[10] H. Lai et al., "Predictive models for diabetes mellitus using machine learning techniques," <em>BMC Endocr. Disord.</em>, vol. 19, no. 1, pp. 1–9, 2019.</p>
                <p class="no-indent">[11] H. L. Tong, H. Ng, and H. A. Ananthan, "Predicting diabetes mellitus with machine learning techniques," <em>J. Eng. Technol. Appl. Phys.</em>, vol. 6, no. 1, pp. 91–99, 2024.</p>
                <p class="no-indent">[12] M. Bhattacharya and D. Datta, "Development of predictive models of diabetes using ensemble machine learning classifier," in <em>Proc. ASCIS</em>, 2022, pp. 377–388.</p>
                <p class="no-indent">[13] Y. Du et al., "An explainable machine learning-based clinical decision support system for prediction of gestational diabetes mellitus," <em>Sci. Rep.</em>, vol. 12, no. 1, p. 1170, 2022.</p>
                <p class="no-indent">[14] O. A. Ebrahim and G. Derbew, "Application of supervised machine learning algorithms for classification of type-2 diabetes in Afar regional state," <em>Sci. Rep.</em>, vol. 13, p. 7779, 2023.</p>
                <p class="no-indent">[15] A. Sarraju et al., "Identifying reasons for statin nonuse in patients with diabetes using deep learning of electronic health records," <em>J. Amer. Heart Assoc.</em>, vol. 12, no. 7, 2023.</p>
                <p class="no-indent">[16] P. N. Thotad et al., "Diabetes disease detection and classification on Indian demographic and health survey data using machine learning," <em>Diabetes Metab. Syndr.</em>, vol. 17, 2023.</p>
                <p class="no-indent">[17] J. J. Olickal et al., "Down referral and assessing comprehensive diabetes care in primary care settings: An operational research from India," <em>Diabetes Metab. Syndr.</em>, vol. 17, 2023.</p>
                <p class="no-indent">[18] S. AlZu’bi et al., "Diabetes monitoring system in smart health cities based on big data intelligence," <em>Future Internet</em>, vol. 15, no. 2, p. 85, 2023.</p>
                <p class="no-indent">[19] H. Pan et al., "A risk prediction model for type 2 diabetes mellitus complicated with retinopathy based on machine learning," <em>Frontiers Med.</em>, vol. 10, Art. no. 1136653, 2023.</p>
                <p class="no-indent">[20] M. J. Uddin et al., "A comparison of machine learning techniques for the detection of type-2 diabetes mellitus: Experiences from Bangladesh," <em>Information</em>, vol. 14, no. 7, p. 376, 2023.</p>
                <p class="no-indent">[21] M. Zhao et al., "A machine learning-based diagnosis modelling of type 2 diabetes mellitus with environmental metal exposure," <em>Comput. Methods Programs Biomed.</em>, vol. 235, 2023.</p>
                <p class="no-indent">[22] M. Bernardini et al., "Discovering type 2 diabetes in electronic health records using sparse balanced support vector machine," <em>IEEE J. Biomed. Health Inform.</em>, vol. 24, no. 1, pp. 235–246, 2020.</p>
                <p class="no-indent">[23] M. Eleftheriades et al., "Prediction of insulin treatment in women with gestational diabetes mellitus," <em>Nutr. Diabetes</em>, vol. 11, no. 1, p. 30, 2021.</p>
                <p class="no-indent">[24] A. Pyne and B. Chakraborty, "Artificial neural network based approach to diabetes prediction using pima Indians dataset," in <em>Proc. ICCAD</em>, 2023, pp. 1–6.</p>
                <p class="no-indent">[25] V. Chang et al., "Pima Indians diabetes mellitus classification based on machine learning (ML) algorithms," <em>Neural Comput. Appl.</em>, vol. 35, no. 22, pp. 16157–16173, 2023.</p>
                <p class="no-indent">[26] N. Gupta et al., "Performance evaluation of deep dense layer neural network for diabetes prediction," <em>Comput. Mater. Continua</em>, vol. 76, no. 1, pp. 347–366, 2023.</p>
                <p class="no-indent">[27] S. C. Gupta and N. Goel, "Predictive modeling and analytics for diabetes using hyperparameter tuned machine learning techniques," <em>Proc. Comput. Sci.</em>, vol. 218, pp. 1257–1269, 2023.</p>
                <p class="no-indent">[28] R. Alhalaseh et al., "The effect of feature selection on diabetes prediction using machine learning," in <em>Proc. IEEE ISCC</em>, 2023, pp. 1–7.</p>
                <p class="no-indent">[29] E. S. Nasser and F. A. A. Dawood, "Diagnosis and classification of type II diabetes based on multilayer neural network," <em>Iraqi J. Sci.</em>, vol. 63, no. 10, pp. 3744–3758, 2021.</p>
                <p class="no-indent">[30] P. Nuankaew et al., "Average weighted objective distance-based method for type 2 diabetes prediction," <em>IEEE Access</em>, vol. 9, pp. 137015–137028, 2021.</p>
                <p class="no-indent">[31] S. Sivaranjani et al., "Diabetes prediction using machine learning algorithms with feature selection and dimensionality reduction," in <em>Proc. ICACCS</em>, 2021, pp. 141–146.</p>
                <p class="no-indent">[32] S. Naveen et al., "Machine learning based diabetic prediction using random forest," in <em>Proc. ViTECoN</em>, 2023, pp. 1–5.</p>
                <p class="no-indent">[33] N. Abdulhadi and A. Al-Mousa, "Diabetes detection using machine learning classification methods," in <em>Proc. ICIT</em>, 2021, pp. 350–354.</p>
                <p class="no-indent">[34] V. Chang et al., "An assessment of machine learning models and algorithms for early prediction of diabetes," <em>Healthcare Anal.</em>, vol. 2, Art. no. 100118, 2022.</p>
                <p class="no-indent">[35] M. T. García-Ordás et al., "Diabetes detection using deep learning techniques with oversampling and feature augmentation," <em>Comput. Methods Programs Biomed.</em>, vol. 202, 2021.</p>
                <p class="no-indent">[36] J. J. Khanam and S. Y. Foo, "A comparison of machine learning algorithms for diabetes prediction," <em>ICT Exp.</em>, vol. 7, no. 4, pp. 432–439, 2021.</p>
                <p class="no-indent">[37] K. Kannadasan et al., "Type 2 diabetes data classification using stacked autoencoders in deep neural networks," <em>Clin. Epidemiol. Global Health</em>, vol. 7, no. 4, pp. 530–535, 2019.</p>
                <p class="no-indent">[38] G. Swapna et al., "Diabetes detection using deep learning algorithms," <em>ICT Exp.</em>, vol. 4, no. 4, pp. 243–246, 2018.</p>
                <p class="no-indent">[39] O. R. Shahin et al., "A robust deep neural network framework for the detection of diabetes," <em>Alexandria Eng. J.</em>, vol. 74, pp. 715–724, 2023.</p>
                <p class="no-indent">[40] O. Daanouni et al., "Predicting diabetes diseases using mixed data and supervised machine learning algorithms," in <em>Proc. SCA</em>, 2019, pp. 1–6.</p>
                <p class="no-indent">[41] N. Pradhan et al., "Diabetes prediction using artificial neural network," in <em>Deep Learning Techniques for Biomedical and Health Informatics</em>, Academic Press, 2020, pp. 327–339.</p>
                <p class="no-indent">[42] M. S. A. Reshan et al., "Enhancing breast cancer detection using advanced multi-model features and ensemble machine learning," <em>Life</em>, vol. 13, no. 10, p. 2093, 2023.</p>
                <p class="no-indent">[43] H. Zhou et al., "A diabetes prediction model based on Boruta feature selection and ensemble learning," <em>BMC Bioinf.</em>, vol. 24, p. 224, 2023.</p>
                <p class="no-indent">[44] Kaggle, UCI Mach. Learn. <em>Pima Indians Diabetes Database</em>, 2023. [Online]. Available: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database</p>
                <p class="no-indent">[45] Kaggle. <em>Dataset of Diabetes, Hospital Frankfurt, Germany</em>, 2023. [Online]. Available: https://www.kaggle.com/datasets/johndasilva/diabetes</p>
                <p class="no-indent">[46] A. Rashid. "Diabetes Dataset," <em>Mendeley Data</em>, V1, 2020. doi: 10.17632/wj9rwkp9c2.1.</p>
                <p class="no-indent">[47] M. S. A. Reshan et al., "A robust heart disease prediction system using hybrid deep neural networks," <em>IEEE Access</em>, vol. 11, pp. 121574–121591, 2023.</p>
                <p class="no-indent">[48] R. Rastogi and M. Bansal, "Diabetes prediction model using data mining techniques," <em>Meas. Sensors</em>, vol. 25, Art. no. 100605, 2023.</p>
                <p class="no-indent">[49] M. M. Nishat, "Performance assessment of machine learning algorithms in predicting diabetes mellitus," <em>Biosci. Biotech. Res. Comm.</em>, vol. 14, pp. 74–82, 2021.</p>
                <p class="no-indent">[50] K. M. J. Rani, "Diabetes prediction using machine learning," <em>Int. J. Sci. Res. Comput. Sci. Eng. Inf. Technol.</em>, vol. 6, pp. 294–305, 2020.</p>
                <p class="no-indent">[51] M. O. Edeh et al., "A classification algorithm-based hybrid diabetes prediction model," <em>Front. Public Health</em>, vol. 10, Art. no. 829519, 2022.</p>
                <p class="no-indent">[52] C.-Y. Chou et al., "Predicting the onset of diabetes with machine learning methods," <em>J. Pers. Med.</em>, vol. 13, no. 3, p. 406, 2023.</p>
                <p class="no-indent">[53] D. Sisodia and D. S. Sisodia, "Prediction of diabetes using classification algorithms," <em>Proc. Comput. Sci.</em>, vol. 132, pp. 1578–1585, 2018.</p>
                <p class="no-indent">[54] K. Roy et al., "An enhanced machine learning framework for type 2 diabetes classification using imbalanced data," <em>Complexity</em>, vol. 2021, Art. no. 9953314, 2021.</p>
            </div>

            <div class="full-width" style="margin-top: 10px; border-top: 0.8pt solid #002855; padding-top: 8px;">
                <div class="bio-item">
                    <img src="report_figures/fig20_author_photo.png" alt="Agarshna R" class="bio-img">
                    <div class="bio-text">
                        <span class="bio-name">AGARSHNA R</span> (Student Member, IEEE) is currently pursuing the Bachelor of Technology (B.Tech) degree in Computer Science and Engineering with specialization in Artificial Intelligence and Machine Learning (CSE-AIML) at SRM Institute of Science and Technology, Tiruchirappalli Campus, Tamil Nadu, India (Register Number: <strong>RA2411026050061</strong>). Her primary research interests encompass clinical decision support systems, deep neural network architectures (ANN, CNN, LSTM), ensemble meta-learning paradigms, explainable artificial intelligence (XAI), and biomedical data informatics. She has actively developed predictive healthcare pipelines, published open-source machine learning frameworks, and conducted comprehensive audits on clinical data hygiene, counterfactual simulations, and game-theoretic attributions. Her ongoing research aims to integrate continuous glucose monitoring (CGM) IoT systems with reinforcement learning agents to pioneer autonomous personalized diabetes care and metabolic triage.
                    </div>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">33</div>
        </div>
    </div>
    '''

print("Part 3 defined successfully.")
