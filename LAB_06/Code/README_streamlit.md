# Naive Bayes Text Classification Streamlit App

This Streamlit application provides an interactive visualization of Naive Bayes text classification results using the Education.csv dataset.

## Features

### 📊 Dataset Overview

- Display dataset statistics and sample data
- Visualize class distribution with interactive charts

### 🤖 Model Training and Results

- **Bernoulli Naive Bayes**: Uses binary features (word presence/absence)
- **Multinomial Naive Bayes**: Uses count features (word frequencies)

### 📈 Performance Comparison

- Side-by-side comparison of both models
- Interactive metrics visualization
- Performance comparison charts

### 🔍 Detailed Analysis

- **Confusion Matrices**: Interactive heatmaps for both models
- **ROC Curves**: With AUC scores for performance evaluation
- **Classification Reports**: Detailed precision, recall, and F1-score breakdowns

### 🎯 Feature Analysis

- **Feature Importance**: Top words contributing to positive/negative classifications
- **Vocabulary Comparison**: Size differences between model vectorizers

### 🔮 Interactive Predictions

- Real-time text classification
- Prediction confidence scores
- Probability distributions for both models

## How to Run

### Option 1: Using the batch file (Windows)

1. Double-click `run_app.bat`
2. Wait for package installation
3. The app will open in your default browser

### Option 2: Manual installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run streamlit_app.py
   ```

3. Open your browser to the provided URL (typically http://localhost:8501)

## App Structure

### Main Sections:

1. **Configuration Sidebar**: Adjust test set ratio
2. **Dataset Overview**: Basic statistics and data preview
3. **Model Training**: Automated training of both Naive Bayes variants
4. **Tabbed Results**:
   - Performance Comparison
   - Detailed Analysis
   - Feature Analysis
5. **Interactive Prediction**: Test your own text inputs

### Key Visualizations:

- **Bar Charts**: Class distribution and performance metrics
- **Heatmaps**: Confusion matrices
- **Line Charts**: ROC curves
- **Horizontal Bar Charts**: Feature importance analysis
- **Real-time Predictions**: With confidence scores

## Understanding the Results

### Bernoulli vs Multinomial Naive Bayes:

- **Bernoulli**: Better for shorter texts, focuses on word presence
- **Multinomial**: Better for longer texts, considers word frequencies

### Metrics Explanation:

- **Accuracy**: Overall correct predictions
- **Precision**: How many positive predictions were actually positive
- **Recall**: How many actual positives were correctly identified
- **F1-Score**: Harmonic mean of precision and recall
- **AUC**: Area Under the ROC Curve (higher is better)

### Feature Importance:

- Shows which words most strongly indicate positive or negative sentiment
- Helps understand model decision-making process

## Dataset

The app uses the Education.csv dataset containing:

- **Text**: Educational text snippets
- **Label**: Sentiment labels (positive/negative)

## Technical Details

- **Framework**: Streamlit for web interface
- **ML Library**: scikit-learn for Naive Bayes implementation
- **Visualization**: Plotly for interactive charts
- **Data Processing**: Pandas and NumPy

## Customization

You can modify the app by:

- Changing the test set ratio in the sidebar
- Adjusting the number of top features displayed
- Adding new visualization types
- Experimenting with different text preprocessing options

Enjoy exploring your Naive Bayes text classification results! 🚀
