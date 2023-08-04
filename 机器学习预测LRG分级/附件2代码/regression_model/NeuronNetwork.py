import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
data = pd.read_excel('predict_data.xlsx')
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(8, 256)
        self.fc2 = nn.Linear(256,128)
        self.fc3 = nn.Linear(128,256)
        self.fc4 = nn.Linear(128,64)
        self.fc5 = nn.Linear(64,32)
        self.fc6 = nn.Linear(32,4)
        self.fc7 = nn.Linear(4, 1)

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

model = Net()

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(torch.Tensor(X_train.values))
    loss = criterion(outputs, torch.Tensor(y_train.values).unsqueeze(1))
    loss.backward()
    optimizer.step()

    print('Epoch [%d/%d], train_Loss:%.4f' % (epoch + 1,100 , loss))


with torch.no_grad():
    y_pred = model(torch.Tensor(X_test.values)).squeeze().numpy()
    y_pred = [min(max(round(y), 0), 5) for y in y_pred]

acc = accuracy_score(y_test, y_pred)
print('Accuracy:', acc)
plt.plot(list(range(len(y_pred))),y_pred,y_test.to_numpy())
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