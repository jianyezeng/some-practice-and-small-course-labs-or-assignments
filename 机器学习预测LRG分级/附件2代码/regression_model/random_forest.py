import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# 读取Excel表格数据
data = pd.read_excel('predict_data.xlsx')

# 将特征和标签分开
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练随机森林模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 预测测试集并进行处理
y_pred = rf.predict(X_test)
y_pred = [min(max(round(y), 0), 5) for y in y_pred]

# 对预测结果和实际结果进行比较
acc = accuracy_score(y_test, y_pred)
print('Accuracy:', acc)

plt.plot(list(range(len(y_test.to_numpy()))), y_pred,y_test.to_numpy())
plt.show()

import numpy as np
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