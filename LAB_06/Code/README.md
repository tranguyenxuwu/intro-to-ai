# LAB_06

## Chức năng các file

- Các file python này code chính lấy từ file notebook có sẵn nhưng được sửa lại để streamlit có thể sử dụng các function từ `exec.py` và `exec_2.py` dưới dạng module-hóa

- **exec.py**

  - `load_data`: Đọc dữ liệu văn bản.
  - `train_bernoulli_model`: Huấn luyện mô hình Bernoulli Naive Bayes cho phân loại text.
  - `predict_text_bernoulli`: Dự đoán nhãn (positive/negative) cho văn bản.

- **exec_2.py**

  - `load_data_drug`: Đọc dữ liệu thuốc.
  - `train_gaussian_model`: Huấn luyện mô hình GaussianNB cho dự đoán thuốc.
  - `predict_drug`: Dự đoán loại thuốc phù hợp dựa trên thông tin bệnh nhân.

- **streamlit_app.py**
  - Giao diện web cho phép chọn giữa 2 chức năng:
  - Phân loại văn bản (Naive Bayes)
  - Dự đoán thuốc (GaussianNB)

## Ảnh demo web

### Phân loại văn bản Naive Bayes

![Naive Bayes](<../Ảnh/Screenshot%20(18).png>)

### Dự đoán thuốc GaussianNB

![GaussianNB](<../Ảnh/Screenshot%20(17).png>)
