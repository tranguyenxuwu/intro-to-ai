
# Thư viện
import numpy as np
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer

# Hàm load dữ liệu

def load_data(path='../Data/Education.csv'):
    """Load dữ liệu từ file CSV."""
    data = pd.read_csv(path)
    return data

# Hàm train Bernoulli Naive Bayes

def train_bernoulli_model(data):
    """Huấn luyện mô hình BernoulliNB và vectorizer."""
    X = data['Text']
    y = data['Label'].map({"positive": 1, "negative": 0})
    vectorizer = CountVectorizer(binary=True, stop_words='english')
    X_vec = vectorizer.fit_transform(X)
    model = BernoulliNB()
    model.fit(X_vec, y)
    return model, vectorizer

# Hàm dự đoán

def predict_text_bernoulli(text, model, vectorizer):
    """Dự đoán nhãn (positive/negative) cho một đoạn văn bản."""
    X_input = vectorizer.transform([text])
    pred = model.predict(X_input)[0]
    proba = model.predict_proba(X_input)[0]
    label = "positive" if pred == 1 else "negative"
    return label, proba

# Lưu ý: Không có code thực thi trực tiếp ở đây để có thể import vào streamlit_app.py