import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import torch.nn.functional as F
import matplotlib.pyplot as plt

# 读取Excel表格数据
data = pd.read_excel('predict_data.xlsx')

# 提取特征和标签
features = data.iloc[:, :8].values
labels = data.iloc[:, -1].values

# 数据归一化
scaler = StandardScaler()
features = scaler.fit_transform(features)

# 标签编码
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)

# 划分训练集和测试集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=42)

# 转换为Tensor
train_features = torch.tensor(train_features, dtype=torch.float32)
train_labels = torch.tensor(train_labels, dtype=torch.long)
test_features = torch.tensor(test_features, dtype=torch.float32)

# 独热编码
num_classes = len(label_encoder.classes_)
train_labels = F.one_hot(train_labels, num_classes=num_classes).float()

# 定义神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(train_features.shape[1], 256)
        self.fc2 = nn.Linear(256,128)
        self.fc3 = nn.Linear(128,256)
        self.fc4 = nn.Linear(128,64)
        self.fc5 = nn.Linear(64,32)
        self.fc6 = nn.Linear(32,4)
        self.fc7 = nn.Linear(4, num_classes)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        y=x 
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc2(x+y))
        x = torch.relu(self.fc4(x))
        x = torch.relu(self.fc5(x))
        x = torch.relu(self.fc6(x))
        x = self.fc7(x)
        return x

# 初始化模型
model = Net()

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
epochs = 100
batch_size = 16
num_batches = len(train_features) // batch_size

for epoch in range(epochs):
    running_loss = 0.0
    test_loss = 0.0

    for i in range(num_batches):
        batch_features = train_features[i * batch_size: (i + 1) * batch_size]
        batch_labels = train_labels[i * batch_size: (i + 1) * batch_size]

        # 前向传播
        outputs = model(batch_features)
        loss = criterion(outputs, torch.argmax(batch_labels, dim=1))

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    

    # 在测试集上进行预测
    with torch.no_grad():
        model.eval()
        test_outputs = model(test_features)
        loss = criterion(outputs, torch.argmax(batch_labels, dim=1))

        test_loss += loss.item()


    print('Epoch [%d/%d], train_Loss:%.4f,test_Loss: %.4f' % (epoch + 1, epochs, running_loss / num_batches,test_loss/num_batches))

# 在测试集上进行预测
with torch.no_grad():
    model.eval()
    test_outputs = model(test_features)
    _, test_predictions = torch.max(test_outputs, 1)
    test_predictions = test_predictions.numpy()

# 计算准确度等指标
accuracy = (test_predictions == test_labels).mean()
print(accuracy)
plt.plot(list(range(len(test_predictions))), test_predictions,test_labels)
plt.show()

import numpy as np
def cross_entropy(y_true, y_pred):
    # 将实际分类结果和预测分类结果转换为Numpy数组
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    # 计算交叉熵
    loss = -np.mean(y_true * np.log(y_pred + 1e-8))
    return loss

loss = cross_entropy(test_predictions,test_labels)
print(loss)

import numpy as np
from sklearn.metrics import confusion_matrix
import itertools
# y_true为实际分类结果，y_pred为预测分类结果
cm = confusion_matrix(test_predictions, test_labels)
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