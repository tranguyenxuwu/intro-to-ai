
# thư viện
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# Hàm load dữ liệu
def load_data_drug(path='../Data/drug200.csv'):
    """Load dữ liệu thuốc từ file CSV."""
    data = pd.read_csv(path)
    return data

# Hàm train GaussianNB
def train_gaussian_model(data):
    """Huấn luyện mô hình GaussianNB, trả về model, cột đặc trưng, mapping nhãn."""
    X = data.drop(['Drug'], axis=1)
    y = data['Drug']
    X = pd.get_dummies(X, dtype='int')
    label_map = {"drugA": 1, "drugB": 2, "drugC": 3, "drugX": 4, "DrugY": 5}
    inv_label_map = {v: k for k, v in label_map.items()}
    y_num = y.map(label_map)
    model = GaussianNB()
    model.fit(X, y_num)
    return model, X.columns.tolist(), inv_label_map

# Hàm dự đoán thuốc
def predict_drug(input_data, model, feature_columns, inv_label_map):
    """
    Dự đoán loại thuốc cho input (dict hoặc DataFrame 1 dòng).
    Trả về tên thuốc dự đoán và xác suất.
    """
    if isinstance(input_data, dict):
        input_df = pd.DataFrame([input_data])
    else:
        input_df = input_data.copy()
    input_df = pd.get_dummies(input_df, dtype='int')
    # Đảm bảo đủ cột như khi train
    for col in feature_columns:
        if col not in input_df:
            input_df[col] = 0
    input_df = input_df[feature_columns]
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]
    label = inv_label_map[pred]
    return label, proba

# Không có code thực thi trực tiếp để có thể import vào streamlit_app.py
