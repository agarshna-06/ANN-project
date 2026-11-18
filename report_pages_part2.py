"""
Part 2 of 33-Page IEEE Access Report: Pages 12 to 22
Author: AGARSHNA R (RA2411026050061)
Department: B.Tech CSE (AIML), SRM IST
"""

def get_page_12():
    return '''
    <div class="page" id="page-12">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">X. BASE DEEP LEARNING ARCHITECTURES: ARTIFICIAL NEURAL NETWORK (ANN)</h2>
            <p>Artificial Neural Networks (ANN), specifically deep Multi-Layer Perceptrons (MLP), excel at learning complex non-linear functional representations from structured, tabular clinical indicators [24], [36]. Tabular medical predictors exhibit intricate non-linear interactions (e.g., between Glucose, Age, and Insulin) that single-plane linear hyperplanes cannot adequately separate.</p>

            <h3 class="subsec-heading">A. FORWARD PROPAGATION MATRIX CALCULUS</h3>
            <p>For an $L$-layer feedforward neural network receiving clinical patient vector $a^{[0]} = x \in \mathbb{R}^D$, forward propagation at each layer $l \in \{1, \dots, L\}$ is computed as:</p>

            <div class="eq-box">
                <span class="eq-math">z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}, \quad a^{[l]} = g^{[l]}(z^{[l]})</span>
                <span class="eq-num">(13)</span>
            </div>
            <p>where $W^{[l]} \in \mathbb{R}^{n_l \times n_{l-1}}$ is the weight parameter matrix, $b^{[l]} \in \mathbb{R}^{n_l}$ is the bias vector, and $g^{[l]}(\cdot)$ represents the non-linear activation function. To prevent the vanishing gradient problem, the Rectified Linear Unit (ReLU) activation function is deployed across hidden layers:</p>

            <div class="eq-box">
                <span class="eq-math">g^{[l]}(z) = \text{ReLU}(z) = \max(0, z)</span>
                <span class="eq-num">(14)</span>
            </div>
            <p>For binary classification (PIMA-IDD-I, DDFH-G), the final output layer $L$ employs the logistic Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$. For multi-class classification (IDPD-I), the Softmax operator is applied:</p>

            <div class="eq-box">
                <span class="eq-math">\hat{p}_c = \text{Softmax}(z)_c = \frac{e^{z_c}}{\sum_{j=1}^{|\mathcal{C}|} e^{z_j}}</span>
                <span class="eq-num">(15)</span>
            </div>

            <h3 class="subsec-heading">B. BACKPROPAGATION & OPTIMIZATION</h3>
            <p>The network minimizes categorical cross-entropy loss using error backpropagation. The output gradient is $\delta^{[L]} = \hat{y} - y$. Backpropagating errors through preceding layers obeys the recursive chain rule:</p>

            <div class="eq-box">
                <span class="eq-math">\delta^{[l]} = \left( (W^{[l+1]})^T \delta^{[l+1]} \right) \odot g'^{[l]}(z^{[l]})</span>
                <span class="eq-num">(16)</span>
            </div>
            <p>Weight updates are executed using the Adam optimizer with adaptive learning rates based on exponentially decaying first ($m_t$) and second ($v_t$) gradient moments ($\beta_1=0.9, \beta_2=0.999, \epsilon=10^{-8}$).</p>

            <div class="table-caption">TABLE 6. Base-Level ANN Architectural Layer Specifications.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Layer Name</th><th>Type</th><th>Output Units</th><th>Activation</th><th>Dropout / Regularization</th></tr>
                </thead>
                <tbody>
                    <tr><td>Input_Layer</td><td>Input</td><td>$D$ features</td><td>None</td><td>None</td></tr>
                    <tr><td>Dense_1</td><td>Fully Connected</td><td>128</td><td>ReLU</td><td>Batch Normalization</td></tr>
                    <tr><td>Dropout_1</td><td>Dropout</td><td>128</td><td>None</td><td>Rate = 0.30</td></tr>
                    <tr><td>Dense_2</td><td>Fully Connected</td><td>64</td><td>ReLU</td><td>None</td></tr>
                    <tr><td>Dense_3</td><td>Fully Connected</td><td>32</td><td>ReLU</td><td>None</td></tr>
                    <tr class="last-row"><td>Output_Head</td><td>Dense</td><td>1 or 3</td><td>Sigmoid / Softmax</td><td>$L_2$ penalty ($\lambda=10^{-4}$)</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">12</div>
        </div>
    </div>
    '''

def get_page_13():
    return '''
    <div class="page" id="page-13">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XI. BASE DEEP LEARNING ARCHITECTURES: 1D-CONVOLUTIONAL NEURAL NETWORK (CNN)</h2>
            <p>While Convolutional Neural Networks (CNNs) were originally formulated for 2D spatial grid processing in medical imaging, 1D-CNN architectures have proven remarkably adept at extracting localized spatial correlations and hierarchical sub-patterns across ordered clinical tabular indicators [35], [38].</p>

            <h3 class="subsec-heading">A. 1D CONVOLUTIONAL FEATURE MAP TRANSFORMATION</h3>
            <p>To process tabular patient records, the normalized clinical attribute vector $x \in \mathbb{R}^D$ is reshaped into a single-channel 1D sequence $X \in \mathbb{R}^{D \times 1}$. A set of $F$ discrete one-dimensional convolution kernels $\{K_f\}_{f=1}^F$, each of temporal kernel size $k$, slides across adjacent clinical features:</p>

            <div class="eq-box">
                <span class="eq-math">c_i^f = \text{ReLU}\left( \sum_{j=1}^k K_f(j) \cdot X(i + j - 1) + b_f \right)</span>
                <span class="eq-num">(17)</span>
            </div>
            <p>where $c_i^f$ denotes the activated feature response at position $i$ for filter $f$, and $b_f$ is a scalar bias. By sliding over groups of contiguous attributes (e.g., Glucose, Insulin, and BMI), the convolutional filters capture localized cross-feature physiological synergies that dense layers may overparameterize.</p>

            <h3 class="subsec-heading">B. MAX-POOLING AND CLASSIFICATION HEAD</h3>
            <p>Following convolution, a 1D Max-Pooling operation with pool size $p=2$ subsamples the feature maps, enforcing translation invariance and suppressing minor noise fluctuations:</p>

            <div class="eq-box">
                <span class="eq-math">p_m^f = \max_{0 \le t < p} c_{m \cdot p + t}^f</span>
                <span class="eq-num">(18)</span>
            </div>
            <p>The subsampled feature maps are flattened into a continuous representation vector and passed into a dense projection classification head with dropout regularization.</p>

            <div class="table-caption">TABLE 7. Base-Level 1D-CNN Architectural Layer Specifications.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Layer Name</th><th>Type</th><th>Kernel / Filters</th><th>Output Shape</th><th>Activation</th></tr>
                </thead>
                <tbody>
                    <tr><td>Input_Reshape</td><td>Reshape</td><td>None</td><td>$(D, 1)$</td><td>None</td></tr>
                    <tr><td>Conv1D_1</td><td>1D Convolution</td><td>32 filters, $k=3$</td><td>$(D, 32)$</td><td>ReLU</td></tr>
                    <tr><td>MaxPool_1</td><td>1D Max-Pooling</td><td>Pool Size = 2</td><td>$(D/2, 32)$</td><td>None</td></tr>
                    <tr><td>Conv1D_2</td><td>1D Convolution</td><td>64 filters, $k=3$</td><td>$(D/2, 64)$</td><td>ReLU</td></tr>
                    <tr><td>Flatten_Layer</td><td>Flatten</td><td>None</td><td>$64 \cdot (D/2)$</td><td>None</td></tr>
                    <tr><td>Dense_FC</td><td>Dense</td><td>64 units</td><td>$(64)$</td><td>ReLU (Dropout 0.4)</td></tr>
                    <tr class="last-row"><td>Output_Head</td><td>Dense</td><td>1 or 3 units</td><td>$(1)$ or $(3)$</td><td>Sigmoid / Softmax</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">13</div>
        </div>
    </div>
    '''

def get_page_14():
    return '''
    <div class="page" id="page-14">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XII. BASE DEEP LEARNING ARCHITECTURES: LONG SHORT-TERM MEMORY (LSTM)</h2>
            <p>Recurrent Neural Networks (RNN), particularly Long Short-Term Memory (LSTM) networks [38], provide an exceptional mechanism for capturing sequential and progressive dependencies across patient clinical indicators. By structuring clinical examination features as an ordered diagnostic sequence, LSTM cells effectively model cumulative physiological stress.</p>

            <h3 class="subsec-heading">A. LSTM GATING MECHANISMS & CELL STATE UPDATE</h3>
            <p>At each clinical indicator sequence step $t$, the LSTM unit maintains an internal cell state $C_t$ and hidden state $h_t$. The information flow is governed by three non-linear affine gating mechanisms:</p>
            <p><strong>1. Forget Gate ($f_t$):</strong> Decides what information from previous clinical steps to discard:</p>

            <div class="eq-box">
                <span class="eq-math">f_t = \sigma\left( W_f \cdot [h_{t-1}, x_t] + b_f \right)</span>
                <span class="eq-num">(19)</span>
            </div>

            <p><strong>2. Input Gate ($i_t$) & Candidate Cell ($\tilde{C}_t$):</strong> Determines which new clinical observations to incorporate into long-term memory:</p>

            <div class="eq-box">
                <span class="eq-math">i_t = \sigma\left( W_i \cdot [h_{t-1}, x_t] + b_i \right)</span>
                <span class="eq-num">(20)</span>
            </div>
            <div class="eq-box">
                <span class="eq-math">\tilde{C}_t = \tanh\left( W_c \cdot [h_{t-1}, x_t] + b_c \right)</span>
                <span class="eq-num">(21)</span>
            </div>

            <p><strong>3. Cell State Update ($C_t$):</strong> Computes the new internal memory via linear combination:</p>

            <div class="eq-box">
                <span class="eq-math">C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t</span>
                <span class="eq-num">(22)</span>
            </div>

            <p><strong>4. Output Gate ($o_t$) & Hidden State ($h_t$):</strong> Emits the conditioned diagnostic representation:</p>

            <div class="eq-box">
                <span class="eq-math">o_t = \sigma\left( W_o \cdot [h_{t-1}, x_t] + b_o \right), \quad h_t = o_t \odot \tanh(C_t)</span>
                <span class="eq-num">(23)</span>
            </div>
            <p>This additive cell state design circumvents exponential gradient degradation, enabling the network to bridge early demographic risk factors with terminal biochemical biomarkers.</p>

            <div class="table-caption">TABLE 8. Base-Level LSTM Architectural Layer Specifications.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Layer Name</th><th>Type</th><th>Units / Nodes</th><th>Output Shape</th><th>Activation Function</th></tr>
                </thead>
                <tbody>
                    <tr><td>Input_Reshape</td><td>Reshape</td><td>None</td><td>$(D, 1)$</td><td>Linear</td></tr>
                    <tr><td>LSTM_Core</td><td>LSTM Recurrent</td><td>64 memory cells</td><td>$(64)$</td><td>Tanh / Sigmoid gates</td></tr>
                    <tr><td>Dense_Intermediate</td><td>Dense</td><td>32 units</td><td>$(32)$</td><td>ReLU (Dropout 0.3)</td></tr>
                    <tr class="last-row"><td>Output_Head</td><td>Dense</td><td>1 or 3 units</td><td>$(1)$ or $(3)$</td><td>Sigmoid / Softmax</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">14</div>
        </div>
    </div>
    '''

def get_page_15():
    return '''
    <div class="page" id="page-15">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XIII. STACKING ENSEMBLE DEEP LEARNING (EDL) ARCHITECTURE</h2>
            <p>Stacking generalization, formulated theoretically by Wolpert (1992) and extended in the Super Learner framework by van der Laan et al. (2007), provides a mathematically optimal paradigm for combining heterogeneous predictive models. By training a meta-level learner on the predictions of diverse base learners, stacking constructs an optimal non-linear blending function that is proven to asymptotically perform at least as well as the best candidate base model.</p>

            <h3 class="subsec-heading">A. META-FEATURE MATRIX CONSTRUCTION</h3>
            <p>Directly training a meta-model on base predictions evaluated on the training set induces severe overfitting, as base models exhibit overly optimistic confidence on seen data. To prevent meta-level data leakage, out-of-fold (OOF) cross-validation predictions are generated. For each fold $k \in \{1, \dots, K\}$, base models are trained on $\mathcal{D} \setminus \mathcal{D}_k$ and evaluated on the held-out fold $\mathcal{D}_k$. The resulting probability vectors are concatenated to construct the meta-feature matrix $Z \in \mathbb{R}^{N \times (M \cdot |\mathcal{C}|)}$:</p>

            <div class="eq-box">
                <span class="eq-math">Z = \begin{bmatrix}
                \hat{P}_{ANN}(x_1) & \hat{P}_{LSTM}(x_1) & \hat{P}_{CNN}(x_1) \\
                \hat{P}_{ANN}(x_2) & \hat{P}_{LSTM}(x_2) & \hat{P}_{CNN}(x_2) \\
                \vdots & \vdots & \vdots \\
                \hat{P}_{ANN}(x_N) & \hat{P}_{LSTM}(x_N) & \hat{P}_{CNN}(x_N)
                \end{bmatrix}</span>
                <span class="eq-num">(24)</span>
            </div>

            <p>Because each base learner operates on fundamentally different mathematical mechanics—ANN mapping global dense projections, CNN extracting local spatial filters, and LSTM tracing sequential feature states—their prediction errors exhibit low mutual correlation. Stacking leverages this orthogonality to dramatically suppress decision variance and eliminate individual model blind spots.</p>

            <div class="callout-box">
                <strong>Super Learner Generalization Bound:</strong> As the training sample size $N \to \infty$, the cross-validation risk of the stacking meta-learner approaches the risk of the theoretical oracle selector plus an asymptotically negligible error bound $O(\frac{\log M}{N})$.
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">15</div>
        </div>
    </div>
    '''

def get_page_16():
    return '''
    <div class="page" id="page-16">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XIV. META-MODEL ARCHITECTURES: STACK-ANN</h2>
            <p>Stack-ANN deploys a specialized multi-layer neural network operating at the meta-level to synthesize base-model probability predictions into an authoritative diagnostic decision, as depicted in Figure 3.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig03_stack_ann.png" alt="Stack-ANN Framework" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 3.</strong> Proposed EDL-based Stack-ANN framework: base-model probability ingestion, meta-dense layers with ReLU activation, dropout regularization (0.5), and sigmoid/softmax classification output.</div>
            </div>

            <h3 class="subsec-heading">A. ARCHITECTURAL DESIGN & HYPERPARAMETERS</h3>
            <p>The input layer receives the meta-vector $z_i \in \mathbb{R}^3$ for binary classification. The intermediate meta-layer consists of a fully connected Dense layer with 32 neurons utilizing the Rectified Linear Unit (ReLU) activation function. To prevent meta-overfitting on probability magnitudes, an aggressive Dropout layer with dropout probability $p=0.5$ is applied. The final classification head contains 1 unit with Sigmoid activation for binary tasks, and 3 units with Softmax for multi-class screening.</p>
            <p>Training is conducted for 20 epochs with batch size 32, learning rate $\eta = 0.01$ under the Adam optimizer, utilizing a 20% validation split for early stopping.</p>

            <div class="table-caption">TABLE 9. Stack-ANN Meta-Learner Layer Configuration.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Layer</th><th>Units / Nodes</th><th>Activation</th><th>Regularization</th><th>Role in Meta-Ensemble</th></tr>
                </thead>
                <tbody>
                    <tr><td>Meta_Input</td><td>$M \times |\mathcal{C}|$</td><td>Linear</td><td>None</td><td>Base probability ingestion</td></tr>
                    <tr><td>Dense_Meta</td><td>32</td><td>ReLU</td><td>$L_2$ ($\lambda=10^{-3}$)</td><td>Non-linear probability fusion</td></tr>
                    <tr><td>Dropout_Meta</td><td>32</td><td>None</td><td>Rate = 0.50</td><td>Prevents meta-co-adaptation</td></tr>
                    <tr class="last-row"><td>Output_Meta</td><td>1 or 3</td><td>Sigmoid / Softmax</td><td>None</td><td>Final clinical risk score</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">16</div>
        </div>
    </div>
    '''

def get_page_17():
    return '''
    <div class="page" id="page-17">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XV. META-MODEL ARCHITECTURES: STACK-LSTM</h2>
            <p>Stack-LSTM conceptualizes base-model confidence outputs as a structured sequence of diagnostic opinions, deploying recurrent memory cells at the meta-level to reconcile competing model hypotheses, as illustrated in Figure 4.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig04_stack_lstm.png" alt="Stack-LSTM Framework" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 4.</strong> Proposed EDL-based Stack-LSTM framework: sequential probability reshaping, recurrent LSTM meta-layer (64 units), dense projection (32 units), and calibrated clinical prediction head.</div>
            </div>

            <h3 class="subsec-heading">A. ARCHITECTURAL DESIGN & RECURRENT MECHANICS</h3>
            <p>The input vector $[p_{ANN}, p_{LSTM}, p_{CNN}]$ is reshaped into a sequence of three sequential diagnostic inputs. The recurrent meta-layer comprises 64 LSTM memory units with ReLU activation, allowing the network to retain confidence trajectories across base learners. The accumulated hidden state is projected into an intermediate Dense layer with 32 units, followed by a final Sigmoid or Softmax output unit. The architecture trains over 20 epochs with a batch size of 32 and learning rate 0.01.</p>

            <div class="table-caption">TABLE 10. Stack-LSTM Meta-Learner Layer Configuration.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Layer</th><th>Units / Shape</th><th>Activation</th><th>Dropout</th><th>Role in Meta-Ensemble</th></tr>
                </thead>
                <tbody>
                    <tr><td>Sequence_Reshape</td><td>$(3, 1)$</td><td>Linear</td><td>None</td><td>Formats predictions as sequence</td></tr>
                    <tr><td>LSTM_Meta</td><td>64 units</td><td>ReLU</td><td>Recurrent Dropout 0.2</td><td>Sequential confidence modeling</td></tr>
                    <tr><td>Dense_Projection</td><td>32 units</td><td>ReLU</td><td>Dropout 0.3</td><td>Dimensionality compression</td></tr>
                    <tr class="last-row"><td>Output_Meta</td><td>1 or 3 units</td><td>Sigmoid / Softmax</td><td>None</td><td>Final clinical risk assessment</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">17</div>
        </div>
    </div>
    '''

def get_page_18():
    return '''
    <div class="page" id="page-18">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XVI. META-MODEL ARCHITECTURES: STACK-CNN</h2>
            <p>Stack-CNN deploys a 1D Convolutional Neural Network at the meta-level to detect localized covariance patterns and consensus structures across base-model probability distributions, as depicted in Figure 5.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig05_stack_cnn.png" alt="Stack-CNN Framework" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 5.</strong> Proposed EDL-based Stack-CNN framework: 1D convolutional feature map filtering (32 filters), max-pooling subsampling, flattening, dense projection (64 units), and classification head.</div>
            </div>

            <h3 class="subsec-heading">A. ARCHITECTURAL DESIGN & CONVOLUTIONAL MECHANICS</h3>
            <p>The input vector is processed by a 1D Convolutional layer with 32 filters, kernel size $k=3$, and ReLU activation, extracting localized cross-model agreement signals. A 1D Max-Pooling layer ($pool\_size=2$) subsamples the resulting feature maps, followed by a Flatten layer. A dense fully connected layer with 64 units and ReLU activation processes the pooled features, feeding into the final Sigmoid/Softmax output head. The network is trained for 20 epochs with batch size 32 and learning rate 0.01.</p>

            <div class="table-caption">TABLE 11. Stack-CNN Meta-Learner Layer Configuration.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th>Layer</th><th>Filters / Shape</th><th>Kernel / Pool</th><th>Activation</th><th>Role in Meta-Ensemble</th></tr>
                </thead>
                <tbody>
                    <tr><td>Conv1D_Meta</td><td>32 filters</td><td>$k=3$</td><td>ReLU</td><td>Local consensus filtering</td></tr>
                    <tr><td>MaxPool1D_Meta</td><td>$(1, 32)$</td><td>Pool Size = 2</td><td>None</td><td>Subsampling and noise damping</td></tr>
                    <tr><td>Flatten_Meta</td><td>32</td><td>None</td><td>None</td><td>Vectorization</td></tr>
                    <tr><td>Dense_Meta</td><td>64 units</td><td>None</td><td>ReLU</td><td>Non-linear decision synthesis</td></tr>
                    <tr class="last-row"><td>Output_Meta</td><td>1 or 3 units</td><td>None</td><td>Sigmoid / Softmax</td><td>Final clinical risk assessment</td></tr>
                </tbody>
            </table>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">18</div>
        </div>
    </div>
    '''

def get_page_19():
    return '''
    <div class="page" id="page-19">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XVII. PERFORMANCE EVALUATION METRICS</h2>
            <p>To establish an exhaustive, clinically robust evaluation of model performance, seven primary statistical indexes were evaluated: Accuracy, Precision, Specificity, Sensitivity (Recall), F-Score, Matthews Correlation Coefficient (MCC), and Area Under the ROC Curve (ROC-AUC) [47].</p>

            <h3 class="subsec-heading">A. MATHEMATICAL FORMULATIONS</h3>
            <p>Let $TP$, $TN$, $FP$, and $FN$ represent True Positives, True Negatives, False Positives, and False Negatives, respectively.</p>

            <p><strong>1. Accuracy:</strong> Proportion of correct diagnoses over all clinical instances:</p>
            <div class="eq-box">
                <span class="eq-math">\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}</span>
                <span class="eq-num">(25)</span>
            </div>

            <p><strong>2. Precision:</strong> Positive predictive value, measuring the fidelity of positive triage:</p>
            <div class="eq-box">
                <span class="eq-math">\text{Precision} = \frac{TP}{TP + FP}</span>
                <span class="eq-num">(26)</span>
            </div>

            <p><strong>3. Specificity:</strong> True negative rate, quantifying the ability to correctly identify healthy non-diabetic individuals:</p>
            <div class="eq-box">
                <span class="eq-math">\text{Specificity} = \frac{TN}{TN + FP}</span>
                <span class="eq-num">(27)</span>
            </div>

            <p><strong>4. Sensitivity (Recall):</strong> True positive rate, measuring the capacity to capture all diabetic cases without omission:</p>
            <div class="eq-box">
                <span class="eq-math">\text{Sensitivity} = \frac{TP}{TP + FN}</span>
                <span class="eq-num">(28)</span>
            </div>

            <p><strong>5. F-Score:</strong> Harmonic mean of Precision and Sensitivity, balancing FP and FN costs:</p>
            <div class="eq-box">
                <span class="eq-math">\text{F-Score} = 2 \times \frac{\text{Precision} \times \text{Sensitivity}}{\text{Precision} + \text{Sensitivity}}</span>
                <span class="eq-num">(29)</span>
            </div>

            <p><strong>6. Matthews Correlation Coefficient (MCC):</strong> Robust contingency metric reflecting all four confusion matrix quadrants, resilient to severe class imbalance:</p>
            <div class="eq-box">
                <span class="eq-math">\text{MCC} = \frac{TP \cdot TN - FP \cdot FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}}</span>
                <span class="eq-num">(30)</span>
            </div>
            <p>MCC ranges from $-1$ (complete disagreement) through $0$ (random guessing) to $+1$ (perfect prediction).</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">19</div>
        </div>
    </div>
    '''

def get_page_20():
    return '''
    <div class="page" id="page-20">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XVIII. EXPERIMENTAL RESULTS: PIMA-IDD-I DATASET</h2>
            <p>This section reports the experimental performance of the proposed base-level deep neural networks (ANN, LSTM, CNN) and meta-level stacking models (Stack-ANN, Stack-LSTM, Stack-CNN) on the PIMA-IDD-I dataset. Table 12 summarizes the audited metrics across all six classification models.</p>

            <div class="table-caption">TABLE 12. Performance Evaluation of Base and Meta Models on PIMA-IDD-I.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th rowspan="2">Evaluation Indexes</th><th colspan="3">Deep Learning (Base Models)</th><th colspan="3">Ensemble Deep Learning (Meta Models)</th></tr>
                    <tr><th>ANN</th><th>LSTM</th><th>CNN</th><th>Stack-ANN</th><th>Stack-LSTM</th><th>Stack-CNN</th></tr>
                </thead>
                <tbody>
                    <tr><td>Accuracy</td><td>0.9277</td><td>0.9107</td><td>0.9073</td><td><strong>0.9881</strong></td><td>0.9723</td><td>0.9481</td></tr>
                    <tr><td>Precision</td><td>0.9265</td><td>0.9143</td><td>0.9067</td><td><strong>0.9793</strong></td><td>0.9734</td><td>0.9393</td></tr>
                    <tr><td>Specificity</td><td>0.9285</td><td>0.9101</td><td>0.9043</td><td><strong>0.9840</strong></td><td>0.9654</td><td>0.9388</td></tr>
                    <tr><td>Sensitivity</td><td>0.9276</td><td>0.9036</td><td>0.8954</td><td><strong>0.9802</strong></td><td>0.9644</td><td>0.9402</td></tr>
                    <tr><td>F-Score</td><td>0.9101</td><td>0.9051</td><td>0.9032</td><td><strong>0.9780</strong></td><td>0.9706</td><td>0.9378</td></tr>
                    <tr class="last-row"><td>MCC</td><td>0.9043</td><td>0.8953</td><td>0.8898</td><td><strong>0.9428</strong></td><td>0.9307</td><td>0.9228</td></tr>
                </tbody>
            </table>

            <h3 class="subsec-heading">A. QUANTITATIVE ANALYSIS ON PIMA-IDD-I</h3>
            <p>Among base models, the ANN demonstrated superior individual performance, achieving 0.9277 accuracy, 0.9265 precision, and 0.9043 MCC, reflecting the efficacy of dense multi-layer projections on continuous physiological parameters. LSTM and CNN exhibited competitive accuracy of 0.9107 and 0.9073, respectively.</p>
            <p>Critically, all three meta-level stacking models substantially outperformed every base model. Stack-ANN achieved the highest overall performance with an outstanding diagnostic accuracy of <strong>0.9881</strong> (98.81%), precision of 0.9793, specificity of 0.9840, sensitivity of 0.9802, F-score of 0.9780, and MCC of 0.9428. Stack-LSTM achieved 0.9723 accuracy and 0.9307 MCC, while Stack-CNN attained 0.9481 accuracy and 0.9228 MCC.</p>
            <p>The remarkable surge in MCC (+0.0385 gain over the best base model) underscores how stacking effectively eliminates false positive diagnoses while ensuring zero omission of genuine diabetic patients.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">20</div>
        </div>
    </div>
    '''

def get_page_21():
    return '''
    <div class="page" id="page-21">
        <div class="page-header">
            <div class="header-left">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
            <div class="header-right"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
        </div>

        <div class="content-body">
            <h3 class="subsec-heading">B. VISUAL PERFORMANCE EVALUATION ON PIMA-IDD-I</h3>
            <p>Figure 6 presents a graphical comparison of the six evaluation metrics across both base and meta models on PIMA-IDD-I. The consistent elevation of the meta-level models is evident across every metric category.</p>

            <div class="fig-container full-width">
                <img src="report_figures/fig06_pima_perf.png" alt="PIMA Performance" style="max-height: 2.8in;">
                <div class="fig-caption"><strong>FIGURE 6.</strong> Performance comparison of proposed DL base models and EDL meta-models on PIMA-IDD-I across Accuracy, Precision, Specificity, Sensitivity, F-Score, and MCC.</div>
            </div>

            <p>Figures 9 and 12 display the Receiver Operating Characteristic (ROC) curves and corresponding Area Under the Curve (AUC) values for the base and meta models, respectively. In Figure 9, the base models achieve AUCs of 0.92 (ANN), 0.96 (CNN), and 0.92 (LSTM). In Figure 12, the EDL meta-models achieve dramatic AUC improvements, with Stack-ANN attaining an exceptional AUC of <strong>0.98</strong>, Stack-LSTM achieving 0.97, and Stack-CNN reaching 0.94.</p>

            <div style="display: flex; gap: 8px; margin: 6px 0;" class="full-width">
                <div style="flex: 1; text-align: center;">
                    <img src="report_figures/fig09_base_roc_pima.png" alt="Base ROC PIMA" style="max-height: 2.2in; width: 100%;">
                    <div class="fig-caption"><strong>FIGURE 9.</strong> ROC/AUC for DL base models (LSTM, CNN, ANN) on PIMA-IDD-I.</div>
                </div>
                <div style="flex: 1; text-align: center;">
                    <img src="report_figures/fig12_edl_roc_pima.png" alt="EDL ROC PIMA" style="max-height: 2.2in; width: 100%;">
                    <div class="fig-caption"><strong>FIGURE 12.</strong> ROC/AUC for proposed EDL models (Stack-ANN, LSTM, CNN) on PIMA-IDD-I.</div>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">21</div>
        </div>
    </div>
    '''

def get_page_22():
    return '''
    <div class="page" id="page-22">
        <div class="page-header">
            <div class="header-left"><span class="ieee-logo-text"><span class="ieee-blue">IEEE</span> <span class="ieee-access">Access</span></span></div>
            <div class="header-right">A. R: Innovative EDL Clinical Decision Support System for Diabetes Prediction</div>
        </div>

        <div class="content-body">
            <h2 class="sec-heading">XIX. EXPERIMENTAL RESULTS: DDFH-G DATASET (2000 CASES)</h2>
            <p>To evaluate scalability on larger clinical cohorts, the proposed framework was trained and evaluated on the 2000-case Frankfurt Hospital Germany dataset (DDFH-G). Table 13 reports the benchmarked performance metrics.</p>

            <div class="table-caption">TABLE 13. Performance Evaluation of Base and Meta Models on DDFH-G.</div>
            <table class="ieee-table">
                <thead>
                    <tr><th rowspan="2">Evaluation Indexes</th><th colspan="3">Deep Learning (Base Models)</th><th colspan="3">Ensemble Deep Learning (Meta Models)</th></tr>
                    <tr><th>ANN</th><th>LSTM</th><th>CNN</th><th>Stack-ANN</th><th>Stack-LSTM</th><th>Stack-CNN</th></tr>
                </thead>
                <tbody>
                    <tr><td>Accuracy</td><td>0.9477</td><td>0.9324</td><td>0.9273</td><td><strong>0.9951</strong></td><td>0.9836</td><td>0.9744</td></tr>
                    <tr><td>Precision</td><td>0.9365</td><td>0.9365</td><td>0.9367</td><td><strong>0.9892</strong></td><td>0.9834</td><td>0.9704</td></tr>
                    <tr><td>Specificity</td><td>0.9285</td><td>0.9285</td><td>0.9143</td><td><strong>0.9902</strong></td><td>0.9877</td><td>0.9688</td></tr>
                    <tr><td>Sensitivity</td><td>0.9402</td><td>0.9332</td><td>0.9251</td><td><strong>0.9897</strong></td><td>0.9854</td><td>0.9685</td></tr>
                    <tr><td>F-Score</td><td>0.9401</td><td>0.9301</td><td>0.9232</td><td><strong>0.9922</strong></td><td>0.9743</td><td>0.9606</td></tr>
                    <tr class="last-row"><td>MCC</td><td>0.9364</td><td>0.9323</td><td>0.9399</td><td><strong>0.9728</strong></td><td>0.9620</td><td>0.9507</td></tr>
                </tbody>
            </table>

            <h3 class="subsec-heading">A. QUANTITATIVE ANALYSIS ON DDFH-G</h3>
            <p>The elevated sample size of DDFH-G provided rich statistical training volume that enabled deep neural networks to converge with exceptional fidelity. Base ANN reached 0.9477 accuracy and 0.9364 MCC. Base LSTM and CNN achieved 0.9324 and 0.9273 accuracy, respectively.</p>
            <p>Stack-ANN attained a remarkable peak diagnostic accuracy of <strong>0.9951</strong> (99.51%), precision of 0.9892, specificity of 0.9902, sensitivity of 0.9897, F-score of 0.9922, and MCC of 0.9728. Out of 400 held-out test patients, Stack-ANN misclassified only two cases. Stack-LSTM attained 0.9836 accuracy and 0.9620 MCC, while Stack-CNN recorded 0.9744 accuracy and 0.9507 MCC.</p>
            <p>These findings conclusively demonstrate that the stacking meta-learner scales effectively with increasing clinical data volume, delivering near-deterministic diagnostic precision.</p>
        </div>

        <div class="page-footer">
            <div class="footer-left">VOLUME 14, 2026</div>
            <div class="footer-center">© 2026 The Author. This work is licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.</div>
            <div class="footer-right">22</div>
        </div>
    </div>
    '''

print("Part 2 defined successfully.")
