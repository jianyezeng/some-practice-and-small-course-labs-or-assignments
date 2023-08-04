import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
data = pd.read_excel('predict_data.xlsx', header=None)

X = data.iloc[1:, :-1]
y = data.iloc[1:, -1]


# 对特征进行标准化处理
scaler = StandardScaler()
X = scaler.fit_transform(X)



# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# 定义三个基模型：支持向量机、随机森林和线性回归
svm = SVR(kernel='linear')
rf = RandomForestRegressor(n_estimators=100, random_state=42)
lr = LinearRegression()
# 定义集成模型，并将三个基模型加入到集成模型中
ensemble = VotingRegressor(estimators=[('svm', svm), ('rf', rf), ('lr', lr)])
# 训练集成模型
ensemble.fit(X_train, y_train)



# 使用测试集来评估模型性能
y_pred = ensemble.predict(X_test)
# 对预测结果进行处理，使其满足题目要求
y_pred = np.clip(y_pred, 0, 5)
y_pred = np.round(y_pred)
# 计算预测结果与实际结果相同的比例
accuracy = np.mean(y_pred == y_test)
print('Accuracy:', accuracy)

plt.plot(list(range(len(y_test.to_numpy()))),y_pred,y_test.to_numpy())
plt.show()




cm = confusion_matrix(list(y_test), y_pred)
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