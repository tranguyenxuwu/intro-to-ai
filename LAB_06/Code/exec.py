
# Thư viện
import numpy as np
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


# Lấy dữ liệu
data = pd.read_csv('../Data/Education.csv')
data.head()


# tạo hàm train test
def split_train_test(data, ratio_test):
    np.random.seed(00)
    index_permu = np.random.permutation(len(data))
    data_permu = data.iloc[index_permu]
    test_size = int(len(data_permu)*ratio_test)
    train_set = data_permu.iloc[:-test_size]
    test_set = data_permu.iloc[-test_size:]
    return train_set, test_set


train_set, test_set = split_train_test(data, 0.2)
train_set.reset_index(drop = True, inplace = True)
test_set.reset_index(drop = True, inplace = True)
print("Kích thước tập train:", len(train_set))
print("Kích thước tập train:", len(test_set))


X_train, y_train = train_set['Text'], train_set['Label']
X_test, y_test = test_set['Text'], test_set['Label']
print(len(X_train), len(y_train))
print(len(X_test), len(y_test))
print(X_test)
print(y_test)


print(y_train.value_counts())
print(y_test.value_counts())


# chuyển đổi positive: 1 và negative: 0
print(y_train.head())
y_train = y_train.map({"positive": 1, "negative": 0})
y_train.head()


# count1: phân phối Bernoulli --> cài tham số binary: True
count1 = CountVectorizer(binary = True, stop_words = 'english') # dùng bộ lọc trong tiếng anh
count1.fit(X_train)
X_train = count1.transform(X_train)
print(X_train.toarray())
print(X_train.toarray().shape)


# xem tên các đặc trưng
get_name = count1.get_feature_names_out()
print(get_name)
print(len(get_name)) 


bernoulli = BernoulliNB()
model1 = bernoulli.fit(X_train, y_train)


# chuyển đổi X_test về ma trận trước khi dự đoán
# lưu ý: biến đổi dựa trên các đặc trưng của count 1
X_test = count1.transform(X_test)
print(X_test.toarray())
print(X_test.shape)


y_pred = model1.predict(X_test)
y_pred_proba = model1.predict_proba(X_test)
print(y_pred)
print(y_pred_proba)
y_pred_trans = np.where(y_pred == 0, "negative", "positive")
print(y_pred_trans)


list(zip(y_pred_trans, y_test))


# có 4 độ đo phổ biến cho bài toán phân loại: accuracy, precision, recall, F1 score


# confusion matrix
from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(y_test, y_pred_trans)
print(confusion)


# đối chiếu với lý thuyết ta thấy: TN = 2, FP = 4, FN = 0, TP = 4
TN = confusion[0][0]
FP = confusion[0][1]
FN = confusion[1][0]
TP = confusion[1][1]
print(TN, FP, FN, TP)


accuracy = (TP + TN)/len(y_pred_trans)
precision = TP/(TP + FP)
recall = TP/(TP + FN)
f1_score = round(2*(precision*recall)/(precision + recall), 2)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)


# hàm xem nhanh các độ đo
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred_trans))


#     negative       1.00      0.33      0.50         6
#     positive       0.50      1.00      0.67         4

#     accuracy                           0.60        10
#    macro avg       0.75      0.67      0.58        10
# weighted avg       0.80      0.60      0.57        10


# đường cong ROC, AUC
from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1], pos_label = 'positive')
# diện tích dưới đường cong ROC
auc = auc(fpr, tpr)
print(auc)


# vẽ đường cong ROC
import matplotlib.pyplot as plt
plt.plot([0, 1], [0, 1], linestyle = '--', color = 'gray')
plt.plot(fpr, tpr, marker = '.', color = 'green')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC')
plt.show()