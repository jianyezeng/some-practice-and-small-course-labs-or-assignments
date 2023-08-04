import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
import graphviz
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# 读取Excel表格数据
data = pd.read_excel('predict_data.xlsx')

# 将特征和标签分开
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 将标签转换为有序分类问题的类别标签
y = pd.Categorical(y, categories=[0, 1, 2, 3, 4, 5], ordered=True)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练决策树模型
tree = DecisionTreeClassifier(max_depth=5)
tree.fit(X_train, y_train)

# 预测测试集并计算准确率
y_pred = tree.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print('Decision Tree Accuracy:', acc)

# 输出决策树组成
dot_data = export_graphviz(tree, out_file=None, feature_names=X.columns.astype(str), class_names=y.categories.astype(str), filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('decision_tree', format='png')
plt.plot(list(range(len(y_test))), y_pred,y_test)
plt.show()

import numpy as np
def cross_entropy(y_true, y_pred):
    # 将实际分类结果和预测分类结果转换为Numpy数组
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    # 计算交叉熵
    loss = -np.mean(y_true * np.log(y_pred + 1e-8))
    return loss

loss = cross_entropy(y_test, y_pred)
print(loss)

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