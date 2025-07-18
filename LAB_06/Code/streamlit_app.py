import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# Import các hàm từ exec.py
from exec import load_data, train_bernoulli_model, predict_text_bernoulli
# Import các hàm từ exec_2.py
from exec_2 import load_data_drug, train_gaussian_model, predict_drug

st.set_page_config(
    page_title="Naive Bayes & Drug Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Ứng dụng AI: Phân loại văn bản & Dự đoán thuốc")

# Lựa chọn chức năng
option = st.selectbox(
    "Chọn chức năng:",
    ["Phân loại văn bản (Naive Bayes)", "Dự đoán thuốc (GaussianNB)"]
)

if option == "Phân loại văn bản (Naive Bayes)":
    st.markdown("Nhập văn bản để phân loại là **positive** hoặc **negative**.")
    st.markdown("---")
    @st.cache_resource
    def get_model():
        data = load_data()
        model, vectorizer = train_bernoulli_model(data)
        return model, vectorizer
    model, vectorizer = get_model()
    user_text = st.text_area(
        "Nhập văn bản cần phân loại:", 
        placeholder="Nhập nội dung giáo dục...",
        height=100
    )
    submit_button = st.button("🚀 Phân loại", type="primary", use_container_width=True)
    if user_text and submit_button:
        label, proba = predict_text_bernoulli(user_text, model, vectorizer)
        confidence = np.max(proba) * 100
        if label == "positive":
            st.success(f"**Kết quả dự đoán:** {label.title()}")
        else:
            st.error(f"**Kết quả dự đoán:** {label.title()}")
        st.info(f"**Xác suất tự tin:** {confidence:.1f}%")
        prob_df = pd.DataFrame({
            'Class': ['Negative', 'Positive'],
            'Probability (%)': proba * 100
        })
        fig_prob = px.bar(
            prob_df, x='Class', y='Probability (%)', 
            title="Xác suất dự đoán (%)",
            color='Class',
            color_discrete_map={'Negative': 'red', 'Positive': 'green'}
        )
        fig_prob.update_layout(height=300)
        st.plotly_chart(fig_prob, use_container_width=True)
    st.markdown("---")
    st.markdown("### 💡 Thử các ví dụ sau:")
    sample_texts = [
        "This course provides excellent learning opportunities and valuable knowledge.",
        "The educational program was poorly designed and not helpful."
    ]
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Văn bản tích cực"):
            st.text_area("Văn bản mẫu:", value=sample_texts[0], key="sample1")
    with col2:
        if st.button("Văn bản tiêu cực"):
            st.text_area("Văn bản mẫu:", value=sample_texts[1], key="sample2")

elif option == "Dự đoán thuốc (GaussianNB)":
    st.markdown("Nhập thông tin bệnh nhân để dự đoán loại thuốc phù hợp.")
    st.markdown("---")
    @st.cache_resource
    def get_drug_model():
        data = load_data_drug()
        model, feature_columns, inv_label_map = train_gaussian_model(data)
        return model, feature_columns, inv_label_map
    model, feature_columns, inv_label_map = get_drug_model()
    with st.form("drug_form"):
        age = st.number_input("Age", min_value=0, max_value=120, value=50)
        sex = st.selectbox("Sex", ["F", "M"])
        bp = st.selectbox("BP", ["LOW", "NORMAL", "HIGH"])
        cholesterol = st.selectbox("Cholesterol", ["NORMAL", "HIGH"])
        na_to_k = st.number_input("Na_to_K", min_value=0.0, max_value=100.0, value=15.0, step=0.1)
        submit_drug = st.form_submit_button("🚀 Dự đoán thuốc")
    if submit_drug:
        input_data = {
            "Age": age,
            "Sex": sex,
            "BP": bp,
            "Cholesterol": cholesterol,
            "Na_to_K": na_to_k
        }
        label, proba = predict_drug(input_data, model, feature_columns, inv_label_map)
        confidence = np.max(proba) * 100
        st.success(f"**Loại thuốc dự đoán:** {label}")
        st.info(f"**Xác suất tự tin:** {confidence:.1f}%")
        # Hiển thị xác suất cho từng loại thuốc
        drug_labels = [inv_label_map[i+1] for i in range(len(proba))]
        prob_df = pd.DataFrame({
            'Drug': drug_labels,
            'Probability (%)': proba * 100
        })
        fig_prob = px.bar(
            prob_df, x='Drug', y='Probability (%)', 
            title="Xác suất dự đoán từng loại thuốc (%)",
            color='Drug'
        )
        fig_prob.update_layout(height=300)
        st.plotly_chart(fig_prob, use_container_width=True)
