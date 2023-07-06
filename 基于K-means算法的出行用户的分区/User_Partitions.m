%提取数据
filename = 'data_customer.txt'; 
data = importdata(filename); 
location = [data(:,1:2);data(:,3:4)];
figure;
%出行用户出发点与到达点分布展示
x = location(:,1);
y = location(:,2);
scatter(x,y,5,'filled','MarkerFaceColor',[0 .255 .5]);

%使用K-means算法进行聚类
K = 10;
[idx, C] = kmeans(location, K,'MaxIter', 1000);

%分区结果展示
figure;
gscatter(location(:,1), location(:,2), idx);
hold on;
plot(C(:,1), C(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 2,'DisplayName', '聚类中心');

%各个分区中心位置
for i = 1:k
    fprintf('Cluster %d center: (%.4f, %.4f)\n', i, C(i,1), C(i,2));
end
