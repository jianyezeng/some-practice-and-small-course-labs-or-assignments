import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# 读取Excel表格数据
data = pd.read_excel('predict_data.xlsx', header=None)
# 将前8列作为特征X，最后一列作为标签y
X = data.iloc[1:, :-1].values
y = data.iloc[1:, -1].values

import numpy as np

# 定义预测结果的处理函数
def process_result(y_pred):
    y_pred = [min(max(round(y), 0), 5) for y in y_pred]
    return y_pred

# 对标签y进行处理
y = process_result(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestRegressor

# 定义集成模型
class EnsembleModel():
    def __init__(self):
        self.svm = SVC(kernel='linear', C=1.0, probability=True)
        self.rf = RandomForestRegressor(n_estimators=100)

    def fit(self, X, y):
        # 训练支持向量机模型
        self.svm.fit(X, y)

        # 训练随机森林模型
        self.rf.fit(X, y)

    def predict(self, X):
        # 对特征X进行预测
        svm_proba = self.svm.predict_proba(X)[:, 1]
        rf_proba = self.rf.predict(X)
        y_pred = (svm_proba + rf_proba) / 2
        y_pred = process_result(y_pred)
        return y_pred

# 构建集成模型
ensemble_model = EnsembleModel()

# 训练集成模型
ensemble_model.fit(X_train, y_train)

# 对训练数据进行预测
y_pred = ensemble_model.predict(X_test)

# 计算预测结果与实际结果相同所占的比例
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

plt.plot(list(range(len(y_test))),y_pred,y_test)
plt.show()


from sklearn.metrics import confusion_matrix
import itertools
# y_true为实际分类结果，y_pred为预测分类结果
cm = confusion_matrix(y_test, y_pred)
print(cm)
# 绘制混淆矩阵图像
plt.imshow(cm, cmap=plt.cm.Blues)

# 添加颜色条
plt.colorbar()

# 设置坐标轴标签
classes = list(range(6))
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)

# 设置坐标轴刻度
thresh = cm.max() / 2.
for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    plt.text(j, i, format(cm[i, j], 'd'),
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black")

# 添加标题
plt.title("Confusion Matrix")

# 显示图像
plt.show()