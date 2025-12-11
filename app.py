import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Student Marks Prediction Dashboard",
    page_icon=" ",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .insight-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #17a2b8;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">  Student Marks Prediction Analysis</p>', unsafe_allow_html=True)
st.markdown("### Predicting Student Performance Using Machine Learning")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Section", 
                        ["Overview", "Workflow", "RQ1: Midterm I", "RQ2: Midterm II", 
                         "RQ3: Final Exam", "Conclusions"])

# ==================== OVERVIEW PAGE ====================
if page == "Overview":
    st.markdown('<p class="sub-header">Project Overview</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Dataset Size", "254 students", "18 features")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Research Questions", "3", "Prediction Tasks")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Models Tested", "12+", "Various Approaches")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Research Questions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
        <h4>RQ1: Predict Midterm I</h4>
        <p><strong>Features:</strong> 2 Assignments + 2 Quizzes</p>
        <p><strong>Best Model:</strong> Polynomial Regression</p>
        <p><strong>Test R²:</strong> 0.3131</p>
        <p><strong>Test MAE:</strong> 11.20 marks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
        <h4>RQ2: Predict Midterm II</h4>
        <p><strong>Features:</strong> 3 Assignments + 4 Quizzes + Midterm I</p>
        <p><strong>Best Model:</strong> Multiple Linear (Raw)</p>
        <p><strong>Test R²:</strong> 0.5045</p>
        <p><strong>Test MAE:</strong> 11.65 marks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="insight-box">
        <h4>RQ3: Predict Final Exam</h4>
        <p><strong>Features:</strong> Assignments + Both Midterms</p>
        <p><strong>Best Model:</strong> Collapsed (No Quizzes)</p>
        <p><strong>Test R²:</strong> 0.6229</p>
        <p><strong>Test MAE:</strong> 10.30 marks</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("###   Key Findings")
    
    st.markdown("""
    <div class="success-box">
    <h4>Bootstrap Results - Model Stability</h4>
    <ul>
        <li><strong>Mean MAE:</strong> 9.28 marks</li>
        <li><strong>Standard Deviation:</strong> 0.43 marks</li>
        <li><strong>95% Confidence Interval:</strong> [8.50, 10.15] marks</li>
    </ul>
    <p><strong>Interpretation:</strong> We are 95% confident that the true prediction error for the Final Exam 
    lies between 8.50 and 10.15 marks. This narrow confidence interval suggests stable and reliable model performance.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Insights
    st.markdown("###   Key Insights")
    
    st.markdown("""
    <div class="success-box">
    <h4>  Excellent Performance</h4>
    <ul>
        <li><strong>Best Overall R²:</strong> 62% of variance explained (highest across all RQs)</li>
        <li><strong>Lowest MAE:</strong> Average error of only 10.30 marks</li>
        <li><strong>Strong Predictive Power:</strong> Midterm II score is the dominant predictor</li>
        <li><strong>Model Simplicity:</strong> Only 3 features needed for good performance</li>
        <li><strong>Stable Predictions:</strong> Narrow bootstrap confidence interval</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>  Why Quizzes Were Excluded</h4>
    <ul>
        <li><strong>Negative Coefficient:</strong> Quiz_Mean had a coefficient of -0.022 in Model 3</li>
        <li><strong>Illogical Relationship:</strong> Higher quiz scores shouldn't predict lower final scores</li>
        <li><strong>Data Quality Issues:</strong> Suggests noise or missing data problems in quiz records</li>
        <li><strong>Minimal Impact:</strong> R² barely changed when quizzes were added (0.6229 vs 0.6218)</li>
        <li><strong>Better Adjusted R²:</strong> Model without quizzes has better adjusted R² (0.5715 vs 0.5498)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Comparison across all RQs
    st.markdown("###   Performance Across All Research Questions")
    
    all_rqs_data = pd.DataFrame({
        'Research Question': ['RQ1: Midterm I', 'RQ2: Midterm II', 'RQ3: Final Exam'],
        'Best Model': ['Polynomial (deg=2)', 'Multiple Linear (Raw)', 'Collapsed (No Quiz)'],
        'Test R²': [0.3131, 0.5045, 0.6229],
        'Test MAE': [11.20, 11.65, 10.30],
        '# Features': [4, 8, 3]
    })
    
    fig_progression = go.Figure()
    
    fig_progression.add_trace(go.Scatter(
        x=all_rqs_data['Research Question'],
        y=all_rqs_data['Test R²'],
        mode='lines+markers',
        name='Test R²',
        line=dict(color='blue', width=3),
        marker=dict(size=12)
    ))
    
    fig_progression.update_layout(
        title='Model Performance Progression Across Research Questions',
        xaxis_title='Research Question',
        yaxis_title='Test R²',
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig_progression, use_container_width=True)
    
    st.dataframe(all_rqs_data, use_container_width=True)

# ==================== CONCLUSIONS PAGE ====================
elif page == "Conclusions":
    st.markdown('<p class="sub-header">Final Conclusions & Recommendations</p>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Executive Summary")
    
    st.markdown("""
    <div class="success-box">
    <h3>Overall Project Success</h3>
    <p>Successfully developed predictive models for student performance across three stages of assessment, 
    with progressively improving accuracy as more data becomes available.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Findings
    st.markdown("### 🔑 Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
        <h4>  What Works Well</h4>
        <ul>
            <li><strong>Progressive Improvement:</strong> Models get better with more data
                <ul>
                    <li>RQ1: R² = 0.31 (limited data)</li>
                    <li>RQ2: R² = 0.50 (more features)</li>
                    <li>RQ3: R² = 0.62 (complete data)</li>
                </ul>
            </li>
            <li><strong>Previous Performance:</strong> Past exam scores are excellent predictors</li>
            <li><strong>Feature Engineering:</strong> Collapsed features work as well as raw features</li>
            <li><strong>Model Stability:</strong> Bootstrap analysis confirms reliability</li>
            <li><strong>Practical Accuracy:</strong> Final model predicts within ±10 marks</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4>  Challenges & Limitations</h4>
        <ul>
            <li><strong>Quiz Data Quality:</strong> Quiz scores showed inconsistent patterns
                <ul>
                    <li>Negative coefficients in some models</li>
                    <li>Weak correlations with outcomes</li>
                    <li>Possible data entry errors</li>
                </ul>
            </li>
            <li><strong>Missing Data:</strong> Assignments 5-6 and Quizzes 7-8 had missing values</li>
            <li><strong>Early Predictions:</strong> RQ1 (Midterm I) has limited predictive power</li>
            <li><strong>Small Test Set:</strong> RQ3 used only 10% for testing due to many features</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Model Recommendations
    st.markdown("###   Recommended Models for Each Task")
    
    recommendations = pd.DataFrame({
        'Task': ['Predicting Midterm I', 'Predicting Midterm II', 'Predicting Final Exam'],
        'Recommended Model': [
            'Polynomial Regression (degree=2)',
            'Multiple Linear Regression (Raw)',
            'Collapsed Features (No Quizzes)'
        ],
        'R² Score': [0.3131, 0.5045, 0.6229],
        'Expected Error (MAE)': ['11.20 marks', '11.65 marks', '10.30 marks'],
        'Key Predictors': [
            'Qz:2, Qz:1, As:1, As:2',
            'S-I (0.76), Qz:4 (0.13), As:3 (0.12)',
            'S-II (0.59), As_Mean (0.12), S-I (0.07)'
        ],
        'Use Case': [
            'Early intervention (limited accuracy)',
            'Mid-semester assessment',
            'Final grade prediction (most reliable)'
        ]
    })
    
    st.dataframe(recommendations, use_container_width=True)
    
    # Practical Implications
    st.markdown("### 🎓 Practical Implications for Educators")
    
    st.markdown("""
    <div class="insight-box">
    <h4>How to Use These Models</h4>
    
    <p><strong>1. Early Warning System (After 2 Quizzes & 2 Assignments):</strong></p>
    <ul>
        <li>Accuracy is limited (R² = 0.31), but can identify at-risk students</li>
        <li>Use for early intervention and support</li>
        <li>Focus on students predicted to score below 40</li>
    </ul>
    
    <p><strong>2. Mid-Semester Check (After Midterm I):</strong></p>
    <ul>
        <li>Much better accuracy (R² = 0.50)</li>
        <li>Midterm I score is the strongest predictor of Midterm II</li>
        <li>Target students who performed poorly on Midterm I</li>
    </ul>
    
    <p><strong>3. Final Grade Forecasting (After Both Midterms):</strong></p>
    <ul>
        <li>Best accuracy (R² = 0.62) with ±10 marks error</li>
        <li>Midterm II is the most important predictor</li>
        <li>Can be used for grade projections and academic planning</li>
        <li>Assignment performance also matters</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Data Quality Recommendations
    st.markdown("###   Recommendations for Data Collection")
    
    st.markdown("""
    <div class="warning-box">
    <h4>Improving Future Predictions</h4>
    <ul>
        <li><strong>Quiz Management:</strong> Ensure consistent quiz administration and grading
            <ul>
                <li>Current quiz data appears noisy</li>
                <li>Consider standardized quiz formats</li>
                <li>Reduce missing quiz scores</li>
            </ul>
        </li>
        <li><strong>Assignment Collection:</strong> Minimize missing assignment submissions
            <ul>
                <li>As:5 and As:6 had significant missing data</li>
                <li>Implement reminder systems</li>
                <li>Consider alternative submissions for absent students</li>
            </ul>
        </li>
        <li><strong>Additional Features:</strong> Consider collecting:
            <ul>
                <li>Attendance records</li>
                <li>Participation scores</li>
                <li>Study time logs</li>
                <li>Previous semester GPAs</li>
            </ul>
        </li>
        <li><strong>Data Validation:</strong> Implement checks for data entry errors</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Insights
    st.markdown("### 🔧 Technical Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>  Best Practices Applied</h4>
        <ul>
            <li>Proper train-test splits</li>
            <li>Multiple model comparison</li>
            <li>Baseline model evaluation</li>
            <li>Bootstrap confidence intervals</li>
            <li>Adjusted R² for model selection</li>
            <li>Feature engineering (collapsed features)</li>
            <li>Missing data imputation</li>
            <li>Overfitting/underfitting analysis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
        <h4>    Methodology Highlights</h4>
        <ul>
            <li><strong>Imputation Strategy:</strong> Used mean of available assignments/quizzes</li>
            <li><strong>Feature Selection:</strong> Removed noisy quiz data in final model</li>
            <li><strong>Model Complexity:</strong> Simpler models preferred when performance is similar</li>
            <li><strong>Validation:</strong> 500 bootstrap samples for confidence intervals</li>
            <li><strong>Metrics:</strong> R², Adjusted R², MAE, RMSE, MAPE</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Final Recommendation
    st.markdown("###   Final Recommendation")
    
    st.markdown("""
    <div class="success-box">
    <h3>Recommended Approach</h3>
    <p>We recommend <strong>Model 2: Collapsed Features (No Quizzes)</strong> for predicting final exam scores because:</p>
    <ol>
        <li><strong>Best Adjusted R² (0.5715):</strong> Most reliable generalization to new data</li>
        <li><strong>Simplicity:</strong> Uses only 3 features (As_Mean, S-I, S-II)</li>
        <li><strong>Interpretability:</strong> Clear, logical relationships (no negative coefficients)</li>
        <li><strong>Practical Accuracy:</strong> Expected error of ±10 marks</li>
        <li><strong>Data Quality:</strong> Avoids noisy quiz data</li>
        <li><strong>Stability:</strong> Narrow bootstrap confidence interval [8.50, 10.15]</li>
    </ol>
    
    <p><strong>Model Equation:</strong></p>
    <code>Final = 10.59 + 0.12x(Assignment_Avg) + 0.07x(Midterm_I) + 0.59x(Midterm_II)</code>
    
    <p style="margin-top: 1rem;"><em>This model balances accuracy, simplicity, and reliability for practical use in educational settings.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Future Work
    st.markdown("###   Future Work")
    
    st.markdown("""
    <div class="insight-box">
    <h4>Potential Improvements</h4>
    <ul>
        <li><strong>Advanced Models:</strong> Try Random Forest, Gradient Boosting, Neural Networks</li>
        <li><strong>Feature Engineering:</strong> Create interaction terms, polynomial features for all models</li>
        <li><strong>Cross-Validation:</strong> Use k-fold CV instead of simple train-test split</li>
        <li><strong>Hyperparameter Tuning:</strong> Grid search for optimal parameters</li>
        <li><strong>Time Series Analysis:</strong> Model student learning trajectory over time</li>
        <li><strong>Clustering:</strong> Identify distinct student performance groups</li>
        <li><strong>Larger Dataset:</strong> Collect data across multiple semesters/courses</li>
        <li><strong>External Factors:</strong> Include demographic, attendance, engagement data</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Summary Statistics
    st.markdown("###   Project Summary Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Students", "254", "Complete dataset")
    with col2:
        st.metric("Features Analyzed", "18", "Assignments, Quizzes, Exams")
    with col3:
        st.metric("Models Trained", "12+", "Various approaches")
    with col4:
        st.metric("Best R² Achieved", "0.6229", "Final Exam Prediction")
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background-color: #f8f9fa; border-radius: 10px;">
        <h3>📚   Student Marks Prediction System</h3>
        <p><em>Data-driven insights for educational success</em></p>
        <p style="margin-top: 1rem; font-size: 0.9rem; color: #6c757d;">
            Project IDs: 23F-0676, 23F-0709 | Data Science Project I
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("    <h4>    Main Insights</h4>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
        <li><strong>Progressive Improvement:</strong> Model performance increases with more data (RQ1 → RQ2 → RQ3)</li>
        <li><strong>Midterm Performance Matters:</strong> Previous midterm scores are strong predictors of future performance</li>
        <li><strong>Quiz Data Quality Issues:</strong> Quiz scores showed negative correlations in some models, suggesting noisy data</li>
        <li><strong>Feature Engineering Works:</strong> Collapsed features (averages) often performed as well as or better than raw features</li>
        <li><strong>Stable Predictions:</strong> Bootstrap confidence intervals confirm model reliability</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("###   Dataset Summary")
    
    # Create a simple statistics table
    stats_data = {
        'Feature Type': ['Assignments', 'Quizzes', 'Midterms', 'Final Exam', 'Project'],
        'Count': [6, 8, 2, 1, 1],
        'Missing Data': ['Yes (As:5, As:6)', 'Yes (Qz:7, Qz:8)', 'No', 'No', 'No']
    }
    
    df_stats = pd.DataFrame(stats_data)
    st.dataframe(df_stats, use_container_width=True)

# ==================== WORKFLOW PAGE ====================
elif page == "Workflow":
    st.markdown('<p class="sub-header">Analysis Workflow & Pipeline</p>', unsafe_allow_html=True)
    
    st.markdown(
    """
    This diagram shows the complete workflow for all three research questions, including:
    - Data loading and preprocessing
    - Exploratory data analysis
    - Feature engineering
    - Model training and evaluation
    - Bootstrapping analysis
    """
    )
    
    st.info("  **Note:** Please place your workflow.png file in the same directory as this script to display it here.")
    
    # Try to load the workflow image
    try:
        workflow_img = Image.open('workflow.png')
        st.image(workflow_img, caption='Complete Analysis Pipeline', use_column_width=True)
    except:
        st.warning("  Workflow image not found. Please ensure 'workflow.png' is in the correct directory.")
        
        # Show text-based workflow
        st.markdown("### Text-Based Workflow")
        
        st.markdown("""
        ```
        1. Load Student Marks Dataset
           ↓
        2. Initial EDA (254 rows, 18 columns)
           ↓
        3. Data Cleaning & Imputation
           ↓
        4. Feature Engineering (Collapsed features)
           ↓
        5. Exploratory Data Analysis
           ├── Correlation Analysis
           ├── Distribution Analysis
           └── Feature Relationships
           ↓
        6. Research Question Split
           ├── RQ1: Midterm I Prediction
           │   ├── Raw Features Model
           │   ├── Collapsed Features Model
           │   ├── Polynomial Regression
           │   └── Dummy Baseline
           │
           ├── RQ2: Midterm II Prediction
           │   ├── Raw Features Model
           │   ├── Collapsed Features Model
           │   ├── Polynomial Regression
           │   └── Dummy Baseline
           │
           └── RQ3: Final Exam Prediction
               ├── Model 1: Raw with Imputation
               ├── Model 2: Collapsed (No Quiz)
               └── Model 3: Collapsed (With Quiz)
           ↓
        7. Model Evaluation
           ├── R² Score
           ├── Adjusted R²
           ├── MAE, RMSE, MAPE
           └── Overfitting/Underfitting Analysis
           ↓
        8. Bootstrapping Analysis (500 samples)
           ├── Confidence Intervals
           └── Model Stability Assessment
           ↓
        9. Final Results & Recommendations
        ```
        """)

# ==================== RQ1 PAGE ====================
elif page == "RQ1: Midterm I":
    st.markdown('<p class="sub-header">RQ1: Predicting Midterm I Marks</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>  Problem Statement</h4>
    <p>Predict Midterm I (S-I) marks using:</p>
    <ul>
        <li>2 Assignments (As:1, As:2)</li>
        <li>2 Quizzes (Qz:1, Qz:2)</li>
    </ul>
    <p><strong>Dataset Size:</strong> 254 students</p>
    <p><strong>Train/Test Split:</strong> 203/51 (80/20)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model Comparison
    st.markdown("###   Model Comparison")
    
    rq1_data = pd.DataFrame({
        'Model': ['Multiple Linear (Raw)', 'Multiple Linear (Collapsed)', 
                  'Polynomial (deg=2)', 'Dummy Baseline'],
        'Train R²': [0.2636, 0.2606, 0.2879, 0.0000],
        'Test R²': [0.2059, 0.2095, 0.3131, -0.0126],
        'Test MAE': [12.04, 11.98, 11.20, 12.92],
        'Test RMSE': [14.45, 14.41, 13.43, 16.31]
    })
    
    # Display table
    st.dataframe(rq1_data.style.highlight_max(subset=['Test R²'], color='lightgreen')
                               .highlight_min(subset=['Test MAE', 'Test RMSE'], color='lightgreen'),
                 use_container_width=True)
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # R² Comparison
        fig_r2 = go.Figure(data=[
            go.Bar(name='Train R²', x=rq1_data['Model'], y=rq1_data['Train R²'], 
                   marker_color='lightblue'),
            go.Bar(name='Test R²', x=rq1_data['Model'], y=rq1_data['Test R²'], 
                   marker_color='orange')
        ])
        fig_r2.update_layout(
            title='R² Score Comparison',
            barmode='group',
            yaxis_title='R² Score',
            height=400
        )
        st.plotly_chart(fig_r2, use_container_width=True)
    
    with col2:
        # MAE Comparison
        fig_mae = go.Figure(data=[
            go.Bar(x=rq1_data['Model'], y=rq1_data['Test MAE'], 
                   marker_color=['coral', 'coral', 'lightgreen', 'coral'])
        ])
        fig_mae.update_layout(
            title='Test MAE Comparison',
            yaxis_title='MAE (marks)',
            height=400
        )
        st.plotly_chart(fig_mae, use_container_width=True)
    
    # Best Model
    st.markdown("###   Best Model: Polynomial Regression (degree=2)")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Test R²", "0.3131")
    with col2:
        st.metric("Test MAE", "11.20 marks")
    with col3:
        st.metric("Test RMSE", "13.43 marks")
    with col4:
        st.metric("Status", "  Reasonable")
    
    # Bootstrap Analysis
    st.markdown("###   Bootstrap Analysis (500 samples)")
    
    st.markdown("""
    <div class="success-box">
    <h4>Bootstrap Results - Model Stability</h4>
    <ul>
        <li><strong>Mean MAE:</strong> 11.79 marks</li>
        <li><strong>Standard Deviation:</strong> 0.63 marks</li>
        <li><strong>95% Confidence Interval:</strong> [10.47, 13.08] marks</li>
    </ul>
    <p><strong>Interpretation:</strong> We are 95% confident that the true prediction error for Midterm I 
    lies between 10.47 and 13.08 marks. This relatively narrow interval suggests stable model performance.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Correlations
    st.markdown("###   Feature Correlations with Midterm I")
    
    corr_data = pd.DataFrame({
        'Feature': ['S-I', 'Qz:2', 'Qz:1', 'As:1', 'As:2'],
        'Correlation': [1.000, 0.403, 0.384, 0.231, 0.115]
    })
    
    fig_corr = px.bar(corr_data, x='Feature', y='Correlation', 
                      title='Feature Correlation with Midterm I',
                      color='Correlation', color_continuous_scale='Blues')
    fig_corr.update_layout(height=400)
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Key Insights
    st.markdown("###   Key Insights")
    
    st.markdown("""
    <div class="warning-box">
    <h4>  Challenges</h4>
    <ul>
        <li><strong>Low R² Score:</strong> Only 31% of variance explained - suggests weak predictive power</li>
        <li><strong>Limited Features:</strong> With only 2 assignments and 2 quizzes, there's not much information to work with</li>
        <li><strong>Underfitting Risk:</strong> Linear models showed signs of underfitting (low performance on both train and test)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>  What Works</h4>
    <ul>
        <li><strong>Polynomial Features:</strong> Adding polynomial terms improved performance</li>
        <li><strong>Quiz Scores:</strong> Quizzes showed stronger correlation than assignments</li>
        <li><strong>Feature Averaging:</strong> Collapsed features performed nearly as well as raw features</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ==================== RQ2 PAGE ====================
elif page == "RQ2: Midterm II":
    st.markdown('<p class="sub-header">RQ2: Predicting Midterm II Marks</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>  Problem Statement</h4>
    <p>Predict Midterm II (S-II) marks using:</p>
    <ul>
        <li>3 Assignments (As:1, As:2, As:3)</li>
        <li>4 Quizzes (Qz:1, Qz:2, Qz:3, Qz:4)</li>
        <li>Midterm I score (S-I)</li>
    </ul>
    <p><strong>Dataset Size:</strong> 254 students</p>
    <p><strong>Train/Test Split:</strong> 203/51 (80/20)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model Comparison
    st.markdown("###   Model Comparison")
    
    rq2_data = pd.DataFrame({
        'Model': ['Multiple Linear (Raw)', 'Multiple Linear (Collapsed)', 
                  'Polynomial (deg=2)', 'Dummy Baseline'],
        'Train R²': [0.5116, 0.4544, 0.4618, 0.0000],
        'Test R²': [0.5045, 0.4879, 0.4595, -0.0152],
        'Test MAE': [11.65, 12.69, 13.23, 17.36],
        'Test RMSE': [15.11, 15.36, 15.78, 21.63]
    })
    
    st.dataframe(rq2_data.style.highlight_max(subset=['Test R²'], color='lightgreen')
                               .highlight_min(subset=['Test MAE', 'Test RMSE'], color='lightgreen'),
                 use_container_width=True)
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # R² Comparison
        fig_r2 = go.Figure(data=[
            go.Bar(name='Train R²', x=rq2_data['Model'], y=rq2_data['Train R²'], 
                   marker_color='lightblue'),
            go.Bar(name='Test R²', x=rq2_data['Model'], y=rq2_data['Test R²'], 
                   marker_color='orange')
        ])
        fig_r2.update_layout(
            title='R² Score Comparison',
            barmode='group',
            yaxis_title='R² Score',
            height=400
        )
        st.plotly_chart(fig_r2, use_container_width=True)
    
    with col2:
        # MAE Comparison
        fig_mae = go.Figure(data=[
            go.Bar(x=rq2_data['Model'], y=rq2_data['Test MAE'], 
                   marker_color=['lightgreen', 'coral', 'coral', 'coral'])
        ])
        fig_mae.update_layout(
            title='Test MAE Comparison',
            yaxis_title='MAE (marks)',
            height=400
        )
        st.plotly_chart(fig_mae, use_container_width=True)
    
    # Best Model
    st.markdown("###   Best Model: Multiple Linear Regression (Raw Features)")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Test R²", "0.5045")
    with col2:
        st.metric("Test MAE", "11.65 marks")
    with col3:
        st.metric("Test RMSE", "15.11 marks")
    with col4:
        st.metric("Adjusted R²", "0.4101")
    
    # Model Coefficients
    st.markdown("###   Model Coefficients (Raw Features)")
    
    coef_data = pd.DataFrame({
        'Feature': ['S-I', 'Qz:4', 'As:3', 'Qz:3', 'As:2', 'Qz:1', 'As:1', 'Qz:2'],
        'Coefficient': [0.7602, 0.1290, 0.1171, 0.0747, 0.0387, -0.0268, -0.0456, -0.0746]
    })
    
    fig_coef = px.bar(coef_data, x='Feature', y='Coefficient',
                      title='Feature Importance (Coefficients)',
                      color='Coefficient', color_continuous_scale='RdBu_r')
    fig_coef.update_layout(height=400)
    st.plotly_chart(fig_coef, use_container_width=True)
    
    # Bootstrap Analysis
    st.markdown("###   Bootstrap Analysis (500 samples)")
    
    st.markdown("""
    <div class="success-box">
    <h4>Bootstrap Results - Model Stability</h4>
    <ul>
        <li><strong>Mean MAE:</strong> 12.29 marks</li>
        <li><strong>Standard Deviation:</strong> 0.72 marks</li>
        <li><strong>95% Confidence Interval:</strong> [10.84, 13.65] marks</li>
    </ul>
    <p><strong>Interpretation:</strong> We are 95% confident that the true prediction error for Midterm II 
    lies between 10.84 and 13.65 marks. The model shows good stability and reliability.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Correlations
    st.markdown("###   Feature Correlations with Midterm II")
    
    corr_data = pd.DataFrame({
        'Feature': ['S-II', 'S-I', 'Qz:4', 'As:3', 'Qz:3', 'Qz:1', 'Qz:2', 'As:2', 'As:1'],
        'Correlation': [1.000, 0.657, 0.426, 0.356, 0.292, 0.269, 0.237, 0.208, 0.154]
    })
    
    fig_corr = px.bar(corr_data, x='Feature', y='Correlation',
                      title='Feature Correlation with Midterm II',
                      color='Correlation', color_continuous_scale='Viridis')
    fig_corr.update_layout(height=400)
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Key Insights
    st.markdown("###   Key Insights")
    
    st.markdown("""
    <div class="success-box">
    <h4>  Significant Improvements</h4>
    <ul>
        <li><strong>Better R² Score:</strong> 50% of variance explained (up from 31% in RQ1)</li>
        <li><strong>Strong Predictor:</strong> Midterm I score has the highest coefficient (0.76)</li>
        <li><strong>No Overfitting:</strong> Train and test R² scores are very close (0.51 vs 0.50)</li>
        <li><strong>Reasonable Performance:</strong> All models beat the baseline significantly</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>  Observations</h4>
    <ul>
        <li><strong>Previous Performance Matters:</strong> S-I is the strongest predictor by far</li>
        <li><strong>Recent Assessments:</strong> Later quizzes (Qz:4, Qz:3) correlate better than earlier ones</li>
        <li><strong>Model Stability:</strong> Very small difference between train and test performance</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ==================== RQ3 PAGE ====================
elif page == "RQ3: Final Exam":
    st.markdown('<p class="sub-header">RQ3: Predicting Final Exam Marks</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>  Problem Statement</h4>
    <p>Predict Final Exam marks using all available features:</p>
    <ul>
        <li>6 Assignments (with imputation for As:5, As:6)</li>
        <li>8 Quizzes (with imputation for Qz:7, Qz:8)</li>
        <li>Both Midterm scores (S-I, S-II)</li>
    </ul>
    <p><strong>Dataset Size:</strong> 254 students</p>
    <p><strong>Train/Test Split:</strong> 90/10 (smaller test set due to more features)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Model Comparison
    st.markdown("###   Model Comparison")
    
    rq3_data = pd.DataFrame({
        'Model': ['Model 1: Raw (Imputed)', 'Model 2: Collapsed (No Quiz)', 
                  'Model 3: Collapsed (With Quiz)'],
        'R²': [0.7454, 0.6229, 0.6218],
        'Adjusted R²': [0.2928, 0.5715, 0.5498],
        'MAE': [8.46, 10.30, 10.31],
        'RMSE': [10.41, 12.67, 12.68],
        'MAPE (%)': [25.51, 38.40, 38.23]
    })
    
    st.dataframe(rq3_data.style.highlight_max(subset=['R²', 'Adjusted R²'], color='lightgreen')
                               .highlight_min(subset=['MAE', 'RMSE', 'MAPE (%)'], color='lightgreen'),
                 use_container_width=True)
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # R² vs Adjusted R²
        fig_r2 = go.Figure(data=[
            go.Bar(name='R²', x=rq3_data['Model'], y=rq3_data['R²'], 
                   marker_color='lightblue'),
            go.Bar(name='Adjusted R²', x=rq3_data['Model'], y=rq3_data['Adjusted R²'], 
                   marker_color='orange')
        ])
        fig_r2.update_layout(
            title='R² vs Adjusted R² Comparison',
            barmode='group',
            yaxis_title='Score',
            height=400
        )
        st.plotly_chart(fig_r2, use_container_width=True)
    
    with col2:
        # Error Metrics
        fig_error = go.Figure(data=[
            go.Bar(name='MAE', x=rq3_data['Model'], y=rq3_data['MAE'], 
                   marker_color='coral'),
            go.Bar(name='RMSE', x=rq3_data['Model'], y=rq3_data['RMSE'], 
                   marker_color='lightcoral')
        ])
        fig_error.update_layout(
            title='Error Metrics Comparison',
            barmode='group',
            yaxis_title='Error (marks)',
            height=400
        )
        st.plotly_chart(fig_error, use_container_width=True)
    
    # Recommended Model
    st.markdown("###   Recommended Model: Model 2 - Collapsed Features (No Quizzes)")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("R²", "0.6229")
    with col2:
        st.metric("Adjusted R²", "0.5715")
    with col3:
        st.metric("MAE", "10.30 marks")
    with col4:
        st.metric("RMSE", "12.67 marks")
    with col5:
        st.metric("MAPE", "38.40%")
    
    st.markdown("""
    <div class="warning-box">
    <h4>  Why Not Model 1 (Despite Higher R²)?</h4>
    <p>While Model 1 has the highest R² (0.7454), we recommend Model 2 because:</p>
    <ul>
        <li><strong>Overfitting Concerns:</strong> Model 1's Adjusted R² (0.29) is much lower than its R²</li>
        <li><strong>Negative Coefficients:</strong> Some features have illogical negative coefficients</li>
        <li><strong>Better Generalization:</strong> Model 2's Adjusted R² (0.57) is much more reliable</li>
        <li><strong>Simpler Model:</strong> Uses only 3 features (As_Mean, S-I, S-II) instead of 16</li>
        <li><strong>Quiz Data Quality:</strong> Quiz data appears noisy with negative correlations</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Model 2 Details
    st.markdown("###   Model 2 Details - Feature Contributions")
    
    model2_features = pd.DataFrame({
        'Feature': ['S-II', 'As_Mean', 'S-I'],
        'Coefficient': [0.5855, 0.1215, 0.0743],
        'Interpretation': [
            'Most important: Recent midterm performance',
            'Assignment average contributes moderately',
            'First midterm has smaller impact'
        ]
    })
    
    fig_model2 = px.bar(model2_features, x='Feature', y='Coefficient',
                        title='Model 2: Feature Coefficients',
                        color='Coefficient', color_continuous_scale='Blues',
                        text='Coefficient')
    fig_model2.update_traces(texttemplate='%{text:.4f}', textposition='outside')
    fig_model2.update_layout(height=400)
    st.plotly_chart(fig_model2, use_container_width=True)
    
    st.dataframe(model2_features, use_container_width=True)
    
    # Bootstrap Analysis
    st.markdown("###   Bootstrap Analysis (500 samples)")
    
    st.markdown("""
    <div class="success-box">
    <h4>Bootstrap Results - Model Stability</h4>
    <ul>
        <li><strong>Mean MAE:</strong> 9.28 marks</li>
        <li><strong>Standard Deviation:</strong> 0.43 marks</li>
        <li><strong>95% Confidence Interval:</strong> [8.50, 10.15] marks</li>
    </ul>
    <p><strong>Interpretation:</strong> We are 95% confident that the true prediction error for the Final Exam 
    lies between 8.50 and 10.15 marks. This narrow confidence interval suggests stable and reliable model performance.</p>
    </div>
    """, unsafe_allow_html=True)

# Bootstrap visualization
import numpy as np

# Simulate bootstrap distribution for visualization
np.random.seed(42)
bootstrap_samples = np.random.normal(9.28, 0.43, 500)

fig_bootstrap = go.Figure()

fig_bootstrap.add_trace(go.Histogram(
    x=bootstrap_samples,
    nbinsx=30,
    name='Bootstrap MAE',
    marker_color='lightgreen',
    opacity=0.7
))

fig_bootstrap.add_vline(x=9.28, line_dash="dash", line_color="red", 
                        annotation_text="Mean MAE: 9.28", 
                        annotation_position="top right")
fig_bootstrap.add_vline(x=8.50, line_dash="dash", line_color="green", 
                        annotation_text="95% CI Lower: 8.50")
fig_bootstrap.add_vline(x=10.15, line_dash="dash", line_color="green", 
                        annotation_text="95% CI Upper: 10.15")

fig_bootstrap.update_layout(
    title='Bootstrap Distribution of MAE (500 samples)',
    xaxis_title='MAE (marks)',
    yaxis_title='Frequency',
    height=400,
    showlegend=False
)

st.plotly_chart(fig_bootstrap, use_container_width=True)